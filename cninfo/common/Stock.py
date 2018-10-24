# -*- coding: UTF-8 -*- 
import json
from cninfo import D
from base import log
from base import base

def call(codes):
    '''Query base info of stock by code.
    
    Args:
        code: stock codes, separated by comma(,), eg:000001,600000
    Returns:
        1. no data, return ''.
        2. one record, return stock object.
        3. mulitple records, return stock object dict, eg {code: object, ...}
    '''
    url = '/api/stock/p_stock2101'
    params = {
        'scode' : codes
    }
    resp = base.call(url, params)
    if resp == '':
        return ''
    resp = json.loads(resp)
    records = resp['records']
    count = resp['count']
    return D.Stock.parses(records, count)
