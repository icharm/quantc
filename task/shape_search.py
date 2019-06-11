# -*- coding: UTF-8 -*-
# Find hammer shape in daily line.
import time
import traceback
from .shape import *
from qcinfo import D
from qcinfo import szse
from basic import log
from model import SwStock
from model import HammerShape, VenusShape

logger = log.Log()

today_date = time.strftime('%Y-%m-%d', time.localtime())

def main():
    if not szse.is_trade(today_date):
        logger.info('Today is not trading day, interrupt search.')
        return
    hammer_count = 0
    venus_count = 0
    stocks = SwStock.select()
    for stock in stocks:
        try:
            quotes = D.quotes_lately(stock.seccode)
            logger.debug('Shape analysis in stock : ' + str(stock.seccode) + ' ' + str(stock.secname))
            if hammer_shape(stock, quotes):
                hammer_count += 1
            if venus_shape(stock, quotes):
                venus_count += 1
        except:
            logger.error(traceback.format_exc())
            continue
    logger.info('Found ' + str(hammer_count) + ' hammer shape.\n' +
                'Found ' + str(venus_count) + ' venus shape.\n')

def hammer_shape(stock, quotes):
    result = is_hammer_shape(quotes)
    if not result:
        return False
    HammerShape.create(
        seccode=stock.seccode,
        secname=stock.secname,
        type='day',
        trend_before=result['trend_before'],
        color=result['color'],
        ratio=result['ratio'],
        lratio=result['lratio'],
        date=time.strftime("%Y-%m-%d", time.localtime()),
        score_s=hammer_score_s(result['ratio'], result['lratio']),
        close=quotes[-1]['close']
    )
    result['seccode'] = str(stock.seccode)
    result['secname'] = str(stock.secname)
    logger.debug('Found! : ' + str(result))
    return True

def venus_shape(stock, quotes):
    result = venus_shape_judge(quotes)
    if not result:
        return False
    VenusShape.create(
        seccode=stock.seccode,
        secname=stock.secname,
        type='day',
        trend_before=trend_before(quotes),
        color=1,
        date=quotes[-1]['date'],
        close=quotes[-1]['close'],
        score_s=result,
    )
    logger.debug('Venus found! : ' + str(stock.seccode) + ' ' + str(stock.secname))

main()