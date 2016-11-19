from java.lang import String
import threading
import time
import random
from org.myrobotlab.net import BareBonesBrowserLaunch
##
import urllib, urllib2
import json

from datetime import datetime
#######################
import io
import itertools
import textwrap
import codecs
import socket
import os
import shutil
import hashlib
import subprocess
import csv
from subprocess import Popen, PIPE

#############################################################
# This is the InMoov script
# InMoov is powered by MyRobotLab
# Initially we'll start simple
# It will use ProgramAB & Webkit for all interactions with
# the bot.
#############################################################
# All bot specific hardware configuration goes here.
leftPort = "COM8"
rightPort = "COM7"
headPort = leftPort

gesturesPath = "C:\github\pyrobotlab\home\brotherbrown831\inmoov\gestures"

aimlPath = "C:\github\pyrobotlab\home\brotherbrown831\inmoov\inmoovWebKit\aiml"
aimlBotName = "inmoovWebKit"
aimlUserName = "Nolan"
#botVoice = "Ryan"
#############################################################
# LANGUAGE ( FR/EN )
lang="EN"
global Voice
Voice="Ryan" # Bruno in French
voiceType = Voice

##Create your free Id and key https://datamarket.azure.com/dataset/bing/microsofttranslator
client_id = "63ee9eef-2c78-4e87-a6be-5fa0fa29acdd"
client_secret = "6wtk1hynqgXlRhNY1vni4zTjJb8Znlp/yeTX4953LaI"

global human
global inmoov
global weathervar
global walkingThread
#############################################################

# toggle to only load program ab  and skip the inmoov services
startInMoov = False

######################################################################
# helper function help debug the recognized text from webkit/sphinx
######################################################################
def heard(data):
  print "Speech Recognition Data:"+str(data)

######################################################################
#
# MAIN ENTRY POINT  - Start and wire together all the services.
#
######################################################################

# launch the swing gui?
gui = Runtime.createAndStart("gui", "GUIService");

######################################################################
# Create ProgramAB chat bot ( This is the inmoov "brain" )
######################################################################
#neopixel = Runtime.createAndStart("neopixel","Serial")
#neopixel.connect("COM3", 57600, 8, 1, 0)
inmoovWebKit = Runtime.createAndStart("inmoovWebKit", "ProgramAB")
#inmoovWebKit.setPath(aimlPath)
inmoovWebKit.startSession(aimlUserName, aimlBotName)

######################################################################
# Html filter to clean the output from programab.  (just in case)
htmlfilter = Runtime.createAndStart("htmlfilter", "HtmlFilter")

######################################################################
# mouth service, speech synthesis
mouth = Runtime.createAndStart("i01.mouth", "AcapelaSpeech")
#mouth.setVoice(botVoice)
mouth.setVoice(voiceType)
mouth.setLanguage(lang)

######################################################################
# the "ear" of the inmoov TODO: replace this with just base inmoov ear?
ear = Runtime.createAndStart("i01.ear", "WebkitSpeechRecognition")
ear.addListener("publishText", python.name, "heard");
ear.addMouth(mouth)

