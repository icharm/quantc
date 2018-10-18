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
    parentCode = ''         # PARENTCODE 父类编码	varchar	
    classCode = ''	        # SORTCODE 类目编码	varchar	
    className = ''	        # SORTNAME 类目名称	varchar	
    classNameEn = ''   # F001V	类目名称（英文）	varchar	
                            # F002D	终止日期	DATE	
    industryCode = ''       # F003V	行业类型编码	varchar	
    industryType = ''       # F004V	行业类型	varchar

    def __init__(self, industry):
        self.parse(industry)

    def parse(self, industry):
        self.parentCode = industry['PARENTCODE']
        self.classCode = industry['SORTCODE']
        self.className = industry['SORTNAME']
        self.classNameEn = industry['F001V']
        self.industryCode = industry['F003V']
        self.industryType = industry['F004V']

def callService(industryType, industryCode):
    url = '/api/stock/p_public0002'
    params = {
        'indtype' : industryType,
        'indcode' : industryCode
    }
    respContent = base.cacheService(config.cache_industry, url, params)
    if respContent == '':
        return ''
    respContent = json.loads(respContent)
    records = respContent['records']
    recordDict = {}
    for item in records:
        obj = IndustryInfo(item)
        recordDict[obj.classCode] = obj
    return recordDict

def industryClass(industryType):
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
    return callService(industryType, '')

def swIndustryClass():
    '''Get Shen Yin Wang Guo industry class info.
    
    Returns:
        IndustryInfo object dict, eg: {classCode : objIndustryInfo, ... }
    '''
    return callService('008003', '')



