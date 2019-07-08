# -*- coding: UTF-8 -*-
import datetime
from model import HammerShape, HammerShapeWeek
from .base import PeeweeRequestHandler

class HammerShapeWeeklyHandler(PeeweeRequestHandler):
    def get(self):
        date_str = self.get_argument('date', '')
        if date_str is None or date_str == '':
            today = datetime.datetime.today()
            date_str = today.strftime("%Y-%m-%d")
        stocks = HammerShapeWeek.select().where(HammerShapeWeek.date == date_str).order_by(HammerShapeWeek.score_s.desc())
        self.render('hammer_shape_weekly.html', stocks=stocks)