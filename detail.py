import yfinance as yf

def ticker_detail(ticker):
    stock = yf.Ticker(ticker)
    stock_info = stock.info
    return {
        "Current Price $": stock_info.get("currentPrice"),
        "Open Price $": stock_info.get("open"),
        "Bid Price $": stock_info.get("bid"),
        "Ask Price $": stock_info.get("ask"),
        "Bid-Ask Spread $": round(stock_info.get("ask", 0) - stock_info.get("bid", 0), 2),
        "Previous Close $": stock_info.get("previousClose"),
        "Day High $": stock_info.get("dayHigh"),
        "Day Low $": stock_info.get("dayLow"),
        "Market Cap $": stock_info.get("marketCap"),
        "PE Ratio (TTM)": stock_info.get("trailingPE"),
        "EPS (TTM) $": stock_info.get("trailingEps"),
        "Beta": stock_info.get("beta"),
        "Volume": stock_info.get("volume"),
        "Industry": stock_info.get("sector")
    }
