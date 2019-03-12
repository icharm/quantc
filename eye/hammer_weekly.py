# -*- coding: UTF-8 -*-
# Find hammer shape in weekly line.
import time
import traceback
from .shape import is_hammer_shape, hammer_score_s
from .. import gtimg
from .. import szse
from ..base import log
from ..model.quantc import SwStock
from ..model.quantc import HammerShapeWeek

logger = log.Log()

today_date = time.strftime('%Y-%m-%d', time.localtime())
weekday = time.strftime('%a', time.localtime())

# todo trend_before
def main():
    if not szse.is_trade(today_date):
        logger.info('Today is not trading day, interrupt search.')
        return
    if weekday != 'Fri':
        logger.info('Today is not friday, interrupt search.')
    target_count = 0
    stocks = SwStock.select(SwStock.seccode, SwStock.secname)
    for stock in stocks:
        quotes = gtimg.weekly_lately(stock.seccode)[-1]
        if quotes is None:
            continue
        try:
            logger.debug('Hammer analysis in stock : ' + stock.seccode + ' ' + stock.secname)
            result = is_hammer_shape(quotes)
            if not result:
                continue
            HammerShapeWeek.create(
                seccode=stock.seccode,
                secname=stock.secname,
                type='week',
                color=result['color'],
                ratio=result['ratio'],
                lratio=result['lratio'],
                date=time.strftime("%Y-%m-%d", time.localtime()),
                score_s=hammer_score_s(result['ratio'], result['lratio']),
                close=quotes['close']
            )
            target_count += 1
            result['seccode'] = stock.seccode
            result['secname'] = stock.secname
            logger.debug('Found! : ' + str(result))
        except:
            traceback.print_exc()
            continue
    logger.info('Found ' + str(target_count) + ' weekly hammer shape.')


main()
