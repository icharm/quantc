# -*- coding: UTF-8 -*- 
import json
from base import log
from base import base
from base import config
from base import cache

class Securities:

    parent_code = ''    # PARENTCODE	父类编码	VARCHAR	
    code = ''           # SORTCODE	类目编码	VARCHAR	
    name = ''           # SORTNAME	类目名称	VARCHAR	
    name_en = ''        # F002V	类目名称（英文）	VARCHAR	
                        # F001D	终止日期	DATE

    def __init__(self, securities):
        self.parse(securities)

    def parse(self, securities):
        self.parent_code = securities['PARENTCODE']
        self.code = securities['SORTCODE']
        self.name = securities['SORTNAME']
        self.name_en = securities['F002V']
    
def call(parent_code):
    url = '/api/public/p_public0005'
    params = {
        'subtype' : parent_code,
    }
    resp = base.call_cache(config.cache_securities, url, params)
    if resp == '':
        return ''
    resp = json.loads(resp)
    records = resp['records']
    securities = {}
    for record in records:
        obj = Securities(record)
        securities[obj.code] = obj
    return securities

def securities():
    '''Get all securities category info.
    Returns:
        1. not data, return ''
        2. Securities object dict, eg: {code:objSecurities, ...}
    '''
    return call('')

def sub_securities(parent_code):
    '''Get sub securities belong to parent_code.
    Args:
        parent_code: parent code.
    Returns:
        1. not data, then return ''
        2. Securities object dict, eg: {code:objSecurities, ...}
    '''
    return call(parent_code)
