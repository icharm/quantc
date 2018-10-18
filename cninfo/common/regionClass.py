# -*- coding: UTF-8 -*- 
import http.client
import urllib
import json
from base import log
from base import base
from base import config

log = log.Log(__name__)

class RegionInfo:
    parentCode = '' # PARENTCODE	父类编码	varchar	
    regionCode = '' # SORTCODE	地区编码	varchar	
    regionName = '' # SORTNAME	地区名称	varchar	
    regionNameEn = '' # F001V	地区名称（英文）	varchar	
                    #F002D	终止日期	date
    
    def __init__(self, region):
        self.parse(region)
    
    def parse(self, region):
        self.parentCode = region['PARENTCODE']
        self.regionCode = region['SORTCODE']
        self.regionName = region['SORTNAME']
        self.regionNameEn = region['F001V']

def callService(regionId):
    url = '/api/stock/p_public0003'
    params = {
        'areaid' : regionId
    }
    respContent = base.cacheService(config.cache_region, url, params)
    if respContent == '':
        return ''
    respContent = json.loads(respContent)
    records = respContent['records']
    dataDict = {}
    for item in records:
        obj = RegionInfo(item)
        dataDict[obj.regionCode] = obj
    return dataDict

def allRegionClass():
    '''Get all region classification info.
    '''
    return callService('')

def centainRegion(regionCode):
    '''
    Get region calssification belonging to certain class

    Args:
        regionCode: region code.
    
    Returns:
        RegionInfo object dict, eg: {regionCode: objRegionInfo, ...}

    '''
    return callService(regionCode)