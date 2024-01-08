import os

import tornado.web

import views
from settings import debug, cookie_secret


class Application(tornado.web.Application):
    def __init__(self):
        self.root_path = os.path.dirname(__file__)

        handlers = views.handlers
        settings = dict(
            static_path=os.path.join(self.root_path, 'template/assets'),
            template_path=os.path.join(self.root_path, 'template'),
            cookie_secret=cookie_secret,
            debug=True,
            xsrf_cookies=False
        )
        super(Application, self).__init__(handlers, **settings)
