# -*- coding: UTF-8 -*-
import tornado.web
import json
from qcinfo import D, gtimg, sina


class DailyLineHandler(tornado.web.RequestHandler):
    def get(self):
        code = self.get_argument("code")
        if code is None or code == '':
            self.write('')
        self.write(D.quotes(code, type="d").to_json(orient="values"))

class WeeklyLineHandler(tornado.web.RequestHandler):
    def get(self):
        code = self.get_argument('code')
        if code is None or code == '':
            self.write('')
        self.write(D.quotes(code, type="w").to_json(orient="values"))

class QuotesHandler(tornado.web.RequestHandler):
    async def get(self):
        code = self.get_argument('code')
        if code is None or code == '':
            self.write('')
        self.write(json.dumps(await sina.quotes_async(code)))

class CompanyInfoHandler(tornado.web.RequestHandler):
    async def get(self):
        code = self.get_argument('code')
        if code is None or code == '':
            self.write('')
        self.write(await D.company_info_async(code))

class TestHandler(tornado.web.RequestHandler):
    async def get(self):
        query = self.get_argument('q')
        lt = await gtimg.daily_lately_async(query)
        self.write("hello %s" % lt)

