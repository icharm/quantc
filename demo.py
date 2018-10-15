# -*- coding: UTF-8 -*- 

from base import dateutils
from cninfo.common import tradeDate
from cninfo.common import industryClass

def todayIsTradingDay():
    '''判断今天是否是交易日'''
    today = dateutils.currentDate(dateutils.DF_FULL_NORMAL)
    objTradeDate = tradeDate.certainDate(today)
    if objTradeDate.isTradingDay:
        print('Today is trading day')
    else:
        print('Today is closed day')

# todayIsTradingDay()

def getSwIndustryClass():
    '''打印申万行业分类信息'''
    dict = industryClass.swIndustryClass()
    items = dict.items()
    for key,objIndustryInfo in items:
        print(key + ' => ' + objIndustryInfo.className)

# getSwIndustryClass()