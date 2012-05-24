def interact():
  import code
  code.InteractiveConsole(locals=globals()).interact()

"""
This expects an .config file with the following sections:
[API Keys]
api_key=1234567890

[TOOLS]
enmfp_codegen=/path/to/enmfp/codegen
"""
import ConfigParser
import json
from pyechonest import artist 
from pyechonest import config
from pyechonest import song
import redis
import subprocess
from   urlparse import urlparse

cfg = ConfigParser.ConfigParser()
cfg.read('.config')
api_key = cfg.get('APIKeys', 'api_key')
config.ECHO_NEST_API_KEY=api_key

redis_client = redis.Redis(host='localhost', port=6379, db=0)


# Redis sequences
def next_id(sequence_name):
  return redis_client.hincrby('sequences', sequence_name)


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


ingest_file('file:///Users/gabe/code/songclub/dev/test_music/kylie.mp3')
