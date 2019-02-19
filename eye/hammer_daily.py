# -*- coding: UTF-8 -*-
# Find hammer shape in daily line.
import time
import traceback
from base import log
from cninfo import cninfo
from model.quantc import SwStock
from model.quantc import HammerShape

logger = log.Log()

# Ratio of entity and line
entity_line_ratio_h = 0.5
linehead_line_ratio_h = 0.1

today_date = time.strftime('%Y-%m-%d', time.localtime())

# todo trend_before
def main():
    count = 0
    for stock in SwStock.select():
        try:
            logger.debug('Hammer analysis in stock : ' + stock.seccode + ' ' + stock.secname)
            # cninfo 的日K数据没有当天收盘的数据
            nodes = cninfo.daily_line(stock.seccode)
            # Find today node
            now = int(time.time() * 1000)
            today = None
            today_date = time.strftime('%Y-%m-%d', time.localtime())
            length = len(nodes)
            result = is_hammer_shape(nodes[length])
            # for node in nodes:
            #     datetime = time.strftime('%Y-%m-%d', time.localtime(node[0] / 1000))
            #     if datetime == today_date:
            #         today = node
            #         break
            # Determine
            # result = is_hammer_shape(today)
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
        except:
            traceback.print_exception()
            continue

def is_hammer_shape(node):
    color = 1
    if node[1] < 2:     # Open price < 2, not consider.
        return False
    datetime = time.strftime('%Y-%m-%d', time.localtime(node[0] / 1000))
    if datetime != today_date:
        return False
    line_h = round(node[3] - node[4], 2)    # Keep two decimals
    entity_h = abs(round(node[1] - node[2], 2))
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
    logger.info(str(node))
    return {
        'color': color,
        'ratio': ratio,
        'lratio': lratio
    }

def score_s(ratio, lratio):
    add = (ratio + lratio)
    if add == 0:    # Shape T super hammer.
        return 100
    return round(60 / (ratio + lratio), 2)  # 60 / max(0.6) = 100

main()