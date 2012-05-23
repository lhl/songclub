#!/usr/bin/env python
# Screamy 0.1
# Requirement:
# - python
# - pyaudio http://people.csail.mit.edu/hubert/pyaudio/
# - pylame http://sourceforge.net/project/showfiles.php?group_id=290&package_id=65402&release_id=122800
# - shout-python http://icecast.org/download.php
# Copyright (c) 2007 Silvano Galliani http://intanto.org
#
# Screamy is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# Screamy is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with Screamy; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA
import shout
import string
import pyaudio
import sys
import lame
import os
from threading import Thread
s = shout.Shout()
# configure it here
s.host = 'intanto.org'
s.port = 8000
s.user = 'source'
s.password = 'guess'
s.mount = "/screamy.mp3"
s.format = 'mp3'
s.protocol = 'http'
s.name = 'screamy'
s.genre = 'antani'
s.url = 'http://intanto.org'
s.public = 0 | 1
CHANNELS = 2
RATE = 44100
##############################
FORMAT = pyaudio.paInt16
chunk = 1024
if sys.platform == 'darwin':
    CHANNELS = 1
p=pyaudio.PyAudio()
stream = p.open(format = FORMAT, channels = CHANNELS, rate = RATE, input = True, frames_per_buffer = chunk)
# mp3 config
mp3 = lame.encoder()
mp3.num_channels = CHANNELS
#mp3.set_num_samples(long(320000))
mp3.set_abr_bitrate(128)
#mp3.set_in_samplerate (RATE)
#mp3.set_out_samplerate (32000)
#############################
mp3.init()
s.open() # open connection to icecast server
print "Screamy starts streaming!"
nbuf = stream.read(1024)
while 1:
    raw_audio = stream.read(1024) # get raw audio
    audio_encoded = mp3.encode_interleaved(raw_audio) # encode audio to mp3
    s.sync()
    if len(raw_audio) == 0: break
    s.send(audio_encoded) # send mp3 audio to icecast
s.close()
stream.stop_stream()
stream.close()
stream.terminate()
