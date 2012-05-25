import unittest
from fs_crawler import *

class TestAlbumInfo(unittest.TestCase):
  def test_get_album_info_from_path(self):
    test_cases = {
        'Artist Name - 2010 - Album Title' : AlbumInfo(
          artist_name = 'Artist Name', 
          year = '2010', 
          album_title = 'Album Title',
          misc = None,
          length = None),
        'Artist Name - 2010 - Album Title (Misc)' : AlbumInfo(
          artist_name = 'Artist Name', 
          year = '2010', 
          album_title = 'Album Title',
          misc = 'Misc',
          length = None),
        'Artist Name - 2010 - Album Title EP' : AlbumInfo(
          artist_name = 'Artist Name', 
          year = '2010', 
          album_title = 'Album Title',
          misc = None,
          length = 'EP'),
        }

    for path in test_cases:
      self.assertEqual(test_cases[path], get_album_info_from_path(path))
