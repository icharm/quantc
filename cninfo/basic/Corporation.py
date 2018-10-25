# -*- coding: UTF-8 -*- 
import http.client
import urllib
import json
from cninfo import D
from base import log
from base import base
from base import config
from base import cache

log = log.Log(__name__)

def call(codes):
    '''
    Query corporation info by stock code, mulitple codes use comma(,) to split.
    Args:
        codes: stock code, eg: 100001 or 100001,100002,...
    Returns:
        1. no data, return ''
        2. one record, return Corporation dict.
        3. mulitple record, return list.
        See the D.Corporation annotation for field details.
    '''
    url = '/api/stock/p_stock2100'
    params = {
        'scode' : codes,
    }
    resp = base.call(url, params)
    if resp == '':
        return ''
    resp = json.loads(resp)
    records = resp['records']
    count = resp['count']
    return D.Corporation.parses(records, count) 
