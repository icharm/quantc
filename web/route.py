# -*- coding: UTF-8 -*-
"""
the url structure of website
"""
from .handler.index import IndexHandler
from .handler.hammer_shape import HammerShapeHandler
from .handler.stock_data import DailyLineHandler
from .handler.stock_data import QuotesHandler
from .handler.stock_data import TestHandler

url = [
    (r'/', IndexHandler),
    (r'/hs', HammerShapeHandler),
    (r'/sd/daily_line', DailyLineHandler),
    (r'/sd/quotes', QuotesHandler),
    (r'/sd/test', TestHandler)
]