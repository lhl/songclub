import eyeD3

def get_id3(path):
  trackInfo = eyeD3.Mp3AudioFile(path)
  tag = trackInfo.getTag()
  tag.link(path)

  tags = { 
    'artist': tag.getArtist(),
    'album': tag.getAlbum(),
    'title': tag.getTitle(),
    'length': trackInfo.getPlayTimeString(),
    'year': tag.getYear()
  }

  return tags

