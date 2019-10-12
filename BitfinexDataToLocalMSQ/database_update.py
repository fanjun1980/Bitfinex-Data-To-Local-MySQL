import ccxt
from BitfinexDataToLocalMSQ.DB_Local_utils_load import *
from BitfinexDataToLocalMSQ.GlobalObjects import symbols_usd

'''
database_update.py 会在本地MySQL的指定数据库db_name_update中将需要更新的交易对数据进行更新，
其中需要更新的交易对存放在列表变量update_symbols中，
对于其中的每一个交易对，程序会找到最后一条K线时间点，然后从这里接着下载接下来的数据并将其接入这张表中。
'''
update_symbols = symbols_usd

pd.set_option('expand_frame_repr', False)
pd.set_option('max_rows', 20)

bitfinex = ccxt.bitfinex({'timeout': 1000})

timeframe = '1m'
db_name_update = 'cc_bitfinex_hd_1m'
time_sh_utc_hours_diff = 8

list_obj_tableupdate = [CallTableUpdate(symbol=i, exchange=bitfinex, timeframe=timeframe, time_sh_utc_hours_diff=time_sh_utc_hours_diff, db_name=db_name_update) for i in update_symbols]
list_obj_tableupdate_remain = run_function_list(object_list=list_obj_tableupdate)

print('=' * 100)
print([i.symbol for i in list_obj_tableupdate_remain])
