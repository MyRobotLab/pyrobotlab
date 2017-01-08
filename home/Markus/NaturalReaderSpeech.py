# This script is working 2016-02-22
# It starts the webkitspeechrecognition, the chatbot and the webgui
# Create ProgramAB chat bot
######################################################################
lloyd = Runtime.createAndStart("lloyd", "ProgramAB")
lloyd.startSession("markus", "alice2")
# Only works with Chrome !!!!
# To connect to the webgui use this link:
# http://<thishostname:8888/#service/webkitspeechrecognition
# TODO
# Testing on Adriod tablet Chrome Pro is almost working. It reads and translate from speech to text, but I don't think it's posting the content back
# Testing on iPhone Chrome,  nothing shows
######################################################################
# A helper function to print the recognized text to the python window.
# semi-useful for debugging.
######################################################################
def heard(data):
  print "Speech Recognition Data:", data
 

######################################################################
######################################################################
##webgui = Runtime.createAndStart("webgui","WebGui")
# Start webgui without starting the browser
######################################################################
webgui = Runtime.create("WebGui","WebGui")
webgui.autoStartBrowser(False)
webgui.startService()

######################################################################
# Create the webkit speech recognition gui
######################################################################
wksr = Runtime.createAndStart("webkitspeechrecognition", "WebkitSpeechRecognition")
######################################################################
# create the html filter to filter the output of program ab
######################################################################
htmlfilter = Runtime.createAndStart("htmlfilter", "HtmlFilter")
 
######################################################################
# create the speech to text service 
######################################################################
speech = Runtime.createAndStart("speech","NaturalReaderSpeech")
speech.setVoice("Laura")

######################################################################
# create the mouthcontrol to make the jaw move
######################################################################
speech.speakBlocking("Testing to speak")

######################################################################
# MRL Routing webkitspeechrecognition -> program ab -> htmlfilter -> inmoov
######################################################################
# add a route from Sphinx to ProgramAB
# sphinx.addTextListener(lloyd)
# debugging in python route.
# sphinx.addListener("publishText", python.name, "heard", String().getClass());
wksr.setLanguage("sv")
# add a link between the webkit speech to publish to ProgramAB
wksr.addTextListener(lloyd)
# Add route from Program AB to html filter
lloyd.addTextListener(htmlfilter)
# Add route from html filter to mouth
htmlfilter.addTextListener(speech)
# make sure the ear knows if it's speaking.
# TODO: how does this jive with webspeech ?!
# sphinx.attach(mouth)

######################################################################
# MRL Routing webkitspeechrecognition -> program ab -> htmlfilter -> inmoov
######################################################################
# add a route from Sphinx to ProgramAB
# sphinx.addTextListener(lloyd)
# debugging in python route.
# sphinx.addListener("publishText", python.name, "heard", String().getClass());
 
# add a link between the webkit speech to publish to ProgramAB
wksr.addTextListener(lloyd)
# Add route from Program AB to html filter
lloyd.addTextListener(htmlfilter)
# Add route from html filter to mouth
htmlfilter.addTextListener(speech)
webgui.startBrowser("http://localhost:8888/#/service/webkitspeechrecognition")

# make sure the ear knows if it's speaking.
# TODO: how does this jive with webspeech ?!
# sphinx.attach(mouth)
speech.speakBlocking("okay i am ready for conversation")




