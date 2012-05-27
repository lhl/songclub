import tornado.gen
import tornado.httpclient
import tornado.web

from handlers.base import *


class SearchHandler(BaseHandler):
  # @tornado.web.authenticated
  @tornado.web.asynchronous
  @tornado.gen.engine
  def get(self, search):
    http_client = tornado.httpclient.AsyncHTTPClient()
    response = yield tornado.gen.Task(http_client.fetch, "http://localhost:9200/%s" % search)
    self.set_header("Content-Type", "application/json; charset=UTF-8")
    self.write(response.body)
    self.finish()
