# -*- coding: UTF-8 -*-
"""
the url structure of website
"""

import sys

from .handler.index import IndexHandler    #假设已经有了
from .handler.hammer_shape import HammerShapeHandler
from .handler.stock_data import DailyLineHandler

url = [
    (r'/', IndexHandler),
    (r'/hs', HammerShapeHandler),
    (r'/sd/daily_line', DailyLineHandler)
]