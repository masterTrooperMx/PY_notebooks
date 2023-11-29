import pandas  as pd #Data manipulation
import numpy as np #Data manipulation
import yfinance as yf
import matplotlib.pyplot as plt
plt.style.use("seaborn-v0_8")

class SMABacktester:
    def __init__(self) -> None:
        print("classes!")