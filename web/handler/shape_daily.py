# -*- coding: UTF-8 -*-
import datetime
from model import ShapeDaily
from .base import PeeweeRequestHandler

class ShapeDailyHandler(PeeweeRequestHandler):
    def get(self, type='hammer'):
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
        stocks = ShapeDaily.select().where(ShapeDaily.date == date_str, ShapeDaily.type == type).order_by(ShapeDaily.score_s.desc())
        self.render('shape_daily.html', stocks=stocks, lv2=type, lv3='daily')