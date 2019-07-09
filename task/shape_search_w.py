# -*- coding: UTF-8 -*-
# Find hammer shape in daily line.
import time
import traceback
from .shape import *
from qcinfo import D
from basic import log
from model import SwStock
from model import ShapeWeekly, Statistics

logger = log.Log()

today_date = time.strftime('%Y-%m-%d', time.localtime())

def main():
    # if not D.islast_trading_day_week(today_date):
    #     logger.info('Today is not last trading day of week, interrupt search.')
    #     return
    hammer_count = 0
    venus_count = 0
    cross_count = 0
    stocks = SwStock.select()
    for stock in stocks:
        try:
            quotes = D.quotes(stock.seccode, type="w")
            if quotes is None:
                continue
            quotes = quotes.iloc[-50:].to_dict(orient="records")
            date = time.strftime("%Y-%m-%d", time.localtime(int(quotes[-1]["timestamp"] / 1000)))
            # if date != today_date:
            #     logger.info(stock.seccode + " recent quotes no today, is:  " + date)
            #     continue
            logger.debug('Shape analysis in stock : ' + str(stock.seccode) + ' ' + str(stock.secname))
            if hammer_shape(stock, quotes):
                hammer_count += 1
            if venus_shape(stock, quotes):
                venus_count += 1
            if cross_shape(stock, quotes):
                cross_count += 1

        except:
            logger.error(traceback.format_exc())
            continue
    Statistics.create(
        date=today_date,
        type='week',
        hammer_count=hammer_count,
        venus_count=venus_count,
        cross_count=cross_count
    )
    logger.info('Found ' + str(hammer_count) + ' hammer shape in week k line.\n' +
                'Found ' + str(venus_count) + ' venus shape in week k line.\n' +
                'Found ' + str(cross_count) + ' cross shape in week k line.\n')

def hammer_shape(stock, quotes):
    result = is_hammer_shape(quotes)
    if not result:
        return False
    save(result, stock, quotes, 'hammer')
    result['seccode'] = str(stock.seccode)
    result['secname'] = str(stock.secname)
    logger.debug('Hammer Found! : ' + str(result))
    return True

def venus_shape(stock, quotes):
    result = venus_shape_judge(quotes)
    if not result:
        return False
    save(result, stock, quotes, 'venus')
    logger.debug('Venus found! : ' + str(stock.seccode) + ' ' + str(stock.secname))
    return True

def cross_shape(stock, quotes):
    result = is_cross_shape(quotes)
    if not result:
        return False
    save(result, stock, quotes, 'cross')
    logger.debug('Cross found! : ' + str(stock.seccode) + ' ' + str(stock.secname))
    return True

def save(result, stock, quotes, type):
    ShapeWeekly.create(
        seccode=stock.seccode,
        secname=stock.secname,
        type=type,
        trend_before=result['trend_before'],
        color=result['color'],
        date=today_date,
        close=quotes[-1]['close'],
        score_s=result['score'],
    )

main()