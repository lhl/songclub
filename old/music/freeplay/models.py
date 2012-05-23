from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

# Application Settings
class Settings(models.Model):
  updated = models.DateTimeField()
  target_type = models.CharField(maxlength=30)
  target_id = models.IntegerField()
  type = models.CharField(maxlength=30)
  attribute = models.CharField(maxlength=30)
  value = models.TextField()
  user = models.ManyToManyField(User)

  def __str__(self):
    return 'user:' + self.user + ';type:' + self.type + ';attribute:' + self.attribute + ';value:' + self.value

  class Admin:
    pass


class UserProfile(models.Model): 
  url = models.URLField() 
  openid = models.URLField() 
  bbauth = models.CharField(maxlength=200)
  avatar = models.CharField(maxlength=200)
  signup_date = models.DateTimeField()
  lastlogin = models.DateTimeField()
  lastlastlogin = models.DateTimeField()
  updated = models.DateTimeField()
  phone_numer = models.PhoneNumberField() 
  approved = models.IntegerField()
  active = models.IntegerField()
  user = models.ForeignKey(User, unique=True) 

  def __str__(self):
    return 'user:' + self.user


class UserSettings(models.Model):
  # Current Views / Filters
  # roles / permission
  # karma
  # logins, plays, total minutes, downloads 
  # yahooid, ym, aim, jabber
  # lastfm, lastfm_md5
  updated = models.DateTimeField()
  type = models.CharField(maxlength=30)
  attribute = models.CharField(maxlength=30)
  value = models.TextField()
  user = models.ManyToManyField(User)

  def __str__(self):
    return 'user:' + self.user + ';type:' + self.type + ';attribute:' + self.attribute + ';value:' + self.value


class History(models.Model):
  updated = models.DateTimeField()
  type = models.CharField(maxlength=30) # login / browse / play / download
  target_type = models.CharField(maxlength=30) # track / album
  target_id = models.IntegerField()
  user  = models.ManyToManyField(User)
  desc = models.TextField()

  def __str__(self):
    return 'user:' + self.user + ';type:' + self.type + ';desc:' + self.desc


class Token(models.Model):
  updated = models.DateTimeField()
  type = models.CharField(maxlength=30)
  expiration_date = models.DateTimeField()
  access_count = models.IntegerField()
  access_max = models.IntegerField()
  max_concurrent = models.IntegerField()
  target_type = models.CharField(maxlength=30) # track / album
  target_id = models.IntegerField()
  active = models.IntegerField()
  user  = models.ManyToManyField(User)
  
  def __str__(self):
    return 'user:' + self.user + ';type:' + self.type + ';updated:' + self.updated

  class Admin:
    pass


class Connection(models.Model):
  updated = models.DateTimeField()
  type = models.CharField(maxlength=30)
  attribute = models.CharField(maxlength=30)
  value = models.TextField()
  active = models.IntegerField()
  user = models.ManyToManyField(User)

  def __str__(self):
    return 'user:' + self.user + ';type:' + self.type + ';updated:' + self.updated

  class Admin:
    pass


class Note(models.Model):
  updated = models.DateTimeField()
  type = models.CharField(maxlength=30)
  origin_type = models.CharField(maxlength=30)
  origin_id = models.IntegerField()
  target_type = models.CharField(maxlength=30)
  target_id = models.IntegerField()
  user  = models.ManyToManyField(User)
  message = models.TextField()
  status = models.IntegerField() # Hiding Messages

  def __str__(self):
    return 'user:' + self.user + ';type:' + self.type + ';message:' + self.message

  class Admin:
    pass


class File(models.Model):
  updated = models.DateTimeField()
  entered = models.DateTimeField()
  type = models.CharField(maxlength=30)
  inode = models.IntegerField()
  mtime = models.IntegerField()
  atime = models.IntegerField()
  ctime = models.IntegerField()
  size = models.IntegerField()
  fullpath = models.TextField()
  dirname = models.TextField()
  filename = models.TextField()
  extension = models.CharField(maxlength=30)
  md5 = models.CharField(maxlength=200)
  md5_dir = models.CharField(maxlength=200)
  md5_fullpath = models.CharField(maxlength=200)
  status = models.IntegerField()
  user = models.ManyToManyField(User)

  # how to handle remote pointers?  Using URL? syncing...

  title = models.TextField()
  artist = models.TextField()
  album = models.TextField()
  year = models.IntegerField()
  volume = models.IntegerField()
  track = models.IntegerField()
  total = models.IntegerField()
  order = models.IntegerField()
  format =  models.CharField(maxlength=30)
  sample_rate = models.IntegerField()
  channel_mode = models.CharField(maxlength=30)
  bitrate = models.FloatField(max_digits=10, decimal_places=10)
  bitrate_mode =  models.CharField(maxlength=30)
  code = models.CharField(maxlength=30)
  encoder = models.CharField(maxlength=30)
  encoder_options = models.CharField(maxlength=120)
  id3 = models.TextField()

  def __str__(self):
    return 'fullpath:' + self.fullpath + ';updated:' + self.updated
  
  class Admin:
    pass

  
