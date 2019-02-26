# -*- coding: UTF-8 -*-
import tornado.web

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html', title='DashBoard', content='')
        # greeting = self.get_argument('greeting', 'Hello')
        # self.write(greeting + ', welcome you to read')