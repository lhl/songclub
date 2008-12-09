from django.conf.urls.defaults import *
from django.contrib.auth.decorators import login_required

import browse
from django.contrib import databrowse

from django.views.generic.simple import direct_to_template

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name':'login.html'}),
    # Example:
    # (r'^django_chat/', include('django_chat.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^browse/(.*)', login_required(databrowse.site.root)),

    # Uncomment the next line to enable the admin:
    (r'^admin/(.*)', admin.site.root),
    (r'^$', login_required(direct_to_template), {'template':'chat_dojo.html'}),
    (r'^update/$', 'django_chat.chat.views.update'),
    (r'^post/$', 'django_chat.chat.views.post'),
    (r'^testpost/$', 'django_chat.chat.views.testpost'),
    # no ajax
    (r'^noajax$', 'django_chat.chat.views.noajax', {'template':'chat.html'}),
)
