#!/usr/bin/python3

'''
Music Crawler:
* Reads new files
* Inserts into DB

We are using Python 3 to:
  1) Learn Python 3
  2) Make Unicode less painful
'''

import chardet
from   hashlib import *
import magic
import os
from   pprint import pprint
import pymongo
import re
import socket
import stagger
import sys
import time
from   time import sleep, strftime



'''
file {
 location:
 filename:
 parent:
 last_modified:
 type: folder, mp3, image
 extension: png
 md5:

 play_count: 0
}

track {
  artist:
}

song {
}

album {
}

artist {
}

# Tracking plays
play {
}

comment {
}

fave {
}

list {
}



TODO:
  put into functions
  check to see if it exists, update if appropriate

  Unicode collations:
  http://unit.bjork.com/specials/albums/medulla/

  Better MP3 - filetype vs longfiletype

  Handle KeyboardInterrupt
'''

# DB
conn = pymongo.Connection()
db = conn['songclub']

# Globals
dir = '/locker/music'
mime = magic.Magic(mime=True)
encoding = magic.Magic(mime_encoding=True)

def main():
  for root, dirs, files in os.walk(dir):
    # Files
    for f in files:
      location = root + '/' + f
      add_location(root + '/' + f)

    # Folders
    for d in dirs:
      add_location(root + '/' + d)


    '''
    # Folders
    for d in dirs:
      try:
        try:
          d = str(d, 'utf8')
        except UnicodeDecodeError:
          try:
             encoding = chardet.detect(d)['encoding']
             d = str(d, encoding)
          except UnicodeDecodeError:
             print(strftime("[%Y-%m-%d %H:%M:%S] ") + "Unicode Error, couldn't add : " + d)
             
        entry = {'proto': 'file',
                 'owner': 'lhl',
                 'path' : root,
                }
        entry['location'] = root + '/' + d + '/'
        entry['name'] = d + '/'
        entry['type'] = 'folder'

        entry['filelist'] = os.listdir(entry['location'].encode('utf8'))

        try:
          entry['filelist'] = [str(x, 'utf8') for x in entry['filelist']]
        except UnicodeDecodeError:
          print(strftime("[%Y-%m-%d %H:%M:%S] ") + 'Unicode Error with: ' + entry['location'])

        entry['filecount'] = len(os.listdir(entry['location'].encode('utf8')))

        mp3count = len([x for x in entry['filelist'] if mp3re.search(x)])
        if mp3count:
          entry['mp3count'] = mp3count

        addentry(entry)

      except:
        print(strftime("[%Y-%m-%d %H:%M:%S] ") + 'Error adding ' + entry['location'].encode('utf8') + ' ', sys.exc_info())

    # Files
    for f in files:
      try:
        try:
          f = str(f, 'utf8')
        except UnicodeDecodeError:
          try:
             encoding = chardet.detect(f)['encoding']
             f = str(f, encoding)
          except UnicodeDecodeError:
             print(strftime("[%Y-%m-%d %H:%M:%S] ") + "Unicode Error, couldn't add : " + f)

        entry = {'proto': 'file',
                 'owner': 'lhl',
                 'path' : root,
                }
        entry['location'] = root + '/' + f
        entry['name'] = f
        x, entry['ext'] = os.path.splitext(f)
        if entry['ext']:
          entry['ext'] = entry['ext'][1:]

        stat = os.stat(root + '/' + f)
        entry['size'] = stat.st_size
        entry['mtime'] = stat.st_mtime
        entry['sha1'] = sha1(open(entry['location'], 'rb').read()).hexdigest()
        entry['type'] = magic.from_file(entry['location'].encode('utf8'))

    '''

def add_location(location):
  entry = {}
  entry['location'] = location
  entry['encoding'] = encoding.from_file(location.encode('utf-8')).decode('utf-8')
  entry['mime'] = mime.from_file(location.encode('utf-8')).decode('utf-8')
  if os.path.isdir(location):
    entry['type'] = 'folder'
  elif os.path.isfile(location):
    entry['type'] = 'file'
    (root, ext) = os.path.splitext(location)
    if ext:
      entry['extension'] = ext[1:]

      if ext[1:].lower() == 'mp3':
        print(location)
        tag = stagger.read_tag(location)
        for t in tag.values():
          print(t)
        print(tag.title)
        print(tag.comment)
        '''
        try:
          tag = stagger.read_tag(location)
          for t in tag.values():
            print(t)
          print(t.comment)
        except:
          # No tag:w
          pass
        '''
        sys.exit()
        # id3 = getID3()

  # print(entry)


