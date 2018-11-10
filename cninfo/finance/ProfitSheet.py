# -*- coding: UTF-8 -*- 
# Profit sheet. 利润表.
import http.client
import urllib
import json
from cninfo import D
from base import log
from base import base
from base import config
from base import cache

log = log.Log(__name__)

def call(codes, report_date=''):
    '''
    Query all profit sheet data by certain stock codes.
    Args:
        code: stock codes, split by comma(,) eg: 100001,100002
    Returns:
        1. no data, return ''
        2. profit sheet pandas.DataFrame.
    '''
    url = '/api/stock/p_stock2301'
    params = {
        'scode' : codes,
        'rdate' : report_date
    }
    resp = base.call_cache(config.cache_profit, url, params)
    if resp == '':
        return ''
    resp = json.loads(resp)
    records = resp['records']
    count = resp['count']
    return D.ProfitSheet.parses(records, count)
