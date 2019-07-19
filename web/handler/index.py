# -*- coding: UTF-8 -*-
import json
from .base import PeeweeRequestHandler
from model import Statistics
from playhouse.shortcuts import model_to_dict

class IndexHandler(PeeweeRequestHandler):
    def get(self):
        self.render('index.html', title='DashBoard', content='')
        # greeting = self.get_argument('greeting', 'Hello')
        # self.write(greeting + ', welcome you to read')

class ShapeStatisticsHandler(PeeweeRequestHandler):
    def get(self):
        num = self.get_argument('num')
        if num is None or num == '':
            num = 12
        data = Statistics.select(Statistics.date, Statistics.hammer_count, Statistics.venus_count, Statistics.cross_count).where(Statistics.type == 'day').limit(num)
        json_arr = [model_to_dict(t) for t in data]
        self.write(json.dumps(json_arr))