# -*- coding: UTF-8 -*- 
import http.client
import urllib
import json
from cninfo import D
from base import log
from base import base
from base import config

log = log.Log(__name__)

def call(region_id):
    url = '/api/stock/p_public0003'
    params = {
        'areaid' : region_id
    }
    resp = base.call_cache(config.cache_region, url, params)
    if resp == '':
        return ''
    resp = json.loads(resp)
    records = resp['records']
    count = resp['count']
    return D.Region.parses(records, count)

def all():
    '''Get all region classification info.
    '''
    return call('')

def certain(code):
    '''
    Get region calssification belonging to certain class

    Args:
        code: region code.
    
    Returns:
        Region info list, eg: [region1_dict, region2_dict, ...]
    '''
    return call(code)