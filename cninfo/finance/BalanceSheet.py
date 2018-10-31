# -*- coding: UTF-8 -*- 
# Balance sheet. 资产负债表.
import http.client
import urllib
import json
from cninfo import D
from base import log
from base import base
from base import config
from base import cache

log = log.Log(__name__)

def call(codes, report_date):
    url = '/api/stock/p_stock2300'
    params = {
        'scode' : codes,
        'rdate' : report_date
    }
    resp = base.call_cache(config.cache_balance, url, params)
    if resp == '':
        return ''
    resp = json.loads(resp)
    records = resp['records']
    count = resp['count']
    return D.BalanceSheet.parses(records, count)

def code(code):
    '''
    Query all balance sheet data by certain stock code.
    Args:
        code: stock code.
    Returns:
        1. no data, return ''
        2. Balance sheet dict list.
    '''
    return call(code, '')

def codes(codes):
    '''
    Query all balance sheet data by certain stock codes.
    Args:
        code: stock codes, split by comma(,) eg: 100001,100002
    Returns:
        1. no data, return ''
        2. Balance sheet dict list.
    '''
    return call(codes, '')

def rdate(codes, rdate):
    '''
    Query certain reported date balance sheet by codes
    Args:
        codes: stock codes, split by comma(,) eg: 100001,100002
        rdate: reported date.
    Returns
        1. no data, return ''
        2. Balance sheet dict if codes only one.
        3. Balance sheet dict list.
    '''
    return call(codes, rdate)