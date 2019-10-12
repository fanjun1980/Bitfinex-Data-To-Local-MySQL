# -*- coding:utf-8 -*-
import pandas as pd
from sqlalchemy import create_engine

"""
@author:fanjun
@file  :export_kline.py
@time  :2019/8/910:32
"""
pd.set_option('expand_frame_repr', False)
pd.set_option('max_rows', 20)


def export_csv(db_name, name_table):
    engine = create_engine(f'mysql://fanjun:123456@192.168.1.154/{db_name}')
    query = f'select time as candle_begin_time,open,high,low,close,volume from {name_table} where time>"2018-01-01 00:00:00" order by time;'
    record_last = pd.read_sql(sql=query, con=engine)  # .sort_values(by=['candle_begin_time'], ascending=True)
    print(record_last.tail(10))
    record_last.to_csv(f'e:/{name_table}.csv', index=False)


def export_h5(db_name, name_table):
    engine = create_engine(f'mysql://fanjun:123456@192.168.1.154/{db_name}')
    query = f'select time as candle_begin_time,open,high,low,close,volume from {name_table} where time>"2018-01-01 00:00:00" order by time;'
    record_last = pd.read_sql(sql=query, con=engine)  # .sort_values(by=['candle_begin_time'], ascending=True)
    print(record_last.tail(10))
    record_last.to_hdf(f'e:/{name_table}.h5', key='all_data', mode='w')


export_csv('cc_bitfinex_hd_1m', 'btc_usd_1m')
export_h5('cc_bitfinex_hd_1m', 'btc_usd_1m')

export_csv('cc_bitfinex_hd_1m', 'eos_usd_1m')
export_h5('cc_bitfinex_hd_1m', 'eos_usd_1m')

export_csv('cc_bitfinex_hd_1m', 'eth_usd_1m')
export_h5('cc_bitfinex_hd_1m', 'eth_usd_1m')

export_csv('cc_bitfinex_hd_1m', 'xrp_usd_1m')
export_h5('cc_bitfinex_hd_1m', 'xrp_usd_1m')