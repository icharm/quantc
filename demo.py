# -*- coding: UTF-8 -*- 

from base import dateutils
from base import cache
from cninfo.common import TradeDate
from cninfo.common import IndustryClass
from cninfo.common import RegionClass
from cninfo.common import SecuritiesCategory
from cninfo.common import IndustryStocks

def today_is_trading_day():
    '''判断今天是否是交易日'''
    today = dateutils.current(dateutils.DF_FULL_NORMAL)
    day = TradeDate.certain(today)
    if day['is_trading_day']:
        print('Today is trading day')
    else:
        print('Today is closed day')

today_is_trading_day()

def sw_industry_class():
    '''打印申万行业分类信息'''
    ls = IndustryClass.sywg()
    for dt in ls:
        print(dt['code'] + ' => ' + dt['name'])

# sw_industry_class()

def all_region_info():
    '''获取所有地区分类信息'''
    regions = RegionClass.all()
    for region in regions:
        print(region['code'] + ' => ' + region['name'])

# all_region_info()

def all_securities():
    ''' 获取所有证券分类信息'''
    securities = SecuritiesCategory.securities()
    items = securities.items()
    for key, obj in items:
        print(key + ' => ' + obj.name)

# all_securities()

# def stocks_certain_industry():
#     '''获取申万调味乳制品分类下股票列表'''
#     stocks = IndustryStocks.sw_industry_stocks('S340402')
#     if stocks != '':
#         items = stocks.items()
#         for key, obj in items:
#                 print(key + ' => ' + obj.name)

# stocks_certain_industry()