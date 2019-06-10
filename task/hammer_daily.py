# -*- coding: UTF-8 -*-
# Find hammer shape in daily line.
import time
import traceback
from .shape import is_hammer_shape, hammer_score_s
from qcinfo import sina
from qcinfo import szse
from basic import log
from model import SwStock
from model import HammerShape

logger = log.Log()

# Ratio of entity and line
entity_line_ratio_h = 0.3
linehead_entity_ratio_h = 0.15
linehead_line_ratio_h = 0.2

today_date = time.strftime('%Y-%m-%d', time.localtime())

# todo trend_before
def main():
    if not szse.is_trade(today_date):
        logger.info('Today is not trading day, interrupt search.')
        return
    target_count = 0
    count = SwStock.select().count()
    count = int(count / 100)
    for offset in range(0, count):
        stocks = SwStock.select(SwStock.seccode).limit(100).offset(offset*100)
        codes = []
        for stock in stocks:
            codes.append(stock.seccode)
        try:
            quotes_list = sina.quotes_multiple(codes)
            for code, quotes in quotes_list.items():
                logger.debug('Hammer analysis in stock : ' + quotes['code'] + ' ' + quotes['name'])
                result = is_hammer_shape(quotes)
                if not result:
                    continue
                HammerShape.create(
                    seccode=code,
                    secname=quotes['name'],
                    type='day',
                    color=result['color'],
                    ratio=result['ratio'],
                    lratio=result['lratio'],
                    date=time.strftime("%Y-%m-%d", time.localtime()),
                    score_s=hammer_score_s(result['ratio'], result['lratio']),
                    close=quotes['close']
                )
                target_count += 1
                result['seccode'] = code
                result['secname'] = quotes['name']
                logger.debug('Found! : ' + str(result))
        except:
            traceback.print_exc()
            continue
    logger.info('Found ' + str(target_count) + ' hammer shape.')

main()