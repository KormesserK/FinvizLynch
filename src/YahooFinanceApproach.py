from yahoo_finance import *;
from finviz.screener import Screener;

filters = ['exch_nasd']
stock_list = Screener(filters=filters)

oneShare = Share('AAPL')
print(oneShare)




for f in stock_list:
        singleShare = Share(f.get("Ticker"))
        print(singleShare)












