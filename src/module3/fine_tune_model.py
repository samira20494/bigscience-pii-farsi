from datasets import load_metric
from transformers import AutoTokenizer
from transformers import AutoModelForTokenClassification, TrainingArguments, Trainer
from transformers import DataCollatorForTokenClassification
import numpy as np
from src.module3.preprocessing import get_un_token_dataset


def tokenize_and_align_labels(examples):
    label_all_tokens = True
    tokenized_inputs = tokenizer(list(examples["tokens"]), truncation=True, is_split_into_words=True)

    labels = []
    for i, label in enumerate(examples[f"{task}_tags"]):
        word_ids = tokenized_inputs.word_ids(batch_index=i)
        previous_word_idx = None
        label_ids = []
        for word_idx in word_ids:
            if word_idx is None:
                label_ids.append(-100)
            elif label[word_idx] == '0':
                label_ids.append(0)
            elif word_idx != previous_word_idx:
                label_ids.append(label_encoding_dict[label[word_idx]])
            else:
                label_ids.append(label_encoding_dict[label[word_idx]] if label_all_tokens else -100)
            previous_word_idx = word_idx
        labels.append(label_ids)

    tokenized_inputs["labels"] = labels
    return tokenized_inputs


def compute_metrics(p):
    predictions, labels = p
    predictions = np.argmax(predictions, axis=2)

    true_predictions = [[label_list[p] for (p, l) in zip(prediction, label) if l != -100] for prediction, label in
                        zip(predictions, labels)]
    true_labels = [[label_list[l] for (p, l) in zip(prediction, label) if l != -100] for prediction, label in
                   zip(predictions, labels)]

    results = metric.compute(predictions=true_predictions, references=true_labels)
    return {"precision": results["overall_precision"], "recall": results["overall_recall"], "f1": results["overall_f1"],
            "accuracy": results["overall_accuracy"]}


label_list = ['O', 'B-event', 'I-event', 'B-loc', 'I-loc', 'B-pers', 'I-pers', 'B-pro', 'I-pro', 'B-fac', 'I-fac',
              'B-org', 'I-org']

label_encoding_dict = {'': 0, 'O': 0, 'I-': 0, 'B-event': 1, 'I-event': 2, 'B-pers': 3, 'I-pers': 4,
                       'B-org': 5, 'I-org': 6, 'B-loc': 7, 'I-loc': 8, 'B-pro': 9, 'I-pro': 10, 'B-fac': 11, 'I-fac': 12}


task = "ner"
model_checkpoint = "HooshvareLab/bert-fa-zwnj-base"
batch_size = 16

tokenizer = AutoTokenizer.from_pretrained(model_checkpoint)

# preprocessing
train_dataset, test_dataset = get_un_token_dataset('../data/')

print(f"No. of training examples: {train_dataset.shape[0]}")
print(f"No. of testing examples: {test_dataset.shape[0]}")

train_tokenized_datasets = train_dataset.map(tokenize_and_align_labels, batched=True)
test_tokenized_datasets = test_dataset.map(tokenize_and_align_labels, batched=True)

print(f"Shape of training examples: {train_tokenized_datasets.shape}")
print(f"Shape of testing examples: {test_tokenized_datasets.shape}")

# fine-tuning

model_checkpoint = "HooshvareLab/bert-fa-zwnj-base"
model = AutoModelForTokenClassification.from_pretrained(model_checkpoint, num_labels=len(label_list))

args = TrainingArguments(
    f"test-{task}",
    evaluation_strategy="epoch",
    learning_rate=1e-4,
    per_device_train_batch_size=batch_size,
    per_device_eval_batch_size=batch_size,
    num_train_epochs=3,
    weight_decay=1e-5,
)

data_collator = DataCollatorForTokenClassification(tokenizer)
metric = load_metric("seqeval")

trainer = Trainer(
    model,
    args,
    train_dataset=train_tokenized_datasets,
    eval_dataset=test_tokenized_datasets,
    data_collator=data_collator,
    tokenizer=tokenizer,
    compute_metrics=compute_metrics
)

trainer.train()
trainer.evaluate()
trainer.save_model('model/armanperso-ner.model')