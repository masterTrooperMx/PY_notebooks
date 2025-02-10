# https://codedamn.com/news/python/importerror-modulenotfounderror-yaml-python
# https://github.com/portfolioplus/pytickersymbols/tree/master
from pytickersymbols import PyTickerSymbols

stock_data = PyTickerSymbols()
countries = stock_data.get_all_countries()
indices = stock_data.get_all_indices()
industries = stock_data.get_all_industries()

print(industries)
print(indices)