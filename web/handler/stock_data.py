# -*- coding: UTF-8 -*-
import tornado.web
import json
from ...cninfo import cninfo
from ... import sina

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

