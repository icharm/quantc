# -*- coding: UTF-8 -*-
import time
from qcinfo import D
from qcinfo import sina
from basic import log
from model import ShapeDaily

logger = log.Log()
fm = '%Y-%m-%d'
today_str = time.strftime(fm, time.localtime())

def main():
    if not D.is_trading(today_str):
        logger.info('Today is not trading day, interrupt checking.')
        return
    for i in [1, 2, 3, 4, 5, 10, 15, 20, 40, 60]:
        date = D.previous_trading_day(today_str, i)
        if date is None:
            continue
        check(date, i)

def check(date, num):
    logger.debug('checking for d' + str(num) + ', date is ' + date)
    stocks = ShapeDaily.select().where(ShapeDaily.date == date)
    codes = []
    for stock in stocks:
        codes.append(stock.seccode)
    if len(codes) == 0:
        logger.info('No shape stock need to check for d' + str(num) + ', date is ' + date)
        return
    quotess = sina.quotes_multiple(codes)

    for stock in stocks:
        quotes = quotess.get(stock.seccode)
        today_close = quotes.get('close')
        rg = round((today_close - stock.close) / stock.close * 100, 2)
        save(stock, num, rg)

def save(stock, num, rg):
    if num == 1:
        stock.d1 = rg
    elif num == 2:
        stock.d2 = rg
    elif num == 3:
        stock.d3 = rg
    elif num == 4:
        stock.d4 = rg
    elif num == 5:
        stock.d5 = rg
    elif num == 10:
        stock.d6 = rg
    elif num == 15:
        stock.d7 = rg
    elif num == 20:
        stock.d8 = rg
    elif num == 40:
        stock.d9 = rg
    elif num == 60:
        stock.d10 = rg
    stock.save()

main()