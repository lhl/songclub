from pyes import *

conn = ES('127.0.0.1:9200')

def reset_indicies():
  try:
    conn.delete_index('songs-index')
    conn.delete_index('files-index')
  except:
    pass

  conn.create_index("songs-index")
  conn.create_index("files-index")



def add_file(file_doc):
  conn.index(file_doc, 'files-index', 'file')


def add_song(song_doc):
  conn.index(song_doc, 'songs-index', 'song')


def add_artist(artist_doc):
  conn.index(artist_doc, 'artists-index', 'artist')
