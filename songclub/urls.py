from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^songclub/', include('songclub.foo.urls')),


    (r'^player/$', 'songclub.player.views.index'),
    (r'^player/browse/([\d\w]{40})$', 'songclub.player.views.browse'),
    (r'^player/file/([\d\w]{40})', 'songclub.player.views.file'),


    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/(.*)', admin.site.root),
)