class Song(models.Model): 
  name = models.TextField()
  normalized = models.TextField()
  amgid = models.CharField(maxlength=120)
  ymid = models.CharField(maxlength=120)
  
  def __str__(self):
    return 'name:' + self.name + ';normalized:' + self.normalized

  
class Artist(models.Model): 
  name = models.TextField()
  normalized = models.TextField()
  amgid = models.CharField(maxlength=120)
  ymid = models.CharField(maxlength=120)
  
  def __str__(self):
    return 'name:' + self.name + ';normalized:' + self.normalized

  
class Album(models.Model):
  name = models.TextField()
  normalized = models.TextField()
  amgid = models.CharField(maxlength=120)
  ymid = models.CharField(maxlength=120)

  def __str__(self):
    return 'name:' + self.name + ';normalized:' + self.normalized

  
class MusicAttributes(models.Model):
  updated = models.DateTimeField()
  target_type = models.CharField(maxlength=30) # track / album
  target_id = models.IntegerField()
  type = models.CharField(maxlength=80)
  attribute = models.CharField(maxlength=120)
  value = models.TextField()

  def __str__(self):
    return 'type:' + self.type + ';attribute:' + self.attribute + ';value:' + self.value

  
# Tags (support machine tags)
class Tag(models.Model):
  updated = models.DateTimeField('') 
  name = models.CharField(maxlength=255)
  normalized = models.CharField(maxlength=255)
  target_type = models.CharField(maxlength=30) # track / album
  target_id = models.IntegerField()
  type = models.CharField(maxlength=30)
  attribute = models.CharField(maxlength=120)
  value = models.TextField()
  user = models.ManyToManyField(User)

  def __str__(self):
    return 'user:' + self.user + ';attribute:' + self.attribute + ';value:' + self.value
  

# Recommendations (add notes, a single recommendation can have artists)
# a type of message?
class Recommendation(models.Model):
  updated = models.DateTimeField()
  type = models.CharField(maxlength=30) # implicit / explicit, rstrength?
  origin_type = models.CharField(maxlength=30)
  origin_id = models.IntegerField()
  target_type = models.CharField(maxlength=30) # track / album
  target_id = models.IntegerField()
  desc = models.CharField(maxlength=255)
  message = models.TextField()
  status = models.IntegerField() # Hiding Messages
  user = models.ManyToManyField(User)

  def __str__(self):
    return 'user:' + self.user + ';desc:' + self.desc + ';message:' + self.message

  class Admin:
    pass


class Rating(models.Model):
  updated = models.DateTimeField()
  rating = models.IntegerField()
  desc = models.CharField(maxlength=255)
  target_type = models.CharField(maxlength=30) # track / album
  target_id = models.IntegerField()
  user = models.ManyToManyField(User)

  def __str__(self):
    return 'user:' + self.user + ';rating:' + self.rating + ';target:' + self.target_type + ':' + self.target_id


class Favorite(models.Model):
  updated = models.DateTimeField()
  type = models.CharField(maxlength=30)
  desc = models.CharField(maxlength=255)
  target_type = models.CharField(maxlength=30) # track / album
  target_id = models.IntegerField()
  privacy = models.IntegerField() # Public or Not
  user = models.ManyToManyField(User)

  def __str__(self):
    return 'user:' + self.user + ';type:' + self.type + ';target:' + self.target_type + ':' + self.target_id


class Playlist(models.Model):
  name = models.CharField(maxlength=255)
  type = models.CharField(maxlength=30)
  privacy = models.IntegerField()
  status = models.IntegerField()
  desc = models.TextField()
  user = models.ManyToManyField(User)

  def __str__(self):
    return 'user:' + self.user + ';name:' + self.name


class PlaylistItem(models.Model):
  target_type = models.CharField(maxlength=30)
  target_id = models.IntegerField()
  order = models.FloatField(max_digits=10, decimal_places=10)
  playlist = models.ForeignKey(Playlist)

  def __str__(self):
    return 'playlist:' + self.playlist + ';target:' + self.target_type + ':' + self.target_id


# class DynamicPlaylist
#   rulesets, allow caching
#   or simply extend Playlist...

# Comments - scoped to artist / song, 

# Tag comment w/ artist and song to do query
