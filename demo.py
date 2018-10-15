# -*- coding: UTF-8 -*- 

from base import dateutils
from cninfo.common import tradeDate

def todayIsTradingDay():
    today = dateutils.currentDate(dateutils.DF_FULL_NORMAL)
    objTradeDate = tradeDate.certainDate(today)
    if objTradeDate.isTradingDay:
        print('Today is trading day')
    else:
        print('Today is closed day')


todayIsTradingDay()
