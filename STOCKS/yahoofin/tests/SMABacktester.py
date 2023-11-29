import pandas  as pd #Data manipulation
import numpy as np #Data manipulation
import yfinance as yf
import matplotlib.pyplot as plt
plt.style.use("seaborn-v0_8")

class SMABacktester :
    def __init__(self) -> None:
        print("Inner class")
"""     def __init__(self, symbol):
        self.symbol = symbol
        self.df = yf.download(tickers=self.symbol) # no period brings all
        self.df.head()

    def getSymbol(self, symbol):
        return self.df[[symbol]] """