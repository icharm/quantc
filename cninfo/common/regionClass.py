# -*- coding: UTF-8 -*- 
import http.client
import urllib
import json
from base import log
from base import base
from base import config

log = log.Log(__name__)

class RegionInfo:
    parent_code = '' # PARENTCODE	父类编码	varchar	
    region_code = '' # SORTCODE	地区编码	varchar	
    region_name = '' # SORTNAME	地区名称	varchar	
    region_name_en = '' # F001V	地区名称（英文）	varchar	
                    #F002D	终止日期	date
    
    def __init__(self, region):
        self.parse(region)
    
    def parse(self, region):
        self.parent_code = region['PARENTCODE']
        self.region_code = region['SORTCODE']
        self.region_name = region['SORTNAME']
        self.region_name_en = region['F001V']

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
    regions = {}
    for item in records:
        obj = RegionInfo(item)
        regions[obj.region_code] = obj
    return regions

def allRegionClass():
    '''Get all region classification info.
    '''
    return call('')

def centainRegion(region_code):
    '''
    Get region calssification belonging to certain class

    Args:
        regionCode: region code.
    
    Returns:
        RegionInfo object dict, eg: {regionCode: objRegionInfo, ...}

    '''
    return call(region_code)