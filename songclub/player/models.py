# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

import datetime
from django.db import models

class EpochDateField(models.DateTimeField):
  # http://blog.elsdoerfer.name/2008/01/08/fuzzydates-or-one-django-model-field-multiple-database-columns/

  def contribute_to_class(self, cls, name):  
    precision_field = models.IntegerField(null=True, blank=True)  
    # cls.add_to_class(_precision_field_name(name), precision_field)  

  # def get_db_prep_save()

class File(models.Model):
    id = models.IntegerField(primary_key=True)
    locationsha1 = models.CharField(unique=True, max_length=120)
    location = models.CharField(max_length=15000)
    path = models.CharField(max_length=12000)
    name = models.CharField(max_length=3000)
    proto = models.CharField(max_length=60)
    type = models.CharField(max_length=120, blank=True)
    mimetype = models.CharField(max_length=600, blank=True)
    magic = models.CharField(max_length=6000, blank=True)
    owner = models.CharField(max_length=240)
    filecount = models.IntegerField(null=True, blank=True)
    mp3count = models.IntegerField(null=True, blank=True)
    filelist = models.TextField(blank=True)
    ext = models.CharField(max_length=240, blank=True)
    mp3 = models.TextField(blank=True)
    mtime = models.IntegerField(null=True, blank=True)
    size = models.IntegerField(null=True, blank=True)
    sha1 = models.CharField(max_length=120, blank=True)

    def __unicode__(self):
      return self.location

    def getModifiedDateTime(self):
      return datetime.datetime.fromtimestamp(self.mtime)

    def getRecentlyAddedFolders(self, hasmp3s=1):
      pass

    def getTracksInFolder(self, folder):
      # tracks should have location 
      pass

    class Meta:
        db_table = u'file'

