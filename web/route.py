# -*- coding: UTF-8 -*-
"""
the url structure of website
"""
from .handler.index import IndexHandler
from .handler.hammer_shape import HammerShapeHandler, HammerShapeWeeklyHandler
from .handler.venus_shape import VenusShapeHandler
from .handler.stock_data import DailyLineHandler, WeeklyLineHandler
from .handler.stock_data import QuotesHandler
from .handler.stock_data import TestHandler

url = [
    (r'/', IndexHandler),
    (r'/hs/d', HammerShapeHandler),
    (r'/hs/w', HammerShapeWeeklyHandler),
    (r'/vs/d', VenusShapeHandler),
    (r'/sd/daily_line', DailyLineHandler),
    (r'/sd/weekly_line', WeeklyLineHandler),
    (r'/sd/quotes', QuotesHandler),
    (r'/sd/test', TestHandler)
]