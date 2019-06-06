# -*- coding: UTF-8 -*-
# Find Venus shape in daily line.
import time
import traceback
from .shape import venus_shape_judge
from qcinfo import gtimg
from qcinfo import szse
from basic import log
from quantc import SwStock
from quantc import VenusShape

logger = log.Log()

today_date = time.strftime('%Y-%m-%d', time.localtime())

def main():
    if not szse.is_trade(today_date):
        logger.info('Today is not trading day, interrupt search.')
        return
    target_count = 0
    stocks = SwStock.select()
    for stock in stocks:
        try:
            quotes_list = gtimg.daily_lately(stock.seccode)
            if quotes_list is None:
                logger.debug('Get quotes of ' + stock.seccode + " failed.")
                exit(-1)
            logger.debug('Venus analysis in stock : ' + stock.seccode + ' ' + stock.secname)
            result = venus_shape_judge(quotes_list)
            if not result:
                continue
            VenusShape.create(
                seccode=stock.seccode,
                secname=stock.secname,
                type='day',
                color=1,
                date=quotes_list[-2]['date'],
                close=quotes_list[-1]['close'],
                score_s=result,
            )
            target_count += 1
            result['seccode'] = str(stock.seccode)
            result['secname'] = str(stock.secname)
            logger.debug('Venus found! : ' + str(result))
        except:
            traceback.print_exc()
            continue
    logger.info('Found ' + str(target_count) + ' venus shape.')

main()