# -*- coding: UTF-8 -*-
import tornado.web
from ...cninfo import cninfo

class DailyLineHandler(tornado.web.RequestHandler):
    def get(self):
        code = self.get_argument("code")
        if code is None or code == '':
            return
        self.write(cninfo.daily_line(code, is_parse=False))
