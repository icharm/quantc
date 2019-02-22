# -*- coding: UTF-8 -*-
import time
import datetime
import szse
import sina
from base import log
from model.quantc import HammerShape

logger = log.Log()
fm = '%Y-%m-%d'
today_str = time.strftime(fm, time.localtime())
today = datetime.datetime.today()
oneday = datetime.timedelta(days=1)

def main():
    if not szse.is_trade(today_str):
        logger.info('Today is not trading day, interrupt search.')
        return
    calendar = szse.calendar_2m_lately()
    length = len(calendar) - 1
    # check for day1-4 and week1
    for i in range(1, 5):
        if length >= i:
            day(calendar[length-i], i)
    # check for week2-3 and month1
    for i in range(2, 4):
        if length >= i*5:
            day(calendar[length-i*5], i*5)
    # check for month2
    # if length >= 8*5:
    #     day(calendar[length - 8 * 5], 40)


def day(calendar, num):

    # logger.info('HammerCheck day' + str(num) + '(' + day_str + ') price change range.')
    hammers = HammerShape.select().where(HammerShape.date == calendar['date'])
    codes = []
    for hammer in hammers:
        codes.append(hammer.seccode)
    if len(codes) == 0:
        logger.info('No hammer stock need to check daily')
        return
    quotess = sina.quotes_multiple(codes)

    for hammer in hammers:
        quotes = quotess.get(hammer.seccode)
        today_close = quotes.get('close')
        rg = round((today_close - hammer.close) / hammer.close * 100, 2)
        save(hammer, num, rg)

def save(hammer, num, rg):
    if num == 1:
        hammer.range_day1 = rg
    elif num == 2:
        hammer.range_day2 = rg
    elif num == 3:
        hammer.range_day3 = rg
    elif num == 4:
        hammer.range_day4 = rg
    elif num == 5:
        hammer.range_week1 = rg
    elif num == 10:
        hammer.range_week2 = rg
    elif num == 15:
        hammer.range_week3 = rg
    elif num == 20:
        hammer.range_month = rg
    hammer.save()




def generte_days(week):
    arr = []
    for i in range(1, 5-week):
        arr.append(i)
    for i in range(1, week):
        arr.append(i+2)

main()


