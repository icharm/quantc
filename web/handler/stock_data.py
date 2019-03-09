# -*- coding: UTF-8 -*-
import tornado.web
import json
import time
from ...cninfo import cninfo
from ... import sina
import asyncio

class DailyLineHandler(tornado.web.RequestHandler):
    def get(self):
        code = self.get_argument("code")
        if code is None or code == '':
            self.write('')
        self.write(cninfo.daily_line(code, is_parse=False))

class QuotesHandler(tornado.web.RequestHandler):
    def get(self):
        code = self.get_argument('code')
        if code is None or code == '':
            self.write('')
        self.write(json.dumps(sina.quotes(code)))

class TestHandler(tornado.web.RequestHandler):
    async def get(self):
        query = self.get_argument('q')
        await asyncio.sleep(5)
        self.write("hello %s" % query)

