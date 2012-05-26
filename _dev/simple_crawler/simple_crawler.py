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
import elastic_songs
import hashlib
import id3

# Globals
search_root_dir = '/Users/gabe/code/songclub/_dev/test_music'
redis_client = redis.Redis(host='localhost', port=6379, db=0)


def main():
  # ingest all files
  for root, dirs, files in os.walk(search_root_dir):
    for name in files:
      full_path = os.path.join(root, name)
      ext = os.path.splitext(name)[1]
      if ext.lower() == '.mp3':
        print full_path
        ingest_file('file://' + full_path)

  elastic_songs.repopulate_from_redis()




# Redis sequences
def next_id(sequence_name):
  return redis_client.hincrby('sequences', sequence_name)


def sha256_for_file(path):
  with open(path,'rb') as f: 
    sha = hashlib.sha256()
    for chunk in iter(lambda: f.read(8192), b''): 
         sha.update(chunk)
    return sha.hexdigest()




# Reading Configs
cfg = ConfigParser.ConfigParser()
cfg.read('.config')
api_key = cfg.get('APIKeys', 'api_key')
config.ECHO_NEST_API_KEY=api_key



# Get the ENMFP from an MP3
def get_enmfp_json_from_mp3(url):
  enmfp_codegen_path = cfg.get('Tools', 'enmfp_codegen')
  file_path = urlparse(url).path
  json_str = subprocess.check_output([enmfp_codegen_path, file_path, '30', '30']).decode('utf-8')
  result = json.loads(json_str)[0]
  return result['code']



# Cache EN info for each song
def store_en_info(url):
  u = urlparse(url)

  # Calc or fetch enmfp from cache
  sha = sha256_for_file(u.path)
  key = 'en_enmfp_by_sha:%s' % sha
  enmfp = redis_client.get(key)
  if not enmfp:
    enmfp = get_enmfp_json_from_mp3(url)
    enmfp = redis_client.set(key, enmfp)

  # Do we have this song result in redis?
  en_song_id = redis_client.get('en_song_ids_by_enmfp:%s' % enmfp)
  if en_song_id:
    return {'result': 'exists'} # we've already handled this song, so dont do anyhting for it

  # Still here? Go to EN API for the song and artist info and store it
  s_results = song.identify(code=enmfp)

  if len(s_results) == 0:
    error = "*** ID FAIL %s with code %s" % (url, enmfp)
    print error
    return { 'result': 'error', 'error': error}
  else:
    s = s_results[0]
    print "ID %s" % (url)
    a = artist.Artist(id=s.artist_id)

  #TODO get release info somehow (via en track query then rosetta lookup?)

  # Add artist terms to artist obj for json dump
  ao = a.__dict__
  ao['terms'] = a.terms

  redis_client.set('en_songs:%s' % s.id, json.dumps(s.__dict__))
  redis_client.set('en_artists:%s' % a.id, json.dumps(ao))
  redis_client.set('en_enmfp_by_path:%s' % u.path, enmfp)
  redis_client.set('en_song_ids_by_enmfp:%s' % enmfp, s.id)

  # Only lookup/store artist terms if we dont have yet
  key = 'en_artist_terms:%s' % a.id
  if not redis_client.get(key):
    redis_client.set(key, json.dumps(a.terms))

  return {'result': 'ok', 'song': s, 'artist': a, 'enmfp': enmfp}


def store_id3_info(url):
  u = urlparse(url)
  info = id3.get_id3(u.path)
  redis_client.set('id3s_by_path:%s' % u.path, json.dumps(info))
  return info


# Store file info in redis
def ingest_file(url):
  u = urlparse(url)

  id3_info = store_id3_info(url)
  en_info = store_en_info(url)

  file = {
    'id'   : next_id('files'),
    'url'  : url,
    'id3'  : id3_info,
  }

  if en_info['result'] == 'ok':
    en_attrs = {
      'enmfp': en_info['enmfp'],
      'en_artist_id' : en_info['artist'].id,
      'en_song_id' : en_info['song'].id,
    }
    file = dict(file.items() + en_attrs.items())

  redis_client.set('files:%s' % file['id'], json.dumps(file))
  return 'OK'




if __name__ == "__main__":
  main()
