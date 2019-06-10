from tornado.web import RequestHandler
import model


class PeeweeRequestHandler(RequestHandler):
    def prepare(self):
        model.db.connect()
        return super(PeeweeRequestHandler, self).prepare()

    def on_finish(self):
        if not model.db.is_closed():
            model.db.close()
        return super(PeeweeRequestHandler, self).on_finish()