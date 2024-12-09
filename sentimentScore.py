import torch
import pandas as pd
from languageModel import embedding

def get_sentiment_analyzer():
    return embedding()

def sentiment_score(df, tokenizer, model):
    def calculate_score(news):
        tokens = tokenizer.encode(news, return_tensors='pt')
        result = model(tokens)
        score = int(torch.argmax(result.logits)) + 1
        return 'Positive' if score == 3 else 'Neutral' if score == 2 else 'Negative'

    if 'summary' in df:
        df['Market Sentiments'] = df['summary'].apply(calculate_score)
        return df['Market Sentiments'].mode()[0]
    return "N/A"
