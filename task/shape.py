# -*- coding: UTF-8 -*-
# Stock hammer shape judge.
from basic import log
logger = log.Log()

def is_hammer_shape(quotes):
    # Ratio of entity and line
    entity_head_line_ration = 0.4
    # entity_line_ratio_h = 0.5
    # linehead_entity_ratio_h = 0.2
    # linehead_line_ratio_h = 0.3

    color = 1
    if quotes[-1]['open'] < 2:     # Open price < 2, not consider.
        return False

    line_h = quotes[-1]['high'] - quotes[-1]['low']    # Keep two decimals
    entity_h = quotes[-1]['open'] - quotes[-1]['close']
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
        lhead = quotes[-1]['high'] - quotes[-1]['close']   # High - Close rise
    else:
        lhead = quotes[-1]['high'] - quotes[-1]['open']   # High - Open drop
    if lhead >= entity_h:
        return False
    lratio = round(lhead / line_h, 4)
    ratio = lratio + ratio
    if ratio > entity_head_line_ration:
        return False

    trendb= trend_before(quotes)
    # is hammer shape
    # logger.info(str(quotes))
    return {
        'trend_before': trendb,
        'color': color,
        'ratio': ratio,
        'lratio': lratio
    }

def hammer_score_s(ratio, lratio):
    add = (ratio + lratio)
    if add == 0:    # Shape T super hammer.
        return 10000
    return round(10 / (ratio + lratio), 2)

def venus_shape_judge(quotes_list):
    q1 = quotes_list[-1]
    q2 = quotes_list[-2]
    q3 = quotes_list[-3]
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

    vol2_average = ma5(quotes_list, -6, -2, "volume")
    vol3_average = ma5(quotes_list, -7, -3, "volume")

    close2_average = ma5(quotes_list, -6, -2, "close")
    close3_average = ma5(quotes_list, -7, -3, "close")
    # 前天跌，昨天跌到底，今天高开高走
    # 成交量较前五天平均值收缩
    if q1_l >= q2_h and q3_l >= q2_h and q2_t < 0 and q1_t > 0 and vol3_average > vol2_average and close3_average >= close2_average:
        c1 = (q1_l - q2_h) / q2['close']
        c2 = (q3_l - q2_h) / q3['open']
        c3 = (q1_h - q1_l) / q2['close']
        c4 = (vol3_average - vol2_average) / vol3_average
        return round((c1 + c2 + c3 + c4) * 1000, 2)
    # 前天跌，昨天低开高走，今天涨
    # 成交量较前五天平均值增加
    elif q1_l >= q2_h and q3_l >= q2_h and q2_t > 0 and q1_t > 0 and vol2_average < vol3_average and close3_average >= close2_average:
        c1 = (q1_l - q2_h) / q2['close']
        c2 = (q3_l - q2_h) / q3['open']
        c3 = (q1_h - q1_l) / q2['close']
        c4 = (vol2_average - vol3_average) / vol2_average
        return round((c1 + c2 + c3 + c4) * 1000, 2)
    else:
        return False

def ma5(quotes, sindex=-5, eindex=-1, item="close"):
    count = 0
    for i in range(sindex, eindex+1):
        count += quotes[i][item]
    return count / 5

def ma5_avg(quotes, sindex=-5, eindex=-1, item="close"):
    '''
    Pervious 5 day md5 average
    :param quotes:
    :param sindex:
    :param eindex:
    :param item:
    :return:
    '''
    count = 0
    for i in range(sindex, eindex+1):
        count += ma5(quotes, i-4, i, item)
    return count / 5

def trend_before(quotes, sindex=-1, item="close"):
    '''
    计算ma5的均线趋势，计算前5天ma5均值的平均值，与后一天收盘价比较，5%以内视为横盘
    :param quotes: 行情list
    :param startIndex:
    :param item:
    :return: 0：横盘， 1：raise， -1：drop
    '''
    avg_previous_5 = ma5_avg(quotes, sindex=sindex-5, eindex=sindex-1, item=item)
    yesterday = quotes[-1]["close"]
    if avg_previous_5 > yesterday:
        ratio = (avg_previous_5 - yesterday) / avg_previous_5
        if ratio < 0.05:
            return 0
        else:
            return -1
    else:
        ratio = (yesterday - avg_previous_5) / yesterday
        if ratio < 0.05:
            return 0
        else:
            return 1

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
