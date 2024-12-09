import yfinance as yf
import matplotlib.pyplot as plt
import datetime as dt
import matplotlib.dates as mdates
import matplotlib

matplotlib.use('Agg')

def plot_price(ticker):
    end_date = dt.datetime.now()
    start_date = (end_date - dt.timedelta(days=1)).date()
    quotes = yf.download(ticker, start=start_date, end=end_date, interval='1m')['Adj Close']

    if quotes.empty:
        return None

    plt.figure(figsize=(10, 5))
    plt.plot(quotes.index, quotes)
    plt.xlabel('Time')
    plt.ylabel('Price')
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d:%I:%M'))
    plt.xticks(rotation=45)
    plt.tight_layout()
    plot_path = f"static/{ticker}_price_plot.png"
    plt.savefig(plot_path)
    plt.close()
    return plot_path
