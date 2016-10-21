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
inmoov = Runtime.createAndStart("inmoov", "ProgramAB")
# this starts a session between username "nolan" and the chat bot named
# "inmoovwebkit"  (AIML for the bots are in the develop/ProgramAB/bots directory.
inmoov.startSession("nolan", "inmoovwebkit")

######################################################################
# create the speech recognition service
# Speech recognition is based on WebSpeechToolkit API
######################################################################
# Start the new WebGuiREST API for MRL
webgui = Runtime.create("webgui","WebGui")
webgui.autoStartBrowser(False)
webgui.startService()
# Then start the browsers and show the WebkitSpeechRecognition service named i01.ear
webgui.startBrowser("http://localhost:8888/#/service/i01.ear")


######################################################################
# Create the webkit speech recognition gui
# This service works in Google Chrome only with the WebGui
######################################################################
wksr = Runtime.createAndStart("webkitspeechrecognition", "WebkitSpeechRecognition")
htmlfilter = Runtime.createAndStart("htmlfilter", "HtmlFilter")
mouth = Runtime.createAndStart("i01.mouth", "AcapelaSpeech")

# debugging in python route.
# wksr.addListener("publishText", python.name, "heard", String().getClass());

######################################################################
# MRL Routing webkitspeechrecognition -> program ab -> htmlfilter -> mouth
######################################################################
wksr.addTextListener(inmoov)
inmoov.addTextListener(htmlfilter)
htmlfilter.addTextListener(mouth)
