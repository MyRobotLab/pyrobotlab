# This script is working 2016-02-22
# It starts the webkitspeechrecognition, the chatbot and the webgui
# Only works with Chrome Browser !!!!
# To connect to the webgui use this link:
# http://<pi ip-address>:8888/#service/webkitspeechrecognition
# Replace <pi ip-address> wityh the ip-address of your PI
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
# Create ProgramAB chat bot
######################################################################
lloyd = Runtime.createAndStart("lloyd", "ProgramAB")
lloyd.startSession("kevin", "alice2")

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
speech = Runtime.createAndStart("speech", "AcapelaSpeech")
speech.setVoice("Will")
######################################################################
# create the mouthcontrol to make the jaw move
######################################################################
arduinoPort = '/dev/ttyACM0'
# Assign PIN numbers
neckPin = 12
jawPin = 11
rightEyePin = 10
leftEyePin = 9
eyeUpDownPin = 8
# Declare min and max values for the neck
neckLeftPos = 128
neckRightPos = 80
# Declare min and max values for the jaw
jawOpen = 120
jawClosed = 90
# Declare min and max values for the eyes
leftEyeMin = 70
leftEyeMax = 120
rightEyeMin = 50
rightEyeMax = 100
# Declare min and max values for the eyes up and down
eyeDownPos = 20
eyeUpPos = 90
neck = Runtime.createAndStart("NeckTurn","Servo")
jaw = Runtime.createAndStart("Jaw","Servo")
eyeLeft = Runtime.createAndStart("eyeLeft","Servo")
eyeRight = Runtime.createAndStart("eyeRight","Servo")
eyeZ = Runtime.createAndStart("eyeZ","Servo")
neck = Runtime.createAndStart("NeckTurn","Servo")
#jaw = Runtime.createAndStart("Jaw","Servo")
eyeLeft = Runtime.createAndStart("eyeLeft","Servo")
eyeRight = Runtime.createAndStart("eyeRight","Servo")
eyeZ = Runtime.createAndStart("eyeZ","Servo")
mouthcontrol= Runtime.createAndStart("mouthcontrol","MouthControl")
arduino = mouthcontrol.getArduino()
arduino.connect(arduinoPort)
jaw = mouthcontrol.getJaw()
jaw.detach()
jaw.attach(arduino,jawPin)
# Assign pins to servos
neck.attach(arduino,neckPin)
jaw.attach(arduino,jawPin)
eyeLeft.attach(arduino,leftEyePin)
eyeRight.attach(arduino,rightEyePin)
eyeZ.attach(arduino,eyeUpDownPin)
# set min and max values for each servo
#jaw.setMinMax(jawClosed,jawOpen)
neck.setMinMax(neckRightPos,neckLeftPos)
eyeLeft.setMinMax(leftEyeMin,leftEyeMax)
eyeRight.setMinMax(rightEyeMin,rightEyeMax)
eyeZ.setMinMax(eyeDownPos,eyeUpPos)
mouthcontrol.setMouth(speech)
mouthcontrol.setmouth(jawClosed,jawOpen)
speech.speakBlocking("Testing to speak")
jaw.moveTo(jawClosed)
sleep(1)
jaw.moveTo(jawOpen)
sleep(1)
jaw.moveTo(jawClosed)
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
# make sure the ear knows if it's speaking.
# TODO: how does this jive with webspeech ?!
# sphinx.attach(mouth)
def neckLeft():
	neck.moveTo(neckLeftPos)
def neckRight():
	neck.moveTo(neckRightPos)
def neckCenter():
	neck.moveTo((neckLeftPos + neckRightPos) / 2)
def leftEyeLeft():
	eyeLeft.moveTo(leftEyeMin)
def leftEyeRight():
	eyeLeft.moveTo(leftEyeMax)
def leftEyeCenter():
	eyeLeft.moveTo((leftEyeMin + leftEyeMax) / 2)
def rightEyeLeft():
	eyeRight.moveTo(rightEyeMin)
def rightEyeRight():
	eyeRight.moveTo(rightEyeMax)
def rightEyeCenter():
	eyeRight.moveTo((rightEyeMin + rightEyeMax) / 2)
def eyeUp():
	eyeZ.moveTo(eyeUpPos)
def eyeDown():
	eyeZ.moveTo(eyeDownPos)
def eyeCenter():
	eyeZ.moveTo((eyeDownPos + eyeUpPos) / 2)
# Start of main program
# Demo
##neckLeft()
##sleep(2)
##neckRight()
##sleep(2)
##neckLeft()
##sleep(2)
##neckRight()
##sleep(2)
neckCenter()
##sleep(2)
eyeCenter()
leftEyeLeft()
rightEyeLeft()
sleep(2)
leftEyeRight()
rightEyeRight()
sleep(2)
leftEyeCenter()
rightEyeCenter()
eyeUp()
sleep(1)
eyeDown()
sleep(1)
eyeCenter()
sleep(1)
leftEyeRight()
rightEyeLeft()
sleep(2)
leftEyeCenter()
rightEyeCenter()
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
# make sure the ear knows if it's speaking.
# TODO: how does this jive with webspeech ?!
# sphinx.attach(mouth)
speech.speakBlocking("Master. I'm here to obey your commands")
