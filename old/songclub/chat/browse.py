from django.contrib import databrowse

from chat.models import *
from django.contrib.auth.models import Group

databrowse.site.register(Post)
databrowse.site.register(Group)
