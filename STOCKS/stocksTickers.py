import numpy as np
import pandas as pd
# https://codedamn.com/news/python/importerror-modulenotfounderror-yaml-python
# https://github.com/portfolioplus/pytickersymbols/tree/master
from pytickersymbols import PyTickerSymbols

stock_data = PyTickerSymbols()
countries = stock_data.get_all_countries()
indices = stock_data.get_all_indices()
industries = stock_data.get_all_industries()

#print(industries)
#print(indices)

stocks_c = list(stock_data.get_stocks_by_industry('Cyclical Consumer Products'))

stocks_i = list(stock_data.get_stocks_by_industry('Industrials'))

stocks_m = list(stock_data.get_stocks_by_industry('Communications & Networking'))

df_stocks_c = pd.DataFrame(stocks_c)
print(df_stocks_c)
df_stocks_c.to_csv("consumer_stocks.csv", sep='\t')

df_stocks_i = pd.DataFrame(stocks_i)
df_stocks_i.to_csv("industrials_stocks.csv", sep='\t')

df_stocks_m = pd.DataFrame(stocks_m)
df_stocks_m.to_csv("communications_stocks.csv", sep='\t')
#stocks = list(stock_data.get_stocks_by_industry(22))

#stocks = list(stock_data.get_stocks_by_industry("Basic Materials"))
#def list_stocks(stocks):
#    for stock in stocks:
#        #is_in_basic = False
#        #for industry in stock["industries"]:
#        #    if "Basic Materials" in industry:
#        #        is_in_basic = True
#        print(stock)

#list_stocks(stocks_c)