######################################################################
# MRL Routing webkitspeechrecognition/ear -> program ab -> htmlfilter -> mouth
######################################################################
ear.addTextListener(inmoovWebKit)
inmoovWebKit.addTextListener(htmlfilter)
htmlfilter.addTextListener(mouth)
######################################################################
#Gets the battery level
level = Runtime.getBatteryLevel()
######################################################################
# Start up the inmoov and attach stuff.
######################################################################
i01 = Runtime.create("i01", "InMoov")
##############
head = Runtime.create("i01.head","InMoovHead")
##############
# tweaking default settings of jaw
head.jaw.setMinMax(42,101)
head.jaw.map(0,180,42,101)
head.jaw.setRest(42)
# tweaking default settings of eyes
head.eyeY.map(0,180,85,110)
head.eyeY.setMinMax(0,180)
head.eyeY.setRest(90)
head.eyeX.map(0,180,75,120)
head.eyeX.setMinMax(0,180)
head.eyeX.setRest(90)
head.neck.map(0,180,75,128)
head.neck.setMinMax(0,180)
head.neck.setRest(90)
head.rothead.map(0,180,60,130)
head.rothead.setMinMax(0,180)
head.rothead.setRest(90)
##############
torso = Runtime.create("i01.torso", "InMoovTorso")
# tweaking default torso settings
#torso.topStom.setMaxVelocity(13)
torso.topStom.setMinMax(60,120)
torso.topStom.map(0,180,60,120)
#torso.midStom.setMaxVelocity(13)
torso.midStom.setMinMax(0,180)
torso.midStom.map(0,180,50,130)
#torso.lowStom.setMaxVelocity(13)
#torso.lowStom.setMinMax(0,180)
#torso.lowStom.map(0,180,60,120)
torso.topStom.setRest(90)
torso.midStom.setRest(90)
#torso.lowStom.setRest(90)
##############
leftHand = Runtime.create("i01.leftHand","InMoovHand")
# tweaking default settings of left hand
#leftHand.thumb.setMaxVelocity(250)
leftHand.thumb.setMinMax(0,180)
#leftHand.index.setMaxVelocity(250)
leftHand.index.setMinMax(0,180)
#leftHand.majeure.setMaxVelocity(250)
leftHand.majeure.setMinMax(0,180)
#leftHand.ringFinger.setMaxVelocity(250)
leftHand.ringFinger.setMinMax(0,180)
#leftHand.pinky.setMaxVelocity(250)
leftHand.pinky.setMinMax(0,180)
#leftHand.wrist.setMaxVelocity(250)
leftHand.wrist.setMinMax(0,180)
leftHand.thumb.map(0,180,62,150)
leftHand.index.map(0,180,35,135)
leftHand.majeure.map(0,180,35,180)
leftHand.ringFinger.map(0,180,45,150)
leftHand.pinky.map(0,180,50,170)
leftHand.wrist.map(0,180,40,130)
###############
leftArm = Runtime.create("i01.leftArm","InMoovArm")
#tweak defaults LeftArm
#leftArm.bicep.setMaxVelocity(26)
leftArm.bicep.setMinMax(5,95)
leftArm.bicep.map(0,180,45,140)
#leftArm.rotate.setMaxVelocity(18)
leftArm.rotate.setMinMax(40,180)
leftArm.rotate.map(40,180,60,142)
#leftArm.shoulder.setMaxVelocity(14)
leftArm.shoulder.setMinMax(0,180)
leftArm.shoulder.map(0,180,42,150)
#leftArm.omoplate.setMaxVelocity(15)
leftArm.omoplate.setMinMax(10,82)
leftArm.omoplate.map(0,180,36,135)
################
rightHand = Runtime.create("i01.rightHand","InMoovHand")
# tweaking defaults settings of right hand
#rightHand.thumb.setMaxVelocity(250)
rightHand.thumb.setMinMax(0,180)
#rightHand.index.setMaxVelocity(250)
rightHand.index.setMinMax(0,180)
#rightHand.majeure.setMaxVelocity(250)
rightHand.majeure.setMinMax(0,180)
#rightHand.ringFinger.setMaxVelocity(250)
rightHand.ringFinger.setMinMax(0,180)
#rightHand.pinky.setMaxVelocity(250)
rightHand.pinky.setMinMax(0,180)
#rightHand.wrist.setMaxVelocity(250)
rightHand.wrist.setMinMax(0,180)
rightHand.thumb.map(0,180,64,135)
rightHand.index.map(0,180,42,160)
rightHand.majeure.map(0,180,35,165)
rightHand.ringFinger.map(0,180,40,140)
rightHand.pinky.map(0,180,45,130)
rightHand.wrist.map(0,180,30,135)
#################
rightArm = Runtime.create("i01.rightArm","InMoovArm")
# tweak default RightArm
#rightArm.bicep.setMaxVelocity(26)
rightArm.bicep.setMinMax(5,95)
rightArm.bicep.map(0,180,45,140)
#rightArm.rotate.setMaxVelocity(18)
rightArm.rotate.setMinMax(40,180)
rightArm.rotate.map(40,180,75,130)
#rightArm.shoulder.setMaxVelocity(14)
rightArm.shoulder.setMinMax(0,180)
rightArm.shoulder.map(0,180,42,150)
#rightArm.omoplate.setMaxVelocity(15)
rightArm.omoplate.setMinMax(10,82)
rightArm.omoplate.map(0,180,45,135)
#################
i01 = Runtime.start("i01","InMoov")
i01.setMute(False)
################# 
if startInMoov:
   i01.startAll(leftPort, rightPort)
   #i01.startMouth()
   #i01.startMouthControl(leftPort)
   i01.mouthControl.setmouth(43,95)
