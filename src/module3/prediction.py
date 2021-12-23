import torch
from transformers import AutoTokenizer
from transformers import AutoModelForTokenClassification, TrainingArguments, Trainer

label_list = ['O', 'B-event', 'I-event', 'B-loc', 'I-loc', 'B-pers', 'I-pers', 'B-pro', 'I-pro', 'B-fac', 'I-fac',
              'B-org', 'I-org']

tokenizer = AutoTokenizer.from_pretrained('./un-ner.model/')

paragraph = '''آقای عباسی'''
tokens = tokenizer(paragraph)
torch.tensor(tokens['input_ids']).unsqueeze(0).size()

model = AutoModelForTokenClassification.from_pretrained('./un-ner.model/', num_labels=len(label_list))
predictions = model.forward(input_ids=torch.tensor(tokens['input_ids']).unsqueeze(0), attention_mask=torch.tensor(tokens['attention_mask']).unsqueeze(0))
predictions = torch.argmax(predictions.logits.squeeze(), axis=1)
predictions = [label_list[i] for i in predictions]

words = tokenizer.batch_decode(tokens['input_ids'])
pd.DataFrame({'ner': predictions, 'words': words}).to_csv('un_ner.csv')