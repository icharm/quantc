# -*- coding: UTF-8 -*-
from .route import url

import tornado.web
import os

settings = dict(
    static_path=os.path.join(os.path.dirname(__file__), "static"),
    template_path=os.path.join(os.path.dirname(__file__), "template")
    )

application = tornado.web.Application(
    handlers=url,
    **settings
)