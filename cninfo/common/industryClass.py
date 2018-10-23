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

def call(industry_type, industry_code):
    url = '/api/stock/p_public0002'
    params = {
        'indtype' : industry_type,
        'indcode' : industry_code
    }
    resp = base.call_cache(config.cache_industry, url, params)
    if resp == '':
        return ''
    resp = json.loads(resp)
    records = resp['records']
    count = resp['count']
    return D.Industry.parses(records, count) 

def industry_class(industry_type):
    ''' Get all industry class info by industryType
    
    Args:
        industryType: 行业分类标准：
            008001	证监会行业分类标准 
            008002	巨潮行业分类标准 
            008003	申银万国行业分类标准 
            008004	新财富行业分类标准 
            008005	国资委行业分类标准 
            008006	巨潮产业细分标准 
            008007	天相行业分类标准 
            008008	全球行业分类标准（GICS） 

    Returns:
        Industry info list, eg: [industry_item_dict, ...].
        See the D.Industry annotation for field details.
    '''
    return call(industry_type, '')

def sywg():
    '''Get Shen Yin Wang Guo industry class info.
    
    Returns:
        Industry info list, eg: [industry_item_dict, ...].
        See the D.Industry annotation for field details.
    '''
    return call('008003', '')



