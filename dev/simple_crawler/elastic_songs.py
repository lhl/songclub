from pyes import *
import redis
import hashlib

es_conn = ES('127.0.0.1:9200')
redis_client = redis.Redis(host='localhost', port=6379, db=0)




def reset_indicies():
  try:
    es_conn.delete_index('songs-index')
    es_conn.delete_index('files-index')
    es_conn.delete_index('artists-index')
  except:
    pass

  es_conn.create_index("songs-index")
  es_conn.create_index("files-index")
  es_conn.create_index("artists-index")


def repopulate_from_redis():
  reset_indicies()

  song_keys = redis_client.keys('en_songs:*')
  for song_key in song_keys:
    song_doc = redis_client.get(song_key)
    add_song(song_doc)

  artist_keys = redis_client.keys('en_artists:*')
  for artist_key in song_keys:
    artist_doc = redis_client.get(artist_key)
    add_artist(artist_doc)



def add_file(file_doc):
  es_conn.index(file_doc, 'files-index', 'file')


def add_song(song_doc):
  es_conn.index(song_doc, 'songs-index', 'song')


def add_artist(artist_doc):
  es_conn.index(artist_doc, 'artists-index', 'artist')
