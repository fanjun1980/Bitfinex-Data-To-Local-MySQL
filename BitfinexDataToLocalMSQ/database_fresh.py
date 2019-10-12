import ccxt
from BitfinexDataToLocalMSQ.DB_Local_utils_load import *
from BitfinexDataToLocalMSQ.GlobalObjects import symbols_usd, coins_picked

'''
database_fresh.py 会创建一个新的数据库，后缀为K线周期，然后将需要下载数据的交易对的历史数据下载到这个数据库中，
这些交易对名称存在列表变量fresh_symbols中，每个交易对的K线数据在一张表中，表的命名规范见上一条，
为了不让新创建的数据库覆盖掉之前的数据库，新库库名后面会加上当日的字符串（库创建好之后库名可以修改）。
'''
fresh_symbols = [i for i in symbols_usd if i.split('/')[0].lower() in coins_picked[:10]]
# fresh_symbols = [i for i in symbols_usd]

pd.set_option('expand_frame_repr', False)
pd.set_option('max_rows', 20)

bitfinex = ccxt.bitfinex({'timeout': 1000})

db_title = 'cc_bitfinex_hd'
timeframe = '1m'
db_name = '_'.join([db_title, timeframe])
db_con, db_name_new = local_fresh_db_con(db_name_title=db_name)
time_sh_utc_hours_diff = 8

list_obj_tablefresh = [CallTableFresh(symbol=i, exchange=bitfinex, timeframe=timeframe, time_sh_utc_hours_diff=time_sh_utc_hours_diff, db_con=db_con) for i in fresh_symbols]

list_obj_tablefresh_remain = run_function_list(object_list=list_obj_tablefresh)

print('=' * 100)
print([i.symbol for i in list_obj_tablefresh_remain])
