#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from django.contrib import admin
from models import *
from django.contrib.auth.admin import UserAdmin

class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'date'
    list_display=('date','user', 'summary',)
    list_filter = ('user',)
admin.site.register(Post, PostAdmin)


admin.site.unregister(User)
class UserDataInline(admin.StackedInline):
    model = UserData
    max_num = 1

class ChatUserAdmin(UserAdmin):
    inlines = [UserDataInline]
admin.site.register(User, ChatUserAdmin)
