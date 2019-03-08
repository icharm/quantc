# -*- coding: UTF-8 -*-
from .base import PeeweeRequestHandler

class IndexHandler(PeeweeRequestHandler):
    def get(self):
        self.render('index.html', title='DashBoard', content='')
        # greeting = self.get_argument('greeting', 'Hello')
        # self.write(greeting + ', welcome you to read')