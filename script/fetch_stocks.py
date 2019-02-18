# -*- coding: UTF-8 -*-
# Fetch stocks according to sw category.

from base import log
from cninfo import cninfo
from model.quantc import SwStock

logger = log.Log(__name__)

category_dt = cninfo.categorys('S')
if category_dt == None:
    exit()
for item in category_dt['children']:
    stocks_dt = cninfo.stocks_under_category(item['PARAM'], item['API'])
    if stocks_dt == None:
        continue
    for stock in stocks_dt:
        logger.debug(str(stock))
        SwStock.create(
            seccode=stock['SECCODE'],
            secname=stock['SECNAME'],
            startdate=stock['STARTDATE'],
            sw1=stock['F009V'] if stock['F009V']!=None else '',
            sw2=stock['F010V'] if stock['F010V']!=None else '',
            sw3=stock['F011V'] if stock['F011V']!=None else '',
            sw=(stock['F004V'] if stock['F004V']!=None else '') + '-' + (stock['F005V'] if stock['F005V']!=None else '') + '-' + (stock['F006V'] if stock['F006V']!=None else '')
        )






