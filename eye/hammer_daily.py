# -*- coding: UTF-8 -*-
# Find hammer shape in daily line.
import time
from base import log
from cninfo import cninfo
from model.quantc import SwStock
from model.quantc import HammerShape

logger = log.Log(__name__)

# Ratio of entity and line
entity_line_ratio_h = 0.5
linehead_line_ratio_h = 0.1

# todo trend_before
def main():
    count = 0
    for stock in SwStock.select():
        logger.debug('Start finding hammer shape...')
        nodes = cninfo.daily_line(stock.seccode)
        length = len(nodes)
        result = is_hammer_shape(nodes[length - 1])
        if not result:
            continue
        HammerShape.create(
            seccode=stock.seccode,
            secname=stock.secname,
            type='day',
            color=result['color'],
            ratio=result['ratio'],
            lratio=result['lratio'],
            date=time.strftime("%Y-%m-%d", time.localtime()),
            score_s=score_s(result['ratio'], result['lratio']),
        )
        count += 1
        result['seccode'] = stock.seccode
        result['secname'] = stock.secname
        logger.debug('Found! : ' + str(result))
# todo entity_h 转正数
def is_hammer_shape(node):
    color = 1
    # Determine if the two timestamps are the same day
    now = int(time.time() * 1000)
    balance = now - int(node[0])
    # Not the same day, 864000000 is the number of milliseconds a day
    # if balance > 864000000 or balance < 0:
    #     return False
    line_h = round(node[3] - node[4], 2)    # Keep two decimals
    entity_h = round(node[1] - node[2], 2)
    # rais(1) or drop(-1)
    if entity_h > 0:    # Open - Close > 0 drop
        color = -1
    # entity line ratio
    ratio = round(entity_h / line_h, 4)
    if ratio > entity_line_ratio_h:
        return False
    # line head line ratio
    if color > 0:
        lhead = round(node[3] - node[2], 2)   # High - Close rise
    else:
        lhead = round(node[3] - node[1], 2)   # High - Open drop
    lratio = round(lhead / line_h, 4)
    if lratio > linehead_line_ratio_h:
        return False
    # is hammer shape
    return {
        'color': color,
        'ratio': ratio,
        'lratio': lratio
    }

def score_s(ratio, lratio):
    add = (ratio + lratio)
    if add == 0:
        return 99999.99
    return round(10 / (ratio + lratio), 2)

main()