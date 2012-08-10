#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import gst
import gobject
from urllib2 import Request, urlopen

class pytts():
    def on_finish(self, bus, message): #Callback triggered at the end of the stream
        self.player.set_state(gst.STATE_NULL)
        self.mainloop.quit()
  
    def __init__(self):
        self.player = None
        self.mainloop = gobject.MainLoop() #Instantiate the mainloop even if not used

    def say(self, text, lang="en",volume=5.0):
        music_stream_uri = 'http://translate.google.com/translate_tts?'+'q='+text+'&tl='+lang+"&ie=UTF-8"
        self.player = gst.element_factory_make("playbin", "player") #Create the player
        self.player.set_property('uri', music_stream_uri) #Provide the source which is a stream
        self.player.set_property('volume',volume) #Val from 0.0 to 10 (float)
        self.player.set_state(gst.STATE_PLAYING) #Play

        bus = self.player.get_bus() #Get the bus (to send catch connect signals..)
        bus.add_signal_watch_full(1)
        bus.connect("message::eos", self.on_finish) #Connect end of stream to the callback
        self.mainloop.run() #Wait an event


    def sayNB(self, text, lang="en",volume=5.0): #NB for Non-Blocking
        music_stream_uri = 'http://translate.google.com/translate_tts?tl='+lang+'&q=' + text +"&ie=UTF-8"
        self.player = gst.element_factory_make("playbin", "player") #Create the player
        self.player.set_property('uri', music_stream_uri) #Provide the source which is a stream
        self.player.set_property('volume',volume) #Val from 0.0 to 10 (float)
        self.player.set_state(gst.STATE_PLAYING) #Play

    def download(self, text, lang="en", filename="translate_tts.mp3"):
        req = Request(url='http://translate.google.com/translate_tts')
        req.add_header('User-Agent', 'My agent !') #Needed otherwise return 403 Forbidden
        req.add_data("tl="+lang+"&q="+text+"&ie=UTF-8")
        fin = urlopen(req)
        mp3 = fin.read()
        fout = file(filename, "wb")
        fout.write(mp3)
        fout.close()
    
    def setVolume(self, val):
        self.player.set_property('volume',val) #Val from 0 to 1 (float)
    
if __name__=="__main__":
  input_string = sys.argv

  if len(input_string) < 3:
      print("Usage: ./tts.py language_code Your text separated with spaces.")
      sys.exit(1)

  input_string.pop(0) #remove the program name from the argv list
  lang = input_string[0] #Take the language which should be now the first args
  input_string.pop(0) #Pop it
  tts_string = '+'.join(input_string) #convert to url all the rest (with + replacing spaces) Nice but not needed
  
  pytts().say(tts_string, lang)
  
  sys.exit(0)