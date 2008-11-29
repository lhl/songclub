#!/usr/bin/python

import magic, os, re, socket, sys
import eyeD3
from couchdb import *
from hashlib import *
from pprint import pprint
from time import sleep,strftime

'''
TODO:
  put into functions
  check to see if it exists, update if appropriate

  Unicode collations:
  http://unit.bjork.com/specials/albums/medulla/

  Better MP3 - filetype vs longfiletype
'''

s = Server('http://127.0.0.1:5984/')
db = s['songclub']
mp3re = re.compile('\.mp3$', re.IGNORECASE)

def main():
  dir = '/locker/music/_misc'

  for root, dirs, files in os.walk(dir):
    root = unicode(root, 'utf8')

    # Folders
    for d in dirs:
      try:
        d = unicode(d, 'utf8')
      except UnicodeDecodeError:
        print strftime("[%Y-%m-%d %H:%M:%S] ") + 'Unicode Error with: ' + d
      entry = {'proto': 'file',
               'owner': 'lhl',
               'path' : root,
              }
      entry['location'] = root + '/' + d + '/'
      entry['name'] = d + '/'
      entry['type'] = 'folder'

      entry['filelist'] = os.listdir(entry['location'].encode('utf8'))

      try:
        entry['filelist'] = map(lambda x: unicode(x, 'utf8'), entry['filelist'])
      except UnicodeDecodeError:
        print strftime("[%Y-%m-%d %H:%M:%S] ") + 'Unicode Error with: ' + entry['location']

      entry['filecount'] = len(os.listdir(entry['location'].encode('utf8')))

      mp3count = len(filter(lambda x: mp3re.search(x), entry['filelist']))
      if mp3count:
        entry['mp3count'] = mp3count

      # addentry(entry)

    # Files
    for f in files:
      try:
        f = unicode(f, 'utf8')
      except UnicodeDecodeError:
        print strftime("[%Y-%m-%d %H:%M:%S] ") + 'Unicode Error with: ' + f
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

      # if mp3 file...
      if eyeD3.isMp3File(entry['location'].encode('utf8')):
        try:
          mp3 = eyeD3.Mp3AudioFile(entry['location'].encode('utf8'))
          entry['mp3'] = {}
          entry['mp3']['vbr'], entry['bitrate'] = mp3.getBitRate()
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
              entry['mp3']['date'] = map(lambda x: x.getDate(), mp3.tag.getDate())
            if mp3.tag.getComments():
              entry['mp3']['comments'] = map(lambda x: x.__unicode__(), mp3.tag.getComments())
            if mp3.tag.getLyrics():
              entry['mp3']['lyrics'] = map(lambda x: x.__unicode__(), mp3.tag.getLyrics())
            if mp3.tag.getUserTextFrames():
              entry['mp3']['usertext'] = map(lambda x: x.__unicode__(), mp3.tag.getUserTextFrames())
        except eyeD3.tag.InvalidAudioFormatException:
          pass

      # pprint(entry)
      # print
      addentry(entry)


def addentry(entry):
  try: 
    db.create(entry)
    print strftime("[%Y-%m-%d %H:%M:%S] ") + 'Added file ' + entry['location'].encode('utf8')
  except socket.error:
    print strftime("[%Y-%m-%d %H:%M:%S] ") + 'Error connecting to CouchDB.  Waiting 5s and trying again... (' + entry['location'].encode('utf8') + ')'
    sleep(5)
    addentry(entry)
  except UnicodeDecodeError:
    print strftime("[%Y-%m-%d %H:%M:%S] ") + 'Unicode Error with: ' + entry['location']


if __name__ == "__main__":
  main()
