import tornado.auth
import tornado.web

from handlers.base import *

class AuthLoginHandler(BaseHandler, tornado.auth.GoogleMixin):
  @tornado.web.asynchronous
  def get(self):
    if self.get_argument('openid.mode', None):
      self.get_authenticated_user(self.async_callback(self._on_auth))
      return
    self.authenticate_redirect('/login')
                                                                                   
  def _on_auth(self, user):
    ## auth fail
    if not user:
      raise tornado.web.HTTPError(500, 'Google auth failed')

    '''
    if user.has_key('email'):
      if not re.search(r'@lensley.com$', user['email']):
        raise tornado.web.HTTPError(500, 'Must be lensley.com user')
    else:
      raise tornado.web.HTTPError(500, 'Must be lensley.com user')
    '''

    '''{'locale': u'en-us', 'first_name': u'Leonard', 'last_name': u'Lin', 'name': u'Leonard Lin', 'email': u'lhl@lensley.com'}'''
    identity = self.get_argument('openid.identity', None)
    if identity:
      mc.set(identity.encode('utf-8'), user)

    self.set_secure_cookie('identity', tornado.escape.json_encode(identity))
    self.redirect('/')
