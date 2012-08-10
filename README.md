pytts
=====

Text-To-Speech multi-platform in python. It uses Google translate engine.

Requirement
-----------

The only module required is gstreamer for python. Indeed the script need this module to grab the voice stream and gobject to
for the voice to end.

How to use it ?
---------------

You can use this script either as a program either as a module. To use it as a program you should give in first argument
the language code followed by the text. Exampleee:

    ./pytts en Hello world !

To use it as a module to following do the exact same thing:

    from pytts import pytts
    pytts().say("Hello world !","en")