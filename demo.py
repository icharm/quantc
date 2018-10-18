# -*- coding: UTF-8 -*- 

from base import dateutils
from base import cache
from cninfo.common import tradeDate
from cninfo.common import industryClass
from cninfo.common import regionClass

def today_is_trading_day():
    '''判断今天是否是交易日'''
    today = dateutils.current(dateutils.DF_FULL_NORMAL)
    objTradeDate = tradeDate.certain(today)
    if objTradeDate.is_trading_day:
        print('Today is trading day')
    else:
        print('Today is closed day')

today_is_trading_day()

def get_sw_industry_class():
    '''打印申万行业分类信息'''
    dict = industryClass.sywg()
    items = dict.items()
    for key,objIndustryInfo in items:
        print(key + ' => ' + objIndustryInfo.className)

# get_sw_industry_class()

def get_all_region_info():
    '''获取所有地区分类信息'''
    dict = regionClass.allRegionClass()
    items = dict.items()
    for key, objRegionInfo in items:
        print(key + ' => ' + objRegionInfo.regionName)

# get_all_region_info()
