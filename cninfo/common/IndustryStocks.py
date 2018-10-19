# -*- coding: UTF-8 -*- 
import http.client
import urllib
import json
from base import log
from base import base
from base import config
from base import cache
from model import Stock

def call_industry(platetype, platecode, abtype):
    '''Query stock list belong to a certain industry classification.
    Args:
        platetype: industry type, eg：
            137001	市场分类 
            137002	证监会行业分类 
            137003	巨潮行业分类 
            137004	申银万国行业分类 
            137005	新财富行业分类 
            137006	地区省市分类 
            137007	指数成份股 
            137008	概念板块
        platecode: certain classification code.
        abtype: A: A股, B: B股
    Returns:
        1. no data, return ''
        2. Stock object dict. eg: {code:obj_Stock, ...}
    '''
    url = '/api/stock/p_public0004'
    params = {
        'platetype' : platetype,
        'platecode' : platecode,
        'abtype' : abtype
    }
    resp = base.call_cache(config.cache_stocks_class, url, params)
    if resp == '':
        return ''
    resp = json.loads(resp)
    records = resp['records']
    stocks = {}
    for record in records:
        obj = Stock.Stock(record)
        stocks[obj.code] = obj
    return stocks

def sw_industry_stocks(code):
    '''Get stocks under a certain sywg industry classification.
    Args:
        code: classification code of sywg industry.
    Returns:
        1. no data, return ''
        2. Stock object dict. eg: {code:obj_Stock, ...}
    '''
    return call_industry('137004', code, '')

def sw_industry_stocks_a(code):
    '''Get stocks of A under a certain sywg industry classification.
    Args:
        code: classification code of sywg industry.
    Returns:
        1. no data, return ''
        2. Stock object dict. eg: {code:obj_Stock, ...}
    '''
    return call_industry('137004', code, 'A')

def sw_industry_stocks_b(code):
    '''Get stocks of B under a certain sywg industry classification.
    Args:
        code: classification code of sywg industry.
    Returns:
        1. no data, return ''
        2. Stock object dict. eg: {code:obj_Stock, ...}
    '''
    return call_industry('137004', code, 'B')
