# -*- coding: UTF-8 -*-
import datetime
from model import VenusShape
from .base import PeeweeRequestHandler

class VenusShapeHandler(PeeweeRequestHandler):
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
        stocks = VenusShape.select().where(VenusShape.date == date_str).order_by(VenusShape.score_s.desc())
        self.render('venus_shape.html', stocks=stocks)

# class HammerShapeWeeklyHandler(PeeweeRequestHandler):
#     def get(self):
#         date_str = self.get_argument('date', '')
#         if date_str is None or date_str == '':
#             today = datetime.datetime.today()
#             date_str = today.strftime("%Y-%m-%d")
#         stocks = HammerShapeWeek.select().where(HammerShapeWeek.date == date_str).order_by(HammerShapeWeek.score_s.desc())
#         self.render('hammer_shape_weekly.html', stocks=stocks)