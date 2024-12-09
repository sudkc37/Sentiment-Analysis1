from flask import Flask, render_template, request
from scraper import news_scraper
from sentimentScore import get_sentiment_analyzer, sentiment_score
from detail import ticker_detail
from graph import plot_price
import os
import warnings

warnings.filterwarnings("ignore")

app = Flask(__name__)

tokenizer, model = get_sentiment_analyzer()

@app.route('/', methods=['GET', 'POST'])
def home():
    ticker = request.args.get('ticker', "").strip()
    market_sentiment = "N/A"
    sentiment_color = "gray"
    details = None
    plot_img = None  

    if request.method == 'POST':
        ticker = request.form.get('ticker', "").strip()

    if ticker:
        try:
            df = news_scraper(ticker)
            if 'summary' in df.columns:
                market_sentiment = sentiment_score(df, tokenizer, model)
                sentiment_color = {"Positive": "green", "Neutral": "yellow", "Negative": "red"}.get(market_sentiment, "gray")
        except Exception as e:
            print(f"Error in sentiment analysis: {e}")

        try:
            details = ticker_detail(ticker)
        except Exception as e:
            print(f"Error in fetching ticker details: {e}")

        try:
            plot_img = plot_price(ticker)
        except Exception as e:
            print(f"Error in generating plot: {e}")

    return render_template(
        'temp.html',
        sentiment=market_sentiment,
        color=sentiment_color,
        ticker_details=details,
        plot_img=plot_img  
    )

if __name__ == "__main__":
    app.run(debug=False, threaded=True, host="0.0.0.0", port=int("7001"))
