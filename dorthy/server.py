
import os
import logging

import tornado.ioloop
import tornado.web
import tornado.log

log = logging.getLogger('dorthy.server')

def listen(routes, port=None):
    if not port:
        try:
            port = os.environ['PORT']
        except:
            port = 8899

    app = tornado.web.Application(routes.routes)
    log.info('Starting tornado server on 127.0.0.1:%s' % port)
    app.listen(port)
    tornado.ioloop.IOLoop.instance().start()    

    

    
