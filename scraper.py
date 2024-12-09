from yahoo_fin import news
import pandas as pd

def news_scraper(ticker):
    return pd.DataFrame(news.get_yf_rss(ticker))
