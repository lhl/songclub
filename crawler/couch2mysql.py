#!/usr/bin/python

import MySQLdb, simplejson, sys
from couchdb import *

# CouchDB is sort of ridiculous...
# 5.4GB for 62K docs
# Temporary views take foreeeeeever

def main():
  # MySQL
  conn = MySQLdb.connect(user='user', passwd='passwd', db='songclub', use_unicode=True, charset="utf8")
  c = conn.cursor(MySQLdb.cursors.DictCursor)

  # CouchDB
  s = Server('http://127.0.0.1:5984/')
  db = s['songclub']

  for row in db:
    file = db[row]
    
    if 'location' in file:
      location = file['location']
    else:
      location = None

    if 'path' in file:
      path = file['path']
    else:
      path = None

    if 'name' in file:
      name = file['name']
    else:
      name = None

    if 'proto' in file:
      proto = file['proto']
    else:
      proto = None

    if 'owner' in file:
      owner = file['owner']
    else:
      owner = None

    # Folder
    if file['type'] == 'folder':
      type = 'folder'

      if 'filecount' in file:
        filecount = file['filecount']
      else:
        filecount = None

      if 'mp3count' in file:
        mp3count = file['mp3count']
      else:
        mp3count = None

      if 'filelist' in file:
        filelist = simplejson.dumps(file['filelist'], allow_nan=False, ensure_ascii=False).encode('utf8')
      else:
        filelist = None

      sql = "INSERT INTO files (location, path, name, proto, type, owner, filecount, mp3count, filelist) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
      # ON DUPLICATE KEY UPDATE...  vs REPLACE INTO
      c.execute(sql, (location, path, name, proto, type, owner, filecount, mp3count, filelist))

    # Regular File
    else:
      type = 'file'

      if 'type' in file:
        magic = file['type']
      else:
        magic = None

      if 'ext' in file:
        ext = file['ext']
      else:
        ext = None

      if 'mp3' in file:
        mp3 = simplejson.dumps(file['mp3'], allow_nan=False, ensure_ascii=False).encode('utf8')
      else:
        mp3 = None

      if 'mtime' in file:
        mtime = file['mtime']
      else:
        mtime = None

      if 'size' in file:
        size = file['size']
      else:
        size = None

      if 'sha1' in file:
        sha1 = file['sha1']
      else:
        sha1 = None

      sql = "INSERT INTO files (location, path, name, proto, type, magic, owner, ext, mp3, mtime, size, sha1) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
      c.execute(sql, (location, path, name, proto, type, magic, owner, ext, mp3, mtime, size, sha1))
    
    # Commit!
    conn.commit()


if __name__ == '__main__':
  main()
