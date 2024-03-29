import os

# import tornado libraries
import tornado.httpserver
import tornado.ioloop
import tornado.web
from tornado.options import define, options

# import handlers
from app.load_balancer_handler import LoadBalancerHandler
from app.status_handlers import StatusHandler, MissingHandler, DenyHandler

# import controllers
from app.controllers.ImagizeGenerator import ImagizeGenerator

# Import our library
from lib.config_wrapper import ConfigWrapper
from lib.json_encoder import JSONEncoder
from lib.log_wrapper import LogWrapper
from lib.db_wrapper import Database

define("config", type=str, default=None)
define("port", default=9005, type=int)
define("processes", default=1, type=int)

settings = {
    'debug': False,
    'template_path': os.path.join(os.path.dirname(__file__), "public"),
    'favicon_path': os.path.join(os.path.dirname(__file__), "public/img"),
    'robots_path': os.path.join(os.path.dirname(__file__), "public/templates"),
    'static_path': os.path.join(os.path.dirname(__file__), "static"),
    'autoreload': True,
    'compress_response': True,
}

applicationDeny = tornado.web.Application([
    (r"/v1/imagize", ImagizeGenerator),

    (r"/v1/static/(.*)", tornado.web.StaticFileHandler, dict(path=settings['static_path'])),
    (r"/v1/public/(.*)", tornado.web.StaticFileHandler, dict(path=settings['template_path'])),
    (r"/statuscheck", StatusHandler),
    (r"/f5", LoadBalancerHandler),
    (r"/v1/(favicon\.ico)", tornado.web.StaticFileHandler, dict(path=settings['favicon_path'])),
    (r"/v1/(robots\.txt)", tornado.web.StaticFileHandler, dict(path=settings['robots_path'])),
    (r"/v1/", DenyHandler),
    (r'.*', MissingHandler)
], settings)

applicationAllow = tornado.web.Application([
    (r"/v1/imagize", ImagizeGenerator),

    (r"/v1/static/(.*)", tornado.web.StaticFileHandler, dict(path=settings['static_path'])),
    (r"/v1/public/(.*)", tornado.web.StaticFileHandler, dict(path=settings['template_path'])),
    (r"/statuscheck", StatusHandler),
    (r"/f5", LoadBalancerHandler),
    (r"/v1/(favicon\.ico)", tornado.web.StaticFileHandler, dict(path=settings['favicon_path'])),
    (r"/v1/(robots\.txt)", tornado.web.StaticFileHandler, dict(path=settings['robots_path'])),
    (r"/v1/", DenyHandler),
    (r'.*', MissingHandler)
], settings)


if __name__ == "__main__":
    tornado.options.parse_command_line()

    config = ConfigWrapper()
    settings = {}
    if options.config:
        settings = config.load_config(options.config, "config")

    if options.port:
        settings['port'] = options.port

    # Load our logging module
    log_instance = LogWrapper(config=settings)
    logger = log_instance.myLogger()

    # db instance
    db = Database(config=settings)

    logger.info("> Tornado Server Started with the Following Configs:")
    logger.info("> Config File ==> " + str(options.config))
    logger.info("> Port ==> " + str(options.port))
    logger.info("> Config Settings ==> " + str(settings))

    if settings['environment'] in ['PRODUCTION', 'STAGING']:
        logger.info("> Loaded ==> Deny application")
        server = tornado.httpserver.HTTPServer(applicationDeny)
    else:
        logger.info("> Loaded ==> Allow application")
        server = tornado.httpserver.HTTPServer(applicationAllow)

    server.bind(options.port)
    server.start(options.processes)

    tornado.ioloop.IOLoop.instance().start()