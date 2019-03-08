# -*- coding: UTF-8 -*-
import time
import datetime
import requests
import json
from .base import log
from .model.quantc import TradeCalendar

logger = log.Log()

month = time.strftime('%Y-%m', time.localtime())

logger = log.Log()

def calendar_request():
    '''
    Request szse.cn for calendar this month.
    :return:
    '''
    url = 'http://www.szse.cn/api/report/exchange/onepersistentday/monthList'
    response = requests.get(url)
    if response.status_code != 200:
        logger.error('Get Szse trade calendar list error. ' + response.status_code)
    arr = json.loads(response.text)
    arr = arr.get('data')
    dt = {}
    for day in arr:
        tmp = {
            'open': int(day.get('jybz')),
            'date': day.get('jyrq'),
            'weekday': day.get('zrxh') - 1
        }
        dt[day.get('jyrq')] = tmp
    return dt

def calendar(tm=None, open=False):
    '''
    Trade calendar this month.
    :param tm: 2019-01, target
    :param open:
    :return: dict {
                '2019-2-1':{
                    'open':1,
                    'weekday': 1
                    }
                    ...
                }
            open 1: is a trade day, weekday: the day of week.
    '''

    if tm is not None:
        trade_calendar = TradeCalendar.select().where(TradeCalendar.month == tm)
    else:
        trade_calendar = TradeCalendar.select().where(TradeCalendar.month == month)
    # if datebase have, then return directly.

    if trade_calendar.count() != 0:
        calender_dt = json.loads(trade_calendar.get().calendar)
        if open:
            return remove_close_days(calender_dt)
        return calender_dt

    # The date is not this month and database dont have calendar, then return None.
    if tm != month:
        logger.error('No calendar for date: ' + tm)
        return None

    # Request szse.cn for this month.
    dt = calendar_request()

    # Save into database.
    json_calendar = json.dumps(dt)
    try:
        TradeCalendar.create(
            month=month,
            calendar=json_calendar
        )
    except:
        pass
    if open:
        dt = remove_close_days(dt)
    return dt

def remove_close_days(dt):
    newdt = {}
    for date, day in dt.items():
        if day['open'] == 1:
            newdt[date] = day
    return newdt

def is_trade(date):
    '''
    Target date is a trading day?
    :param date: '2019-01-01'
    :return: True: yes, False: no
    '''

    dt = calendar(date[:-3])
    if dt is None:  # No calendar data, return False.
        return False
    daydt = dt.get(date, None)
    if daydt is None:
        return False
    if daydt.get('open', 0) == 0:
        return False
    return True

def calendar_2m_lately():
    '''
    Two months calendar item list.
    :return: list
    '''
    today = datetime.datetime.today()
    first_day = today.replace(day=1)
    last_month_end_day = first_day - datetime.timedelta(days=1)
    last_month_first_day = last_month_end_day.replace(day=1)
    last_2month_end_day = last_month_first_day - datetime.timedelta(days=1)
    last_month = last_month_end_day.strftime('%Y-%m')
    last_2month = last_2month_end_day.strftime('%Y-%m')
    month1 = calendar(tm=last_2month, open=True)
    month2 = calendar(tm=last_month, open=True)
    thismonth = calendar(tm=month, open=True)

    today_str = today.strftime('%Y-%m-%d')
    arr = []
    if month1 != None:
        for date, day in month1.items():
            arr.append(day)
    if month2 != None:
        for date, day in month2.items():
            arr.append(day)
    for date, day in thismonth.items():
        arr.append(day)
        if date == today_str:
            break
    return arr

# print(calendar_2m_lately())
