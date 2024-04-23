import pandas  as pd #Data manipulation
import numpy as np #Data manipulation
import yfinance as yf
from datetime import datetime
import os.path

class Portfolio():
    def __init__(self, symbols = ['EURUSD=X', 'AUDEUR=X', 'USDGBP=X'] , start=datetime.now().strftime("%Y-%m-%d"), end=datetime(2023, 12, 31).strftime("%Y-%m-%d")) -> None:
        self.symbols = symbols
        self.prices = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        self.startdate = start
        self.enddate = end
        # check if file is from today otherwise update it
        self.fname = ""
        self.check_file(start, end, True)

    def check_file(self, start, end, createF=False , fname="./data/stocks_portfolio.csv"):
        self.fname = fname
        update_create = createF
        #print(f"{update_create}-{self.get_symbols()}--{self.startdate}/{self.enddate}")
        delta = 0
        if os.path.exists(fname) and update_create != True:
            now = datetime.now()
            now_str = now.strftime('%Y-%m-%d %H:%M')
            mtime = os.path.getmtime(filename=fname)
            timestamp = datetime.fromtimestamp(mtime)
            timestamp_str = timestamp.strftime('%Y-%m-%d %H:%M')
            delta = now - timestamp
            print(f"Stock cvs exists: {timestamp_str}")
            if delta.days >= 1:
                update_create = True
                print(f"file, it is {delta.days} old")

        if update_create:
            print("Updating file with new data")
            # part of class
            self.portfolio_df = yf.download(tickers=self.get_symbols(), start = start, end = end)
            #print(f"getting info {self.portfolio_df.head()}")
            print(f"saving data into {self.fname}")
            self.save_csv(self.fname)

    def set_symbols(self, symbols):
        self.symbols = symbols

    def save_csv(self, fname):
        self.portfolio_df.to_csv(fname)

    def get_symbols(self):
        return self.symbols

    def load_csv(self, symbol):
        pass

    def portfolio_yearly(self):
        # show all years from symbol
        sy_df = pd.to_datetime(self.symbol_df.index)
        #print(symbol_df.year.unique())
        l_symbol_years = list(sy_df.year.unique())
        #print(f"Years to count: {l_symbol_years} for symbol")
        # as part of timeseries characteristics index can be string
        year = input(f"what year: {l_symbol_years} ").upper()
        print(self.symbol_df[year])

    def portfolio_monthly(self):
        pass

    def portfolio_biweekly(self):
        pass

    def portfolio_weekly(self):
        pass
    
    def process_data_symbol(self):
        if not self.symbol_df.empty:
            self.portfolio_yearly()
            # and the others
        else:
            print("Don't have data frame for symbol!!")
    
    def portfolio_show_data(self, symbol):
        # symbol is just the name
        if symbol != "":
            # creating symbol to analysis into class
            self.symbol_df = self.portfolio_df.filter(like=symbol).filter(regex="(Close|High)")
            print(f"SHOWING {symbol} {self.symbol_df.info()}")
            self.process_data_symbol()
        else:
            print("No symbol passed ... nothing to show")