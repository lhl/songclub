from pyes import *
import redis
import hashlib

es_conn = ES('127.0.0.1:9200')
redis_client = redis.Redis(host='localhost', port=6379, db=0)




def reset_indicies():
  indicies = ['en_songs', 'files', 'en_artists', 'en_artist_terms']

  try:
    for index in indicies:
      es_conn.delete_index(index) 
  except:
    pass

  for index in indicies:
    es_conn.create_index(index) 


def repopulate_from_redis():
  reset_indicies()

  def repop_es(redis_key_prefix, es_index_name, es_doc_type):
    keys = redis_client.keys(redis_key_prefix + ':*')
    for key in keys:
      doc = redis_client.get(key)
      es_conn.index(doc, es_index_name, es_doc_type, bulk=True)

  repop_es(redis_key_prefix='en_songs', es_index_name='en_songs', es_doc_type='song')
  repop_es(redis_key_prefix='en_artists', es_index_name='en_artists', es_doc_type='artist')
  #repop_es(redis_key_prefix='en_artist_terms', es_index_name='en_artist_terms', es_doc_type='artist_terms')
  repop_es(redis_key_prefix='files', es_index_name='files', es_doc_type='file')

  es_conn.refresh()


""" 
Example of how to query elastic_search
q = TermQuery("title", "slow")
qr = es_conn.search(q.search())
qr.hits

Elastic Search http interface example urls:
Search  http://127.0.0.1:9200/files/_search?q=title:slow
Status  http://127.0.0.1:9200/_cluster/state   
"""
