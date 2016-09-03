from java.lang import String
import threading
import time
import random
import subprocess
from org.myrobotlab.net import BareBonesBrowserLaunch 

#############################################################
# This is the InMoov script
# InMoov is powered by MyRobotLab
# Initially we'll start simple
# It will use ProgramAB & Webkit for all interactions with
# the bot.
#############################################################
# All bot specific hardware configuration goes here.
leftPort = "COM20"
rightPort = "COM7"
headPort = leftPort

gesturesPath = "C:\Myrobotlab\ProgramAB bots\gestures"

aimlPath = "C:/Myrobotlab/myrobotlab.1.0.1653/develop/ProgramAB"
aimlBotName = "inmoovWebKit"
aimlUserName = "Gael"
botVoice = "Ryan"

# toggle to only load program ab  and skip the inmoov services
startInMoov = True

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
# gui = Runtime.createAndStart("gui", "GUIService");

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
mouth.setVoice(botVoice)

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
# Sets the face recognizer
######################################################################
#opencv=Runtime.start("opencv","OpenCV")
#opencv.setCameraIndex(1)
#fr=opencv.addFilter("FaceRecognizer")
#lastName=fr.getLastRecognizedName()
######################################################################
# Start up the inmoov and attach stuff.
######################################################################
i01 = Runtime.create("i01", "InMoov")
##############
head = Runtime.create("i01.head","InMoovHead")
##############
# tweaking default settings of jaw
head.jaw.setMinMax(43,101)
head.jaw.map(0,180,43,101)
head.jaw.setRest(43)
# tweaking default settings of eyes
head.eyeY.map(0,180,105,65)
head.eyeY.setMinMax(0,180)
head.eyeY.setRest(90)
head.eyeX.map(0,180,100,55)
head.eyeX.setMinMax(0,180)
head.eyeX.setRest(90)
#head.neck.setMaxVelocity(185)
head.neck.map(0,180,105,55)
head.neck.setMinMax(0,180)
head.neck.setRest(90)
#head.rothead.setMaxVelocity(210)
head.rothead.map(0,180,60,130)
head.rothead.setMinMax(0,180)
head.rothead.setRest(90)
##############
torso = Runtime.create("i01.torso", "InMoovTorso")
# tweaking default torso settings
#torso.topStom.setMaxVelocity(13)
torso.topStom.setMinMax(60,120)
torso.topStom.map(0,180,45,140)
#torso.midStom.setMaxVelocity(13)
torso.midStom.setMinMax(0,180)
torso.midStom.map(0,180,60,120)
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
leftHand.majeure.map(0,180,40,180)
leftHand.ringFinger.map(0,180,45,150)
leftHand.pinky.map(0,180,50,170)
leftHand.wrist.map(0,180,45,135)
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
leftArm.shoulder.map(0,180,42,145)
#leftArm.omoplate.setMaxVelocity(15)
leftArm.omoplate.setMinMax(10,82)
leftArm.omoplate.map(0,180,36,128)
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
rightHand.majeure.map(0,180,45,165)
rightHand.ringFinger.map(0,180,40,140)
rightHand.pinky.map(0,180,45,130)
rightHand.wrist.map(0,180,40,135)
#################
rightArm = Runtime.create("i01.rightArm","InMoovArm")
# tweak default RightArm
#rightArm.bicep.setMaxVelocity(26)
rightArm.bicep.setMinMax(5,95)
rightArm.bicep.map(0,180,45,140)
#rightArm.rotate.setMaxVelocity(18)
rightArm.rotate.setMinMax(40,180)
rightArm.rotate.map(40,180,60,142)
#rightArm.shoulder.setMaxVelocity(14)
rightArm.shoulder.setMinMax(0,180)
rightArm.shoulder.map(0,180,42,145)
#rightArm.omoplate.setMaxVelocity(15)
rightArm.omoplate.setMinMax(10,82)
rightArm.omoplate.map(0,180,45,128)
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
   i01.eyesTracking.pid.setPID("eyeX",45.0,1.0,0.1)
   i01.eyesTracking.pid.setPID("eyeY",45.0,1.0,0.1)
   i01.headTracking.pid.setPID("rothead",15.0,1.0,0.2)
   i01.headTracking.pid.setPID("neck",35.0,1.0,0.2)
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
#################
fr=i01.opencv.addFilter("FaceRecognizer")
lastName=fr.getLastRecognizedName()
#################
##Velocity settings
head.neck.setMaxVelocity(12)
head.rothead.setMaxVelocity(12)

torso.topStom.setMaxVelocity(5)
torso.midStom.setMaxVelocity(5)
#torso.lowStom.setMaxVelocity(5)

rightHand.thumb.setMaxVelocity(15)
rightHand.index.setMaxVelocity(15)
rightHand.majeure.setMaxVelocity(15)
rightHand.ringFinger.setMaxVelocity(15)
rightHand.pinky.setMaxVelocity(15)
rightHand.wrist.setMaxVelocity(15)

leftHand.thumb.setMaxVelocity(15)
leftHand.index.setMaxVelocity(15)
leftHand.majeure.setMaxVelocity(15)
leftHand.ringFinger.setMaxVelocity(15)
leftHand.pinky.setMaxVelocity(15)
leftHand.wrist.setMaxVelocity(15)

leftArm.bicep.setMaxVelocity(26)
leftArm.rotate.setMaxVelocity(18)
leftArm.shoulder.setMaxVelocity(14)
leftArm.omoplate.setMaxVelocity(15)

rightArm.bicep.setMaxVelocity(26)
rightArm.rotate.setMaxVelocity(18)
rightArm.shoulder.setMaxVelocity(14)
rightArm.omoplate.setMaxVelocity(15)

######################################################################
# Launch the web gui and create the webkit speech recognition gui
# This service works in Google Chrome only with the WebGui
#################################################################
#webgui = Runtime.create("webgui","WebGui")
webgui.autoStartBrowser(False)
webgui.startService()
BareBonesBrowserLaunch.openURL("http://localhost:8888/#service/i01.ear")

######################################################################
# END MAIN SERVICE SETUP SECTION
######################################################################


######################################################################
# Helper functions and various gesture definitions
######################################################################
i01.loadGestures(gesturesPath)


