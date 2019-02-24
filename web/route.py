# -*- coding: UTF-8 -*-
"""
the url structure of website
"""

import sys

from .handler.index import IndexHandler    #假设已经有了

url = [
    (r'/', IndexHandler),
]