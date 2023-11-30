import pandas  as pd #Data manipulation
import numpy as np #Data manipulation
import yfinance as yf
from scipy.optimize import brute

import matplotlib.pyplot as plt
plt.style.use("seaborn")

class SMABacktester:
    def __init__(self, symbol, smas) -> None:
        self.symbol = symbol
        self.df = yf.download(tickers=self.symbol) # no period brings all
        (self.sma_s, self.sma_l) = smas
        self.df.head()

    def getSymbol(self, symbol):
        # https://www.geeksforgeeks.org/how-to-combine-two-dataframe-in-python-pandas/
        tmp_df = pd.concat([self.df.Open[[symbol]], self.df.High[[symbol]], self.df.Low[[symbol]], self.df.Close[[symbol]], self.df.Volume[[symbol]]], axis=1, join='inner')
        tmp_df.columns = ['Open', 'High', 'Low', 'Close', 'Volume']
        return tmp_df
    
    def setSymbol(self, symbol):
        self.tmp_df = self.getSymbol(symbol)        
    
    def setParameters(self, smas):
        (self.sma_s, self.sma_l) = smas

    def run_strategy(self, smas):
        if smas == ():
            smas = (self.sma_s, self.sma_l)
        data = self.tmp_df.copy()
        data["Returns"] = np.log(data.Close.div(data.Close.shift(1)))
        data["SMA_S"]   = data.Close.rolling(int(smas[0])).mean()
        data["SMA_L"]   = data.Close.rolling(int(smas[1])).mean()
        data.dropna(inplace=True)
        
        data["Position"] = np.where(data["SMA_S"] > data["SMA_L"], 1, -1)
        data["Strategy"] = data.Position.shift(1) * data["Returns"]
        data.dropna(inplace=True)
        return data[["Returns", "Strategy"]].sum().apply(np.exp)#[-1] # absolute performance & over performance
        
    def run_strategy2(self, smas):
        if smas == ():
            smas = (self.sma_s, self.sma_l)
        data = self.tmp_df.copy()
        data["Returns"] = np.log(data.Close.div(data.Close.shift(1)))
        data["SMA_S"]   = data.Close.rolling(int(smas[0])).mean()
        data["SMA_L"]   = data.Close.rolling(int(smas[1])).mean()
        data.dropna(inplace=True)
        
        data["Position"] = np.where(data["SMA_S"] > data["SMA_L"], 1, -1)
        data["Strategy"] = data.Position.shift(1) * data["Returns"]
        data.dropna(inplace=True)
        return -data[["Returns", "Strategy"]].sum().apply(np.exp)[-1] # maximize absolute performance
        
    def plot_results(self, smas, title="EUR/USD - "):
        if smas == ():
            smas = (self.sma_s, self.sma_l)
        data = self.tmp_df.copy()
        data["Returns"] = np.log(data.Close.div(data.Close.shift(1)))
        data["SMA_S"]   = data.Close.rolling(int(smas[0])).mean()
        data["SMA_L"]   = data.Close.rolling(int(smas[1])).mean()
        data.dropna(inplace=True)
        
        data["Position"]  = np.where(data["SMA_S"] > data["SMA_L"], 1, -1)
        data["Strategy"]  = data.Position.shift(1) * data["Returns"]
        data["Creturns"]  = data.Returns.cumsum().apply(np.exp)
        data["Cstrategy"] = data.Strategy.cumsum().apply(np.exp)

        title += " SMA{}, SMA{}"
        data[["Creturns", "Cstrategy"]].plot(title=title.format(smas[0], smas[1]), fontsize=12)
        plt.show()
    
    def plot_positions(self, smas, title="EUR/USD - "):
        if smas == ():
            smas = (self.sma_s, self.sma_l)
        data = self.tmp_df.copy()
        data["Returns"] = np.log(data.Close.div(data.Close.shift(1)))
        data["SMA_S"]   = data.Close.rolling(int(smas[0])).mean()
        data["SMA_L"]   = data.Close.rolling(int(smas[1])).mean()
        data.dropna(inplace=True)
        
        data["Position"]  = np.where(data["SMA_S"] > data["SMA_L"], 1, -1)
        title += " SMA{}, SMA{}"
        data[["Close", "SMA_S", "SMA_L", "Position"]].plot(secondary_y="Position", title=title.format(smas[0], smas[1]), fontsize=12)
        plt.show()
        
        
    def optimize_parameters(self, rranges):
        print(rranges)
        brute_strats = brute(self.run_strategy2, rranges)
        return brute_strats