from tornado.web import RequestHandler
from ...model import quantc

class PeeweeRequestHandler(RequestHandler):
    def prepare(self):
        quantc.db.connect()
        return super(PeeweeRequestHandler, self).prepare()

    def on_finish(self):
        if not quantc.db.is_closed():
            quantc.db.close()
        return super(PeeweeRequestHandler, self).on_finish()