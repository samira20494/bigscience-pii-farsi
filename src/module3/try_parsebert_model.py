from transformers import AutoConfig, AutoTokenizer, AutoModel, TFAutoModel

# v3.0
model_name_or_path = "HooshvareLab/bert-fa-zwnj-base"
config = AutoConfig.from_pretrained(model_name_or_path)
tokenizer = AutoTokenizer.from_pretrained(model_name_or_path)

# model = TFAutoModel.from_pretrained(model_name_or_path)  For TF
model = AutoModel.from_pretrained(model_name_or_path)

text = "ما در هوش‌واره معتقدیم با انتقال صحیح دانش و آگاهی، همه افراد میتوانند از ابزارهای هوشمند استفاده کنند. شعار ما هوش مصنوعی برای همه است."
tokens = tokenizer.tokenize(text)

print(tokens)

['ما', 'در', 'هوش', '[ZWNJ]', 'واره', 'معتقدیم', 'با', 'انتقال', 'صحیح', 'دانش', 'و', 'آ', '##گاهی', '،', 'همه', 'افراد', 'میتوانند', 'از', 'ابزارهای', 'هوشمند', 'استفاده', 'کنند', '.', 'شعار', 'ما', 'هوش', 'مصنوعی', 'برای', 'همه', 'است', '.']