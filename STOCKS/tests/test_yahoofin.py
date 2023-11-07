# https://www.analyticsvidhya.com/blog/2021/06/download-financial-dataset-using-yahoo-finance-in-python-a-complete-guide/

import pandas  as pd #Data manipulation
import numpy as np #Data manipulation
import yfinance as yf
from yahoofinancials import YahooFinancials

aapl_df = yf.download('AAPL')
aapl_df.head()
print(aapl_df)