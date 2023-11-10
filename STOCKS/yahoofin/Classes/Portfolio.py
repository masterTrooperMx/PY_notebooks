import pandas  as pd #Data manipulation
import numpy as np #Data manipulation
import yfinance as yf
from datetime import datetime
import os.path

class Portfolio():
    def __init__(self, start=datetime.now().strftime("%Y-%m-%d"), end=datetime(2023, 12, 31).strftime("%Y-%m-%d")) -> None:
        self.symbols = ["GENIUS21.MX", "BIMBOA.MX", "HERDEZ.MX", "BOLSAA.MX", "IVVPESOISHRS.MX", "WALMEX.MX"]
        self.prices = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        self.startdate = start
        self.enddate = end
        # check if file is from today otherwise update it
        self.check_file(start, end)

    def check_file(self, start, end, fname="./data/stocks_portfolio.csv"):
        update_create = False
        delta = 0
        if os.path.exists(fname) and not update_create:
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
            self.portfolio_df = yf.download(tickers=self.symbols, start = start, end = end)
            print("saving data")
            self.save_csv(fname)

    def save_csv(self, fname="./data/stocks_portfolio.csv"):
        self.portfolio_df.to_csv(fname)

    def get_symbols(self):
        return self.symbols

    def load_csv(self):
        pass

    def portfolio_yearly(self):
        pass

    def portfolio_monthly(self):
        pass

    def portfolio_biweekly(self):
        pass

    def portfolio_weekly(self):
        pass