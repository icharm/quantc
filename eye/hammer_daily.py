# -*- coding: UTF-8 -*-
# Find hammer shape in daily line.
import time
import traceback
from .. import sina
from .. import szse
from ..base import log
from ..model.quantc import SwStock
from ..model.quantc import HammerShape

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
                    score_s=score_s(result['ratio'], result['lratio']),
                    close=quotes['close']
                )
                target_count += 1
                result['seccode'] = code
                result['secname'] = quotes['name']
                logger.debug('Found! : ' + str(result))
        except:
            traceback.print_exception()
            continue
    logger.info('Found ' + str(target_count) + ' hammer shape.')

def is_hammer_shape(quetos):
    color = 1
    if quetos['open'] < 2:     # Open price < 2, not consider.
        return False

    line_h = quetos['high'] - quetos['low']    # Keep two decimals
    entity_h = quetos['open'] - quetos['close']
    if line_h <= 0:
        return False
    # rais(1) or drop(-1)
    if entity_h > 0:    # Open - Close > 0 drop
        color = -1
    entity_h = abs(entity_h)
    # entity line ratio
    ratio = round(entity_h / line_h, 4)
    if ratio > entity_line_ratio_h:
        return False
    # line head line ratio
    if color > 0:
        lhead = quetos['high'] - quetos['close']   # High - Close rise
    else:
        lhead = quetos['high'] - quetos['open']   # High - Open drop
    if entity_h == 0:
        lratio = round(lhead / line_h, 4)
    else:
        lratio = round(lhead / entity_h, 4)
    if lratio > linehead_entity_ratio_h:
        return False
    # is hammer shape
    logger.info(str(quetos))
    return {
        'color': color,
        'ratio': ratio,
        'lratio': lratio
    }

def score_s(ratio, lratio):
    add = (ratio + lratio)
    if add == 0:    # Shape T super hammer.
        return 10000
    return round(10 / (ratio + lratio), 2)

main()