import datetime
from songclub.player.models import File
from django.contrib import admin

class FileAdmin(admin.ModelAdmin):
  list_display = ('location', 'type')
  # list_filter = ['getDateTime']

admin.site.register(File, FileAdmin)

