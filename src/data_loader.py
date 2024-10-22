import yfinance as yf
import pandas as pd

def get_data(tickers, start, end):
    data = yf.download(tickers, start=start, end=end)
    return data['Adj close'] # Adjustované ceny

# Příklad načtení dat pro S&P 500
s&p500_data = get_data('^GSPC', '2010-01-01', '2023-01-01')
s&p500_data.to_csv('data/s&p500.csv')