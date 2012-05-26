import memcache
import re
import tornado.web

class BaseHandler(tornado.web.RequestHandler):
  @property
  def db(self):
    return self.application.db

  @property
  def mc(self):
    try:
      return self._mc
    except:
      self._mc = memcache.Client(['127.0.0.1:11211'])
      return self._mc


  def initialize(self):
    self.errors = []
    self.msg = []

  def nl2br(self, text):
    _paragraph_re = re.compile(r'(?:\r\n|\r|\n){2,}')
    result = u'\n\n'.join(u'<p>%s</p>' % p.replace('\n', '<br>\n') \
      for p in _paragraph_re.split(text))
    return result


  def clear_messages(self):
    self.errors = []
    self.msg = []


  def get_current_user(self):
    identity = self.get_secure_cookie("identity")
    if not identity: return None
    self.user = self.mc.get(identity)
    return 'ok'
    # return self.db.get("SELECT * FROM authors WHERE id = %s", int(user_id))
