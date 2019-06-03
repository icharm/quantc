# -*- coding: UTF-8 -*-
# Find Venus shape in daily line.
import time
import traceback
from .shape import venus_shape_judge
from .. import gtimg
from .. import szse
from ..base import log
from ..model.quantc import SwStock
from ..model.quantc import VenusShape

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
            q1 = quotes_list[-1]
            q2 = quotes_list[-2]
            q3 = quotes_list[-3]
            logger.debug('Venus analysis in stock : ' + stock.seccode + ' ' + stock.secname)
            result = venus_shape_judge(q1, q2, q3)
            if not result:
                continue
            VenusShape.create(
                seccode=stock.seccode,
                secname=stock.secname,
                type='day',
                color=1,
                date=q2['date'],
                close=q3['close'],
                score_s=result,
            )
            target_count += 1
            result['seccode'] = [stock.seccode]
            result['secname'] = [stock.secname]
            logger.debug('Venus found! : ' + str(result))
        except:
            traceback.print_exc()
            continue
    logger.info('Found ' + str(target_count) + ' venus shape.')

main()