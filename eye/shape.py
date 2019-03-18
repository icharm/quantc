# -*- coding: UTF-8 -*-
# Stock hammer shape judge.
from ..base import log
logger = log.Log()

def is_hammer_shape(quetos):
    # Ratio of entity and line
    entity_line_ratio_h = 0.3
    linehead_entity_ratio_h = 0.2
    linehead_line_ratio_h = 0.2

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

def hammer_score_s(ratio, lratio):
    add = (ratio + lratio)
    if add == 0:    # Shape T super hammer.
        return 10000
    return round(10 / (ratio + lratio), 2)