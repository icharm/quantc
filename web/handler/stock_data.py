# -*- coding: UTF-8 -*-
import tornado.web
import json
import cninfo
from ... import sina
from ... import gtimg

class DailyLineHandler(tornado.web.RequestHandler):
    async def get(self):
        code = self.get_argument("code")
        if code is None or code == '':
            self.write('')
        self.write(await cninfo.daily_async(code, is_parse=False))

class WeeklyLineHandler(tornado.web.RequestHandler):
    async def get(self):
        code = self.get_argument('code')
        if code is None or code == '':
            self.write('')
        ls = await gtimg.weekly_async(code, retformat='list', timeformat='int')
        self.write({'nodes': ls, 'responseCode': 200})

class QuotesHandler(tornado.web.RequestHandler):
    async def get(self):
        code = self.get_argument('code')
        if code is None or code == '':
            self.write('')
        self.write(json.dumps(await sina.quotes_async(code)))

class TestHandler(tornado.web.RequestHandler):
    async def get(self):
        query = self.get_argument('q')
        lt = await gtimg.daily_lately_async(query)
        self.write("hello %s" % lt)

