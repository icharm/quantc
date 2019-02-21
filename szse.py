# -*- coding: UTF-8 -*-
import requests
import time
import json
from base import log
from model.quantc import TradeCalendar

logger = log.Log()

def trade_days():
    '''
    Request trade calendar list from Szse.cn
    :return: dict {'2019-2-1':{'is':1, 'week': '1'} ...}
            is 1 meanning trade day, week meanning the day of week.
    '''
    ym = time.strftime('%Y-%m', time.localtime())
    trade_calendar = TradeCalendar.select().where(TradeCalendar.ym == ym)
    # if datebase have, then return directly.
    if trade_calendar.count() != 0:
        return json.loads(trade_calendar.get().json)
    # request szse.cn week data is incorrect.
    url = 'http://www.szse.cn/api/report/exchange/onepersistentday/monthList'
    response = requests.get(url)
    if response.status_code != 200:
        logger.error('Get Szse trade calendar list error. ' + response.status_code)
    arr = json.loads(response.text)
    arr = arr.get('data')
    dt = {}
    for day in arr:
        tmp = {
            'is': day.get('jybz'),
            'week': day.get('zrxh')
        }
        dt[day.get('jyrq')] = tmp
    json_calendar = json.dumps(dt)
    # Create calendar.
    try:
        TradeCalendar.create(
            ym=ym,
            json=json_calendar
        )
    except:
        pass
    return dt

def is_trade(date):
    dt = trade_days()
    daydt = dt.get(date, None)
    if daydt is None:
        return False
    if daydt.get('is', 0) == 0:
        return False
    return True

def today():
    today_date = time.strftime('%Y-%m-%d', time.localtime())
    dt = trade_days()
    daydt = dt.get(today_date, None)
    if daydt is None:
        return False
    return daydt

# print(is_trade('2019-02-21'))
# trade_days()