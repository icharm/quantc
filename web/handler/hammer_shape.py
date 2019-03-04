# -*- coding: UTF-8 -*-
import datetime
import tornado.web
from ...model.quantc import HammerShape

class HammerShapeHandler(tornado.web.RequestHandler):
    def get(self):
        date_str = self.get_argument('date', '')
        if date_str is None or date_str == '':
            today = datetime.datetime.today()
            today_str = today.strftime("%Y-%m-%d")
            if today.hour < 16: # 16 clock, the job will find new hammer today.
                yesterday = today - datetime.timedelta(days=1)
                yester_str = yesterday.strftime("%Y-%m-%d")
                date_str = yester_str
            else:
                date_str = today_str
        stocks = HammerShape.select().where(HammerShape.date == date_str)
        self.render('hammer_shape.html', stocks=stocks,)