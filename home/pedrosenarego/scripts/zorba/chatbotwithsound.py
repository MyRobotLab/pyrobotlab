from java.lang import String
import threading
import random
import codecs
import io
import itertools
import time
import os
import urllib2
import textwrap
import socket
import shutil



#############################################################
# This is the ZOrba
# 
#############################################################
# All bot specific configuration goes here.
leftPort = "COM31"
rightPort = "/dev/ttyACM0"
headPort = leftPort
gesturesPath = "/home/pedro/Dropbox/pastaPessoal/3Dprinter/inmoov/scripts/zorba/gestures"
botVoice = "WillBadGuy"


######################################################################
# mouth service, speech synthesis
mouth = Runtime.createAndStart("i01.mouth", "AcapelaSpeech")
mouth.setVoice(botVoice)




######################################################################
# helper function help debug the recognized text from webkit/sphinx
######################################################################
def heard(data):
  print "Speech Recognition Data:"+str(data)


######################################################################
# Create ProgramAB chat bot ( This is the inmoov "brain" )
######################################################################
zorba2 = Runtime.createAndStart("zorba", "ProgramAB")
zorba2.startSession("Pedro", "zorba")

######################################################################
# Html filter to clean the output from programab.  (just in case)
htmlfilter = Runtime.createAndStart("htmlfilter", "HtmlFilter")


######################################################################
# the "ear" of the inmoov TODO: replace this with just base inmoov ear?
ear = Runtime.createAndStart("i01.ear", "WebkitSpeechRecognition")
ear.addListener("publishText", python.name, "heard");
ear.addMouth(mouth)

######################################################################
# MRL Routing webkitspeechrecognition/ear -> program ab -> htmlfilter -> mouth
######################################################################
ear.addTextListener(zorba)
zorba2.addTextListener(htmlfilter)
htmlfilter.addTextListener(mouth)

#starting the INMOOV
i01 = Runtime.createAndStart("i01", "InMoov")
i01.setMute(True)
i01.mouth = mouth


######################################################################
# Launch the web gui and create the webkit speech recognition gui
# This service works in Google Chrome only with the WebGui
#################################################################
webgui = Runtime.createAndStart("webgui","WebGui")

######################################################################
# Helper functions and various gesture definitions
######################################################################
i01.loadGestures(gesturesPath)
ear.startListening()
 
