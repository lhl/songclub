import tornado.autoreload
import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
  def get(self):
    self.write("root")

class RescanHandler(tornado.web.RequestHandler):
  def get(self):
    self.write("rescan")

class StartHandler(tornado.web.RequestHandler):
  def get(self):
    self.write("start")

class StopHandler(tornado.web.RequestHandler):
  def get(self):
    self.write("stop")


application = tornado.web.Application([
  (r"/", MainHandler),
  (r"/rescan", RescanHandler),
  (r"/start", StartHandler),
  (r"/stop", StopHandler),
])

if __name__ == "__main__":
  application.listen(8888)
  ioloop = tornado.ioloop.IOLoop()
  tornado.autoreload.start(ioloop)
  ioloop.start()

'''
daemonizing: http://agiletesting.blogspot.com/2009/12/deploying-tornado-in-production.html:w
http://dev.af83.com/python/daemonizing-a-tornado-app/2009/10/09

Use Supervisor?

http://stackoverflow.com/questions/4043129/giving-my-python-application-a-web-interface-to-monitor-it-using-tornado:w

'''
