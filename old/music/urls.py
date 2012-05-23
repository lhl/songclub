from django.conf.urls.defaults import *

urlpatterns = patterns('',
    # Example:
    # (r'^music/', include('music.apps.foo.urls.foo')),

  (r'', 'music.freeplay.views.index'),

  # Admin
  (r'^admin/', include('django.contrib.admin.urls')),

  # OpenID
  (r'^openid/$', 'django_openidconsumer.views.begin'),
  (r'^openid/complete/$', 'django_openidconsumer.views.complete'),
  (r'^openid/signout/$', 'django_openidconsumer.views.signout'),
)


