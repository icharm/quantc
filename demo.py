# -*- coding: UTF-8 -*- 

from base import dateutils
from base import cache
from cninfo.common import TradeDate
from cninfo.common import IndustryClass
from cninfo.common import RegionClass
from cninfo.common import SecuritiesCategory

def today_is_trading_day():
    '''判断今天是否是交易日'''
    today = dateutils.current(dateutils.DF_FULL_NORMAL)
    objTradeDate = TradeDate.certain(today)
    if objTradeDate.is_trading_day:
        print('Today is trading day')
    else:
        print('Today is closed day')

# today_is_trading_day()

def sw_industry_class():
    '''打印申万行业分类信息'''
    dict = IndustryClass.sywg()
    items = dict.items()
    for key,objIndustryInfo in items:
        print(key + ' => ' + objIndustryInfo.className)

# sw_industry_class()

def all_region_info():
    '''获取所有地区分类信息'''
    dict = RegionClass.allRegionClass()
    items = dict.items()
    for key, objRegionInfo in items:
        print(key + ' => ' + objRegionInfo.regionName)

# all_region_info()

def all_securities():
    securities = SecuritiesCategory.securities()
    items = securities.items()
    for key, obj in items:
        print(key + ' => ' + obj.name)

# all_securities()