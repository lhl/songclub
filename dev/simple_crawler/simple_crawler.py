#!/usr/bin/python

import os
from os.path import join, getsize
import ConfigParser
import json
from pyechonest import artist 
from pyechonest import config
from pyechonest import song
import redis
import subprocess
from   urlparse import urlparse
    

# Globals
search_root_dir = '/Users/gabe/code/songclub/dev/test_music'


def main():
  redis_client = redis.Redis(host='localhost', port=6379, db=0)

  for root, dirs, files in os.walk(search_root_dir):
    for name in files:
      full_path = os.path.join(root, name)
      ext = os.path.splitext(name)[1]
      if ext.lower() == '.mp3':
        print full_path
        ingest_file('file://' + full_path)


# Redis sequences
def next_id(sequence_name):
  return redis_client.hincrby('sequences', sequence_name)


# Reading Configs
cfg = ConfigParser.ConfigParser()
cfg.read('.config')
api_key = cfg.get('APIKeys', 'api_key')
config.ECHO_NEST_API_KEY=api_key


# DB
redis_client = redis.Redis(host='localhost', port=6379, db=0)


# Get the ENMFP from an MP3
def get_enmfp_json_from_mp3(url):
  enmfp_codegen_path = cfg.get('Tools', 'enmfp_codegen')
  file_path = urlparse(url).path
  json_str = subprocess.check_output([enmfp_codegen_path, file_path, '10', '10']).decode('utf-8')
  result = json.loads(json_str)[0]
  return result['code']



# Cache EN info for each song
def store_en_info(enmfp, url):
  u = urlparse(url)
  s = song.identify(code=enmfp)[0] #TODO deal with more than one match
  a = artist.Artist(id=s.artist_id)

  #TODO find out if we can get release info too
  redis_client.set('en_songs:%s' % s.id, json.dumps(s.__dict__))
  redis_client.set('en_artists:%s' % a.id, json.dumps(a.__dict__))
  redis_client.set('en_enmfp_by_path:%s' % u.path, enmfp)
  redis_client.set('en_song_ids_by_enmfp:%s' % enmfp, s.id)

  # Only lookup/store artist terms if we dont have yet
  key = 'en_artist_terms:%s' % a.id
  if not redis_client.get(key):
    redis_client.set(key, json.dumps(a.terms))

  return {'song': s, 'artist': a}



# Store file info in redis
def ingest_file(url):
  enmfp = get_enmfp_json_from_mp3(url)
  en_info = store_en_info(enmfp, url)

  file = {
    'enmfp': enmfp,
    'url'  : url,
    'id'   : next_id('files'),
    'en_artist_id' : en_info['artist'].id,
    'en_song_id' : en_info['song'].id,
  }

  redis_client.set('files:%s' % file['id'], json.dumps(file))

  return 'OK'




if __name__ == "__main__":
  main()