#################
   #i01.startEyesTracking(leftPort)
   #i01.startHeadTracking(leftPort)
#################
   #to tweak the default PID values
   i01.eyesTracking.pid.setPID("eyeX",12.0,1.0,0.1)
   i01.eyesTracking.pid.setPID("eyeY",12.0,1.0,0.1)
   i01.headTracking.pid.setPID("rothead",5.0,1.0,0.1)
   i01.headTracking.pid.setPID("neck",5.0,1.0,0.1)
#################
   #i01.startEar()
   #i01.startRightArm(rightPort)
   #i01.startRightHand(rightPort,"atmega2560")
   #i01.startLeftArm(leftPort)
   #i01.startLeftHand(leftPort)
   i01.startTorso("COM20")
#################
   #i01.startPIR("COM20",30)



else:
  i01.mouth = mouth
    
# InMoov has a forward servo, i'm adding
forwardServo = Runtime.start("forwardServo","Servo")
directionServo = Runtime.start("directionServo","Servo")
rollneck = Runtime.start("rollneck","Servo")
right = Runtime.start("i01.right", "Arduino")
right.connect("COM7")


directionServo.attach(right, 24)
forwardServo.attach(right, 26)
rollneck.attach(right,12)
rollneck.setRest(90)
rollneck.moveTo(90)
#################
#Sets FaceRecognizer
#fr=i01.opencv.addFilter("FaceRecognizer")
#lastName=fr.getLastRecognizedName()
#################
##Velocity settings

head.eyeX.setVelocity(0)
head.eyeY.setVelocity(0)

head.neck.setVelocity(0)
head.rothead.setVelocity(0)
head.jaw.setVelocity(0)

torso.topStom.setVelocity(0)
torso.midStom.setVelocity(0)
#torso.lowStom.setVelocity(5)

rightHand.thumb.setVelocity(25)
rightHand.index.setVelocity(25)
rightHand.majeure.setVelocity(25)
rightHand.ringFinger.setVelocity(25)
rightHand.pinky.setVelocity(25)
rightHand.wrist.setVelocity(25)

leftHand.thumb.setVelocity(25)
leftHand.index.setVelocity(25)
leftHand.majeure.setVelocity(25)
leftHand.ringFinger.setVelocity(25)
leftHand.pinky.setVelocity(25)
leftHand.wrist.setVelocity(25)

leftArm.bicep.setVelocity(30)
leftArm.rotate.setVelocity(30)
leftArm.shoulder.setVelocity(30)
leftArm.omoplate.setVelocity(30)

rightArm.bicep.setVelocity(30)
rightArm.rotate.setVelocity(30)
rightArm.shoulder.setVelocity(30)
rightArm.omoplate.setVelocity(30)

######################################################################
# Launch the web gui and create the webkit speech recognition gui
# This service works in Google Chrome only with the WebGui
#################################################################
#webgui = Runtime.create("webgui","WebGui")
webgui.autoStartBrowser(True)
webgui.startService()
BareBonesBrowserLaunch.openURL("http://localhost:8888/#service/i01.ear")

######################################################################
# END MAIN SERVICE SETUP SECTION
######################################################################
if lang=="EN":
   ear.setLanguage("en-EN")
python.subscribe(ear.getName(),"publishText")

######################################################################
# Helper functions and various gesture definitions
######################################################################
i01.loadGestures(gesturesPath)


