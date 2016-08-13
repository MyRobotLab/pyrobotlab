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


#starting the INMOOV
i01 = Runtime.createAndStart("i01", "InMoov")
i01.setMute(True)

##############STARTING THE RIGHT HAND#########
i01.rightHand = Runtime.create("i01.rightHand", "InMoovHand")
#tweaking defaults settings of right hand
i01.rightHand.thumb.setMinMax(20,155)
i01.rightHand.index.setMinMax(30,130)
i01.rightHand.majeure.setMinMax(38,150)
i01.rightHand.ringFinger.setMinMax(30,170)
i01.rightHand.pinky.setMinMax(30,150)
i01.rightHand.thumb.map(0,180,20,155)
i01.rightHand.index.map(0,180,30,130)
i01.rightHand.majeure.map(0,180,38,150)
i01.rightHand.ringFinger.map(0,180,30,175)
i01.rightHand.pinky.map(0,180,30,150)
#################

#################STARTING RIGHT ARM###############
i01.startRightArm(rightPort)
#i01.rightArm = Runtime.create("i01.rightArm", "InMoovArm")
## tweak default RightArm
i01.detach()
i01.rightArm.bicep.setMinMax(0,60)
i01.rightArm.bicep.map(0,180,0,60)
i01.rightArm.rotate.setMinMax(46,160)
i01.rightArm.rotate.map(0,180,46,160)
i01.rightArm.shoulder.setMinMax(0,155)
i01.rightArm.shoulder.map(0,180,0,155)
i01.rightArm.omoplate.setMinMax(8,85)
i01.rightArm.omoplate.map(0,180,8,85)

######################################################################
# mouth service, speech synthesis
i01.mouth = Runtime.createAndStart("i01.mouth", "AcapelaSpeech")
i01.mouth.setVoice(botVoice)


#############STARTING THE HEAD##############
i01.head = Runtime.create("i01.head", "InMoovHead")
#weaking defaults settings of head
i01.head.jaw.setMinMax(35,75)
i01.head.jaw.map(0,180,35,75)
i01.head.jaw.setRest(35)
#tweaking default settings of eyes
i01.head.eyeY.setMinMax(0,180)
i01.head.eyeY.map(0,180,70,110)
i01.head.eyeY.setRest(90)
i01.head.eyeX.setMinMax(0,180)
i01.head.eyeX.map(0,180,70,110)
i01.head.eyeX.setRest(90)
i01.head.neck.setMinMax(40,142)
i01.head.neck.map(0,180,40,142)
i01.head.neck.setRest(70)
i01.head.rothead.setMinMax(21,151)
i01.head.rothead.map(0,180,21,151)
i01.head.rothead.setRest(88)

########STARTING SIDE NECK CONTROL########

def neckMoveTo(restPos,delta):
	leftneckServo.moveTo(restPos + delta)
	rightneckServo.moveTo(restPos - delta)

leftneckServo = Runtime.start("leftNeck","Servo")
rightneckServo = Runtime.start("rightNeck","Servo") 
right = Runtime.start("i01.right", "Arduino")
#right.connect(rightPort)


leftneckServo.attach(right, 13)
rightneckServo.attach(right, 12)

restPos = 90
delta = 20
neckMoveTo(restPos,delta)


#########STARTING MOUTH CONTROL###############
#i01.startMouthControl(rightPort)
#i01.mouthControl.setmouth(0,180)

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
i01.ear = Runtime.createAndStart("i01.ear", "WebkitSpeechRecognition")
i01.ear.addListener("publishText", python.name, "heard");
i01.ear.addMouth(i01.mouth)

######################################################################
# MRL Routing webkitspeechrecognition/ear -> program ab -> htmlfilter -> mouth
######################################################################
i01.ear.addTextListener(zorba)
zorba2.addTextListener(htmlfilter)
htmlfilter.addTextListener(i01.mouth)


######################################################################
# Launch the web gui and create the webkit speech recognition gui
# This service works in Google Chrome only with the WebGui
#################################################################
webgui = Runtime.createAndStart("webgui","WebGui")

######################################################################
# Helper functions and various gesture definitions
######################################################################
i01.loadGestures(gesturesPath)


######################################################################
# start services
######################################################################
#leftneckServo.detach()
#rightneckServo.detach()
#i01.startRightHand(rightPort)
#i01.detach()
##i01.startHead(leftPort)
##i01.detach()
##ear.startListening()
#i01.detach()
##i01.detach()


 
