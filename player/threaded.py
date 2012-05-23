hostname ="localhost"
port= 8000
password = "password"

import shout
import sys
import threading
from glob import glob
from random import shuffle,choice

class RunStream (threading.Thread):
   def __init__ (self, channel_mount, music_directory, station_url, genre,name,         description, bitrate="128", samplerate="44100", channels="5",music_format="mp3", ogv=0):
    #connection to icecast
    global hostname,port,password
    self.song_conter= 0
    self.s = shout.Shout()
    self.s.audio_info = {shout.SHOUT_AI_BITRATE:bitrate,   shout.SHOUT_AI_SAMPLERATE:samplerate, shout.SHOUT_AI_CHANNELS:channels}
    self.s.name = name
    self.s.url = station_url
    self.s.mount = channel_mount
    self.s.port = port
    self.ogv = ogv
    self.s.password = password
    self.s.genre = genre
    self.music_directory = music_directory
    self.s.description = description
    self.s.host = hostname
    self.s.format = music_format #using mp3 but it can also be ogg vorbis
    print self.s.open()
    threading.Thread.__init__ (self)

#checking directories for files to stream
   def scan_directories(self):
      self.files_array = glob(self.music_directory+"/*.[mM][Pp]3")  + glob(self.music_directory+"/*/*.[mM][Pp]3") + glob(self.music_directory+"/*/*/*.[mM][Pp]3")   #checks the specified directory down to the third depth
      print str(len(self.files_array))+" files" #display number of matching files found
      shuffle(self.files_array) # randomize playlist

   def run (self):
      while 1: #infinity
        self.scan_directories() # rescan dir, maybe in time you add some new songs
    self.song_counter = 0   
    for e in self.files_array:
           self.write_future()
           self.sendfile(e)
           self.song_counter = self.song_counter + 1

   def format_songname(self,song): # format song name - on filename (strip "mp3", change _ to " ". Formatting name of song for writing into a text file
      result = song.split("/")[-1].split(".")
      result = ".".join(result[:len(result)-1]).replace("_"," ").replace("-"," - ")
  return result

   def write_future(self): #write playlist
      filename = self.s.mount.replace("/","")+"-current.txt"
      fa = open(filename,"w")
      aid = self.song_counter
      pos = 7 # CHANGE if you want more songs in future playlist
      for s in self.files_array[aid:]:
         fa.write(self.format_songname(s)+"\n")
         pos = pos - 1
         if (pos==0):
            break
      if (pos>0):
         for s in self.files_array[:pos+1]:
            fa.write(self.format_songname(s)+"\n")
      fa.close()   

   def sendfile(self,fa):
      print "opening file %s" % fa
      f = open(fa)
      self.s.set_metadata({'song': self.format_songname(fa)})
      nbuf = f.read(4096)
      while 1:
         buf = nbuf
         nbuf = f.read(4096)
         if len(buf) == 0:
            break
         self.s.send(buf)
         self.s.sync()
      f.close()

#running the first stream
RunStream(channel_mount = "/stream", music_directory = "/home/CUWebRadio1/music_one", station_url = "http://webradio.com", genre = "new",name = "Web Radio Channel2", description = "bla bla bla").start()

#running the second stream
RunStream(channel_mount = "/stream_2", music_directory = "/home/CUWebRadio1/music_twos", station_url = "http://webradio.com", genre = "music",name = "Web Radio Music", description = "bla bla bla").start()

#running the Third Stream
RunStream(channel_mount = "/stream_3", music_directory = "/home/CUWebRadio1/music_three", station_url = "http://webradio.com", genre = "Music",name = "CU Web Radio Music3", description = "bla bla bla").start()
