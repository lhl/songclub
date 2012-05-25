import collections
import re

AlbumInfo = collections.namedtuple('AlbumInfo', ['artist_name', 'year', 'album_title', 'misc', 'length'])

def get_album_info_from_path(path):
  m_misc = re.search('(.*) - (.*) - (.*) \((.*)\)', path)
  m_ep = re.search('(.*) - (.*) - (.*) EP', path)
  m_default = re.search('(.*) - (.*) - (.*)', path)

  if m_misc:
    return AlbumInfo(
        artist_name = m_misc.group(1),
        year = m_misc.group(2),
        album_title = m_misc.group(3),
        misc = m_misc.group(4),
        length = None)
  elif m_ep:
    return AlbumInfo(
        artist_name = m_ep.group(1), 
        year = m_ep.group(2), 
        album_title = m_ep.group(3), 
        misc = None, 
        length = 'EP')
  else:
    return AlbumInfo(
        artist_name = m_default.group(1), 
        year = m_default.group(2), 
        album_title = m_default.group(3), 
        misc = None, 
        length = None)
