from java.lang import String
 
######################################################################
# A helper function to print the recognized text to the python window.
# semi-useful for debugging.
######################################################################
def heard(data):
  print "Speech Recognition Data:", data
 
######################################################################
# Create ProgramAB chat bot
######################################################################
programAB = Runtime.start("programAB", "ProgramAB")
# this starts a session between username "kevin" and the chat bot named
# "alice2"  (AIML for the bots are in the develop/ProgramAB/bots directory.
programAB.startSession("mats", "en-US")

######################################################################
# create the speech recognition service
# Speech recognition is based on WebSpeechToolkit API
######################################################################
# Start the new WebGuiREST API for MRL
# webgui = Runtime.createAndStart("webgui","WebGui")
webgui = Runtime.create("webgui","WebGui")
webgui.autoStartBrowser(False)
webgui.startService()

######################################################################
# Create the webkit speech recognition gui
# This service works in Google Chrome only with the WebGui
######################################################################
wksr = Runtime.start("wksr", "WebkitSpeechRecognition")
# auto rearm microphone
wksr.setAutoListen(True)
# speedup recognition if False
wksr.setContinuous(True)
######################################################################
# create the html filter to filter the output of program ab
# this service will strip out any html markup and return only the text
# from the output of ProgramAB
######################################################################
htmlfilter = Runtime.start("htmlfilter", "HtmlFilter")
 
######################################################################
# create the speech to text service (named the same as the inmoov's)
# This service will listen to the output from the htmlfilter and
# call out to the Acapela group to get the an MP3 that represents the
# text to be spoken.  That mp3 will be played back by an AudioFile 
# service.
######################################################################
mouth = Runtime.start("i01.mouth", "MarySpeech")
mouth.setVoice("Mark")

# debugging in python route.
# wksr.addListener("publishText", python.name, "heard", String().getClass());
webgui.startBrowser("http://localhost:8888/#/service/wksr")
######################################################################
# MRL Routing webkitspeechrecognition -> program ab -> htmlfilter -> mouth
######################################################################
# add a link between the webkit speech to publish text to ProgramAB
wksr.addTextListener(programAB)
# Add route from Program AB to publish text to the html filter
programAB.addTextListener(htmlfilter)
# Add route to publish text from html filter to mouth
htmlfilter.addTextListener(mouth)
