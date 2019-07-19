# -*- coding: UTF-8 -*-
"""
the url structure of website
"""
from .handler.index import IndexHandler, ShapeStatisticsHandler
from .handler.shape import ShapeDailyHandler, ShapeWeeklyHandler
from .handler.stock_data import DailyLineHandler, WeeklyLineHandler
from .handler.stock_data import QuotesHandler, CompanyInfoHandler
from .handler.stock_data import TestHandler

url = [
    (r'/', IndexHandler),
    (r"/shape/w/(\w*)", ShapeWeeklyHandler),
    (r"/shape/d/(\w*)", ShapeDailyHandler),
    (r'/sd/daily_line', DailyLineHandler),
    (r'/sd/weekly_line', WeeklyLineHandler),
    (r'/sd/quotes', QuotesHandler),
    (r'/sd/cinfo', CompanyInfoHandler),
    (r'/db/shape_statistics', ShapeStatisticsHandler),
    (r'/sd/test', TestHandler)
]