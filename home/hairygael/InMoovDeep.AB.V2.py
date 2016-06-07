from java.lang import String
import threading

#############################################################
# This is the InMoov script
# InMoov is powered by a MyRobotLab
# Initially we'll start simple
# It will use ProgramAB & Webkit for all interactions with
# the bot.
#############################################################
# All bot specific hardware configuration goes here.
leftPort = "COM20"
rightPort = "COM7"
headPort = leftPort

gesturesPath = "C:\Myrobotlab\ProgramAB bots\gestures"

aimlPath = "C:/Myrobotlab/myrobotlab.1.0.1394/develop/ProgramAB"
aimlBotName = "inmoov"
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
inmoov = Runtime.createAndStart("inmoov", "ProgramAB")
#harry.setPath(aimlPath)
inmoov.startSession(aimlUserName, aimlBotName)

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
ear.addTextListener(inmoov)
inmoov.addTextListener(htmlfilter)
htmlfilter.addTextListener(mouth)

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
head.eyeY.setMinMax(10,175)
head.eyeY.map(0,180,105,63)
head.eyeY.setRest(90)
head.eyeX.setMinMax(10,175)
head.eyeX.map(0,180,95,60)
head.eyeX.setRest(90)
head.neck.setMinMax(0,180)
head.neck.map(0,180,105,55)
head.neck.setRest(90)
head.rothead.setMinMax(0,180)
head.rothead.map(0,180,45,135)
head.rothead.setRest(90)
##############
torso = Runtime.create("i01.torso", "InMoovTorso")
# tweaking default torso settings
torso.topStom.setMinMax(0,180)
torso.topStom.map(0,180,70,120)
torso.midStom.setMinMax(0,180)
torso.topStom.map(0,180,60,120)
#torso.lowStom.setMinMax(0,180)
torso.topStom.setRest(110)
#torso.midStom.setRest(90)
#torso.lowStom.setRest(90)
##############
leftHand = Runtime.create("i01.leftHand","InMoovHand")
# tweaking default settings of left hand
leftHand.thumb.setMinMax(0,180)
leftHand.index.setMinMax(0,180)
leftHand.majeure.setMinMax(0,180)
leftHand.ringFinger.setMinMax(0,180)
leftHand.pinky.setMinMax(0,180)
leftHand.wrist.setMinMax(0,180)
##leftHand.thumb.map(0,180,45,140)
##leftHand.index.map(0,180,40,140)
##leftHand.majeure.map(0,180,30,176)
##leftHand.ringFinger.map(0,180,25,175)
##leftHand.pinky.map(0,180,15,112)
leftHand.wrist.map(0,180,40,135)
###############
leftArm = Runtime.create("i01.leftArm","InMoovArm")
#tweak defaults LeftArm
leftArm.bicep.setMinMax(5,90)
leftArm.bicep.map(0,180,48,100)
leftArm.rotate.setMinMax(40,180)
leftArm.rotate.map(0,180,45,135)
leftArm.shoulder.setMinMax(0,180)
leftArm.shoulder.map(0,180,52,155)
leftArm.omoplate.setMinMax(10,85)
leftArm.omoplate.map(0,180,45,135)
################
rightHand = Runtime.create("i01.rightHand","InMoovHand")
# tweaking defaults settings of right hand
rightHand.thumb.setMinMax(0,180)
rightHand.index.setMinMax(0,180)
rightHand.majeure.setMinMax(0,180)
rightHand.ringFinger.setMinMax(0,180)
rightHand.wrist.setMinMax(0,180)
rightHand.pinky.setMinMax(0,180)
rightHand.thumb.map(0,180,64,135)
rightHand.index.map(0,180,42,160)
rightHand.majeure.map(0,180,41,180)
rightHand.ringFinger.map(0,180,5,145)
rightHand.pinky.map(0,180,50,130)
rightHand.wrist.map(0,180,40,135)
#################
rightArm = Runtime.create("i01.rightArm","InMoovArm")
# tweak default RightArm
#rightArm.bicep.setMinMax(5,90)
rightArm.bicep.map(0,180,48,100)
#rightArm.rotate.setMinMax(40,180)
rightArm.rotate.map(0,180,45,135)
#rightArm.shoulder.setMinMax(0,180)
rightArm.shoulder.map(0,180,45,135)
rightArm.omoplate.setMinMax(10,85)
rightArm.omoplate.map(0,180,45,135)
#################
i01 = Runtime.start("i01","InMoov")
i01.setMute(False)
if startInMoov:
   i01.startAll(leftPort, rightPort)
   #i01.startMouth()
   #i01.startMouthControl(leftPort)
   i01.mouthControl.setmouth(43,95)
################
   #i01.startEyesTracking(leftPort)
   #i01.startHeadTracking(leftPort)
#################
   #to tweak the default PID values
   i01.eyesTracking.pid.setPID("eyeX",45.0,1.0,0.1)
   i01.eyesTracking.pid.setPID("eyeY",45.0,1.0,0.1)
   i01.headTracking.pid.setPID("rothead",15.0,1.0,0.2)
   i01.headTracking.pid.setPID("neck",35.0,1.0,0.2)
##############
   #i01.startEar()
   #i01.startRightArm(rightPort)
   #i01.startRightHand(rightPort,"atmega2560")
   #i01.startLeftArm(leftPort)
   #i01.startLeftHand(leftPort)
   #i01.startTorso("COM20")
##############
   #i01.startPIR("COM20",30)


else:
  i01.mouth = mouth
    
# InMoov has a forward servo, i'm adding
forwardServo = Runtime.start("forwardServo","Servo")

######################################################################
# Launch the web gui and create the webkit speech recognition gui
# This service works in Google Chrome only with the WebGui
#################################################################
webgui = Runtime.createAndStart("webgui","WebGui")

######################################################################
# END MAIN SERVICE SETUP SECTION
######################################################################


######################################################################
# Helper functions and various gesture definitions
######################################################################
i01.loadGestures(gesturesPath)


