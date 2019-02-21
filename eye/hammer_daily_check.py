# -*- coding: UTF-8 -*-
import time
import datetime
import requests
import szse
import sina
from base import log
from model.quantc import HammerShape

logger = log.Log()
fm = '%Y-%m-%d'
# today_date = time.strftime(fm, time.localtime())
today = datetime.datetime.today()
oneday = datetime.timedelta(days=1)

def main():
    t = szse.today()
    week = t['week']
    if not t['is']:
        logger.info('Today is not trading day, interrupt search.')
        return
    day_main(week)
    week_main(week)



def day_main(week):
    for i in range(1, 5):
        day(i)

def day(num):
    day = today - oneday*num
    day_str = day.strftime(fm)
    logger.info('HammerCheck day' + str(num) + '(' + day_str + ') price change range.')
    hammers = HammerShape.select().where(HammerShape.date == day_str)
    codes = []
    for hammer in hammers:
        codes.append(hammer.seccode)
    if len(codes) == 0:
        logger.info('No hammer stock need to check day'+str(num))
        return
    quotess = sina.quotes_multiple(codes)

    for hammer in hammers:
        quotes = quotess.get(hammer.seccode)
        today_close = quotes.get('close')
        rg = round((today_close - hammer.close) / hammer.close, 2)
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

def week_main(week):
    for i in range(2, 4):
        day(5*i)


def generte_days(week):
    arr = []
    for i in range(1, 5-week):
        arr.append(i)
    for i in range(1, week):
        arr.append(i+2)

main()


