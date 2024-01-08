from tornado.web import *
import os
from Shop import *


root_path = os.path.dirname(__file__)
handlers = [

    (r'/', ChargeHandler),
    (r'/shop', ChargeHandler),
    (r'/charge',ChargeHandler),
    (r".*", ChargeHandler)
]
