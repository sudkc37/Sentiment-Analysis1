from transformers import AutoTokenizer, AutoModelForSequenceClassification

def embedding():
    model_path = "ProsusAI/finbert"
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = AutoModelForSequenceClassification.from_pretrained(model_path)
    return tokenizer, model

