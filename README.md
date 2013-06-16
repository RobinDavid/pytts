pytts
=====

PyTTS is multi-platform Text-To-Speech module based on Google translate engine. Therefore it takes advantage of Google's mixed engines,
and the 27 languages can be used.

Requirement
-----------

PyTTS requires an internet connection because every request are sent to Google's engine.

The python modules required are gstreamer and gobject. Gstreamer is used to read the speech stream from Google to play it back on Speakers.
Gobject is used to keep the handle while the speech is not played entirely. (Catch the gstreamer eos(End Of Stream) message)

How to use it ?
---------------

You can use this script either as a program either as a module. In both case it's usage is fairly easy.

As a script
-----------

To use it as a script you should give in first argument the language code followed by the text. Internaly it creates an pytts object and call the "say" methods which speech the text
and return when the speech is done. Example:

    ./pytts en Hello world !

As a python module
------------------

To use PyTTS as a module, you just need to import the module and instanciate a pytts object. Then you can for instance call the "say" method to speech the given text.

    from pytts import pytts
    pytts().say("Hello world !","en")

The available methods for pytts are:

say(self, text, lang='en', volume=5.0)
  Speech the given text, and return when its done.

sayNB(self, text, lang='en', volume=5.0)
  Same as say but non-blocking method. NB (for non blocking)

download(self, text, lang='en', filename="translate_tts.mp3")
  Download the mp3 speech file instead of playing it. (Into the given file path)

setVolume(self, val)
  Put the player volume at the given value


