# -*- coding: UTF-8 -*-
# Stock hammer shape judge.
from ..base import log
logger = log.Log()

def is_hammer_shape(quetos):
    # Ratio of entity and line
    entity_head_line_ration = 0.4
    # entity_line_ratio_h = 0.5
    # linehead_entity_ratio_h = 0.2
    # linehead_line_ratio_h = 0.3

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
    # line head line ratio
    if color > 0:
        lhead = quetos['high'] - quetos['close']   # High - Close rise
    else:
        lhead = quetos['high'] - quetos['open']   # High - Open drop
    if lhead >= entity_h:
        return False
    lratio = round(lhead / line_h, 4)
    ratio = lratio + ratio
    if ratio > entity_head_line_ration:
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

def venus_shape_judge(q1, q2, q3):
    if q1['open'] > q1['close']:
        q1_h = q1['open']
        q1_l = q1['close']
        q1_t = -1
    else:
        q1_h = q1['close']
        q1_l = q1['open']
        q1_t = 1

    if q2['open'] > q2['close']:
        q2_h = q2['open']
        q2_l = q2['close']
        q2_t = -1
    else:
        q2_h = q2['close']
        q2_l = q2['open']
        q2_t = 1

    if q3['open'] > q3['close']:
        q3_h = q3['open']
        q3_l = q3['close']
        q3_t = -1
    else:
        q3_h = q3['close']
        q3_l = q3['open']
        q3_t = 1

    # 前天跌，昨天跌到底，今天高开高走
    if q1_l >= q2_h and q3_l >= q2_h and q2_t < 0 and q1_t > 0:
        c1 = (q1_l - q2_h) / q2['close']
        c2 = (q3_l - q2_h) / q3['open']
        return (c1 + c2) * 1000
    else:
        return False


def top(d1, d2):
    if d1 > d2:
        return d1
    else:
        return d2

def bottom(d1, d2):
    if d1 > d2:
        return d2
    else:
        return d1
