# -*- coding: UTF-8 -*-
"""
the url structure of website
"""
from .handler.index import IndexHandler
from .handler.hammer_shape import HammerShapeHandler, HammerShapeWeeklyHandler
from .handler.stock_data import DailyLineHandler, WeeklyLineHandler
from .handler.stock_data import QuotesHandler
from .handler.stock_data import TestHandler

url = [
    (r'/', IndexHandler),
    (r'/hs', HammerShapeHandler),
    (r'/hsw', HammerShapeWeeklyHandler),
    (r'/sd/daily_line', DailyLineHandler),
    (r'/sd/weekly_line', WeeklyLineHandler),
    (r'/sd/quotes', QuotesHandler),
    (r'/sd/test', TestHandler)
]