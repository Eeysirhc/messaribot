
import os
import sys
import requests

import pandas as pd 
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

from io import StringIO
from datetime import datetime, timedelta, date 

import matplotlib.pyplot as plt
import matplotlib as mpl


mpl.rcParams['figure.dpi'] = 300


def messari_fetch(coin):

  coin = coin.upper()

  # END DATE
  edate = datetime.today().date()

  base_url = "https://data.messari.io/api/v1/assets/{coin}/metrics/price/time-series?start=2020-01-01&end={edate}&interval=1d&format=csv".format(coin=coin, edate=edate)

  # MESSARI SECRET API KEY
  api_key = "YOUR_MESSARI_API_KEY_HERE"
  headers = {'x-messari-api-key': api_key}

  req = requests.get(base_url, headers=headers)
  data = StringIO(req.text)

  df_raw = pd.read_csv(data)
  df = df_raw
  
  # CONVERT TIMESTAMP AND DATE FORMATS
  df['timestamp'] = pd.to_datetime(df['timestamp'])
  df['date'] = df['timestamp'].dt.date 
  df['date'] = pd.to_datetime(df['date'])
  df['coin'] = coin
  
  df = df[['date', 'coin', 'open', 'high', 'low', 'close', 'volume']]

  df['date'] = pd.to_datetime(df['date'])
  
  # 100 DAY MOVING AVERAGE
  df['price_ma'] = df.rolling(window=100)['close'].mean()
  
  # VOLATILITY INDEX
  df['price_volatility'] = df['close'] / df['price_ma'] - 1
  
  # EXTRACT DATA FOR DYNAMIC TITLES
  dx = df.tail(1)

  # TOKEN NAME
  dx1 = dx.coin.to_string(index=False)

  # CLOSING PRICE
  dx['close'] = round(dx['close'], 4)
  dx2 = dx.close.to_string(index=False)

  # VOLATILITY INDEX PERCENTAGE
  dx['price_volatility'] = dx['price_volatility'] * 100
  dx['price_volatility'] = round(dx['price_volatility'], 2)
  dx3 = dx.price_volatility.to_string(index=False)
  
  # MERGE ALL DATA POINTS FOR TITLE
  title = str(dx1) + ": price of " + "$" + str(dx2) + " at " + str(dx3) + " % volatility"
  
  # PLOTTING FUNCTIONS
  plt.clf()
  plt.figure(figsize=(15,10))
  
  # DAILY PRICE CHART
  plt.subplot(2, 1, 1)
  plt.plot(df.date, df.close)
  plt.plot(df.date, df.price_ma, linestyle='--', color='salmon')
  plt.fill_between(df.date.values, df.high, df.low, alpha=0.3)
  plt.axhline(y=dx.close.item(), color='steelblue', linestyle=':')  
  plt.ylabel("Price ($)")
  plt.ylim(0, df.high.max()*1.20)
  plt.title(title, fontsize=15, horizontalalignment='left', x=0.05)
  
  # VOLATILITY INDEX CHART
  plt.subplot(2, 1, 2)
  plt.plot(df.date, df.price_volatility, color='black', alpha=0.5)
  plt.axhline(y=0.40, color='red', linestyle=':')
  plt.axhline(y=0.20, color='orange', linestyle=':')
  plt.axhline(y=0, color='grey', linestyle=':')
  plt.axhline(y=-0.20, color='green', linestyle=':')
  plt.axhline(y=-0.40, color='steelblue', linestyle=':')
  plt.fill_between(df.date.values, 0.20, 0.40, color='red', alpha=0.25)
  plt.fill_between(df.date.values, 0.00, 0.20, color='orange', alpha=0.25)
  plt.fill_between(df.date.values, 0.00, -0.20, color='green', alpha=0.25)
  plt.fill_between(df.date.values, -0.20, -0.40, color='steelblue', alpha=0.25)
  plt.ylabel("Volatility Index (%)")
  plt.ylim(df.price_volatility.min()-0.5, df.price_volatility.max()+0.5)
  
  plt.savefig("/YOUR/FILEPATH/NAME/HERE/toast.png")
  
  
