#Huge thankyou to Kwatter, this is his original work tailored for my use. 
#This chatbot (SARAH) is intened to provide QA services, some personal assistant services and provide interface between user
#and Trashy_bot as well as home automation devices
# Created by Nolan Jan 6,  2016

from java.lang import String

######################################################################
# SARAH is an AIML based MRL powered implementation 
######################################################################
 
aimlDir = "/home/Desktop/MRL/develop/ProgramAB"
userName = "nolan"
botName = "sarah"
 

######################################################################
# A helper function to print the recognized text to the python window.
# semi-useful for debugging.
######################################################################
def heard(data):
  print "Speech Recognition:" + str(data)
 
######################################################################
# Create ProgramAB chat bot
######################################################################
sarah = Runtime.createAndStart("sarah", "ProgramAB")
# start the session for the chat bot
sarah.startSession(aimlDir, userName, botName)

######################################################################
# create the speech recognition service
# Speech recognition is based on WebSpeechToolkit API
# So this just means we need the web gui, it's part of the programAB 
# service now.
######################################################################
# Start the REST API for MRL
webgui = Runtime.createAndStart("webgui","WebGui")

######################################################################
# create the html filter to filter the output of program ab
######################################################################
htmlfilter = Runtime.createAndStart("htmlfilter", "HtmlFilter")
 
######################################################################
# create the speech to text service (named the same as the inmoov's)
# TODO: consider a different voice?
######################################################################
mouth = Runtime.createAndStart("mouth", "MarySpeech")
# mouth.setGoogleURI("http://thehackettfamily.org/Voice_api/api2.php?voice=Ryan&txt=")
#can acapela work here? 
 
######################################################################
# MRL Routing   webgui (speech recognition) -> program ab -> htmlfilter -> inmoov
######################################################################
# Add route from Program AB to html filter
sarah.addTextListener(htmlfilter)
# Add route from html filter to mouth
htmlfilter.addTextListener(mouth)
 
# make sure the ear knows if it's speaking.
# TODO: how does this jive with webspeech ?!
# sphinx.attach(mouth)

