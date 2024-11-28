import yfinance as yf

def get_financials(ticker):
    ticker_data = yf.Ticker(ticker)
    return ticker_data.financials

get_financials(arg1)
