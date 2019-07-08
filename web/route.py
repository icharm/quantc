# -*- coding: UTF-8 -*-
"""
the url structure of website
"""
from .handler.index import IndexHandler
from .handler.hammer_shape import HammerShapeWeeklyHandler
from .handler.shape_daily import ShapeDailyHandler
from .handler.stock_data import DailyLineHandler, WeeklyLineHandler
from .handler.stock_data import QuotesHandler, CompanyInfoHandler
from .handler.stock_data import TestHandler

url = [
    (r'/', IndexHandler),
    (r'/hs/w', HammerShapeWeeklyHandler),
    (r"/shape/d/(\w*)", ShapeDailyHandler),
    (r'/sd/daily_line', DailyLineHandler),
    (r'/sd/weekly_line', WeeklyLineHandler),
    (r'/sd/quotes', QuotesHandler),
    (r'/sd/cinfo', CompanyInfoHandler),
    (r'/sd/test', TestHandler)
]