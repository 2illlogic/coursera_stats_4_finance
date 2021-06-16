import pandas as pd
import yfinance as yf
import datetime as dt
import time
import requests
import io
import os

cwd = os.getcwd()
os.chdir(cwd + '/Documents/coursera/stats_4_finance')

#set start and end dates
start = dt.date.today() + dt.timedelta(days = -364)
end = dt.date.today()

#retrieve tickers and company info
table = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
df = table[0]
df.to_csv('sp500_info.csv')
df.to_csv('sp500_tickers.csv', columns=['Symbol'])

#tickers = read_csv('sp500_tickers')
tickers = pd.read_csv('tickers.csv')
tickers = tickers['tickers'].tolist()

#retrieve price data
prices = pd.DataFrame()

for i in tickers:
   try:
      stock = []
      stock = yf.download(i, start=start, end=end, progress=False)
      
      if len(stock) == 0:
         None
      else:
         stock['Ticker']=i
         prices = prices.append(stock,sort=False)
   except Exception:
      None

prices.to_csv('ex_stock_data.csv')
