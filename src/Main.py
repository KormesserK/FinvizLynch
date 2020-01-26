from finviz.screener import Screener;


filters = ['exch_nasd', 'fa_PEG_low', 'fa_EPS_high', 'fa_EPS past 5Y_high',]
stock_list = Screener(filters=filters, order='-EPS')


print(stock_list)

stock_list.to_csv()

"print(stock_list)"


print('-----------------------------------')