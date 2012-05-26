from pyes import *
import redis
import hashlib

es_conn = ES('127.0.0.1:9200')
redis_client = redis.Redis(host='localhost', port=6379, db=0)




def reset_indicies():
  try:
    es_conn.delete_index('songs')
    es_conn.delete_index('files')
    es_conn.delete_index('artists')
  except:
    pass

  es_conn.create_index("songs")
  es_conn.create_index("files")
  es_conn.create_index("artists")


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

  file_keys = redis_client.keys('files:*')
  for file_key in file_keys:
    file_doc = redis_client.get(file_key)
    add_file(file_doc)

  es_conn.refresh()



def add_file(file_doc, bulk=True):
  es_conn.index(file_doc, 'files', 'file', bulk=bulk)


def add_song(song_doc, bulk=True):
  es_conn.index(song_doc, 'songs', 'song', bulk=bulk)


def add_artist(artist_doc, bulk=True):
  es_conn.index(artist_doc, 'artists', 'artist', bulk=bulk)


""" 
Example of how to query elastic_search
q = TermQuery("title", "slow")
qr = es_conn.search(q.search())
qr.hits

Elastic Search http interface example urls:
Search  http://127.0.0.1:9200/files/_search?q=title:slow
Status  http://127.0.0.1:9200/_cluster/state   
"""
