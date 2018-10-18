# -*- coding: UTF-8 -*- 
import http.client
import urllib
import json
from base import log
from base import base
from base import config
from base import cache

log = log.Log(__name__)

class IndustryInfo:
    parent_code = ''         # PARENTCODE 父类编码	varchar	
    class_code = ''	        # SORTCODE 类目编码	varchar	
    class_name = ''	        # SORTNAME 类目名称	varchar	
    class_name_en = ''   # F001V	类目名称（英文）	varchar	
                            # F002D	终止日期	DATE	
    industry_code = ''       # F003V	行业类型编码	varchar	
    industry_type = ''       # F004V	行业类型	varchar

    def __init__(self, industry):
        self.parse(industry)

    def parse(self, industry):
        self.parent_code = industry['PARENTCODE']
        self.class_code = industry['SORTCODE']
        self.class_name = industry['SORTNAME']
        self.class_name_en = industry['F001V']
        self.industry_code = industry['F003V']
        self.industry_type = industry['F004V']

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
    industries = {}
    for item in records:
        obj = IndustryInfo(item)
        industries[obj.class_code] = obj
    return industries

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
        IndustryInfo object dict, eg: {classCode : objIndustryInfo, ... }
    '''
    return call(industry_type, '')

def sywg():
    '''Get Shen Yin Wang Guo industry class info.
    
    Returns:
        IndustryInfo object dict, eg: {classCode : objIndustryInfo, ... }
    '''
    return call('008003', '')