def addentry(entry):
  try: 
    db.create(entry)
    print(strftime("[%Y-%m-%d %H:%M:%S] ") + 'Added file ' + entry['location'].encode('utf8'))
  except socket.error:
    print(strftime("[%Y-%m-%d %H:%M:%S] ") + 'Error connecting to CouchDB.  Waiting 5s and trying again... (' + entry['location'].encode('utf8') + ')')
    sleep(5)
    addentry(entry)
  except UnicodeDecodeError:
    print(strftime("[%Y-%m-%d %H:%M:%S] ") + 'Couldn\'t add to CouchDB. Unicode Error with: ' + entry['location'])

def getID3(entry):
  # Man, Mutagen and eyeD3 both suck. And they throw exceptions like nobody's business
  # Can't there just be a UFP-like library that just works (actually, there is,
  # but it's getID3() for PHP.  There's just nothing good for Python...

  try:
    entry = mutagenparse(entry)
  except:
    try:
      entry = eyeD3parse(entry)
    except:
      print(strftime("[%Y-%m-%d %H:%M:%S] ") + "ID3 Parsing Error: " + entry['location'].encode('utf8') + ' ', sys.exc_info())

def mutagenparse(entry):
  entry['mp3'] = {}
  mp3 = MP3(entry['location'].encode('utf8'))
  entry['mp3']['parser'] = 'Mutagen'
  entry['mp3']['length'] = mp3.info.length
  entry['mp3']['bitrate'] = mp3.info.bitrate

  if mp3.tags:
    frames = list(mp3.tags.keys())
    for key in frames:
      entry['mp3'][ key] = repr(mp3.tags[key])

  try:
    mp3 = EasyID3(entry['location'].encode('utf8'))
    for key in list(mp3.keys()):
      entry['mp3'][key] = repr(mp3[key])
  except ID3NoHeaderError:
    pass


def eyeD3parse(entry):
  if eyeD3.isMp3File(entry['location'].encode('utf8')):
    mp3 = eyeD3.Mp3AudioFile(entry['location'].encode('utf8'))
    entry['mp3'] = {}
    entry['mp3']['parser'] = 'eyeD3'
    entry['mp3']['vbr'], entry['mp3']['bitrate'] = mp3.getBitRate()
    entry['mp3']['freq'] = mp3.getSampleFreq()
    entry['mp3']['length'] = mp3.getPlayTime()

    if mp3.tag:
      if mp3.tag.getArtist():
        entry['mp3']['artist'] = mp3.tag.getArtist()
      if mp3.tag.getTitle():
        entry['mp3']['title'] = mp3.tag.getTitle()
      if mp3.tag.getAlbum():
        entry['mp3']['album'] = mp3.tag.getAlbum()
      if mp3.tag.getYear():
        entry['mp3']['year'] = mp3.tag.getYear()
      if mp3.tag.getTrackNum():
        entry['mp3']['track'] = mp3.tag.getTrackNum()
      if mp3.tag.getDiscNum():
        entry['mp3']['disc'] = mp3.tag.getDiscNum()
      if mp3.tag.getVersion():
        entry['mp3']['version'] = mp3.tag.getVersion()
      if mp3.tag.getVersionStr():
        entry['mp3']['versionstring'] = mp3.tag.getVersionStr()
      try:
        if mp3.tag.getBPM():
          entry['mp3']['bpm'] = mp3.tag.getBPM()
      except ValueError:
        pass
      if mp3.tag.getPublisher():
        entry['mp3']['publiser'] = mp3.tag.getPublisher()

      if mp3.tag.getDate():
        entry['mp3']['date'] = [x.getDate() for x in mp3.tag.getDate()]
      if mp3.tag.getComments():
        entry['mp3']['comments'] = [x.__unicode__() for x in mp3.tag.getComments()]
      if mp3.tag.getLyrics():
        entry['mp3']['lyrics'] = [x.__unicode__() for x in mp3.tag.getLyrics()]
      if mp3.tag.getUserTextFrames():
        entry['mp3']['usertext'] = [x.__unicode__() for x in mp3.tag.getUserTextFrames()]


if __name__ == "__main__":
  main()
