import os
import uuid
limit = 10
username = '4uuu'
email = 'i@qvq.im'
debug = False

connect_str = 'sqlite:///%s' % os.path.join(os.getcwd(), 'sshop.db3')
cookie_secret = "CISCN"+str(uuid.uuid4())
