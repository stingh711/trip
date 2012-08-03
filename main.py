# -*- coding: utf-8 -*-

from trip import app

#app.run()
from gevent.wsgi import WSGIServer

server = WSGIServer(('172.25.21.22', 8080), app)
server.serve_forever()
