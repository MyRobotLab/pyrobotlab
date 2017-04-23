from java.lang import String
import threading
import socket

#############################################################
# This is the Pinocchio script
# Initially we'll start simple
# It will use ProgramAB & Webkit for all interactions with
# the bot.
#############################################################
# All bot specific hardware configuration goes here.
pcName = socket.gethostname()
if (pcName == "Christian-PC"):
  basePath = "D:\Users\Christian\Desktop\InMoov"
  leftPort = "COM22"
  rightPort = "COM3"
elif (pcName == "Samsung"):
  basePath = "C:\Users\chris_000\Desktop\InMoov"
  leftPort = "COM20"
  rightPort = "COM3"
elif (pcName == "raspberrypi"):
  basePath = "/mnt/InMoov"
  leftPort = "/dev/ttyUSB0"
  rightPort = "/dev/ttyUSB1"
  
headPort = leftPort

gesturesPath = basePath + "\mrl-script\pinocchio\gestures"
initPath = basePath + "\mrl-script\pinocchio\init"
wikiDataPath = basePath + "\mrl-script\pinocchio\wikidata"
aimlPath = basePath + ""

aimlBotName = "pinocchio"
aimlUserName = "Christian"
botVoiceFrench = "Bruno"
botVoiceEnglish = "Will"
botVoice = botVoiceEnglish

joystickId = 3

# toggle to only load program ab  and skip the inmoov services
startInMoov = True

######################################################################
# helper function help debug the recognized text from webkit/sphinx
######################################################################
def heard(data):
  print ""#"Speech Recognition Data:"+str(data)

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
pinocchio = Runtime.createAndStart("pinocchio", "ProgramAB")
pinocchio.setPath(aimlPath)
pinocchio.startSession(aimlUserName, aimlBotName)

######################################################################
# Html filter to clean the output from programab.  (just in case)
htmlfilter = Runtime.createAndStart("htmlfilter", "HtmlFilter")

######################################################################
# mouth service, speech synthesis
mouth = Runtime.createAndStart("i01.mouth", "VoiceRss")
mouth.setKey("***")
mouth.setLanguage("en-gb")
mouth.setRate(0)
#mouth.setVoice(botVoice)

######################################################################
# the "ear" of the inmoov TODO: replace this with just base inmoov ear?
ear = Runtime.createAndStart("i01.ear", "WebkitSpeechRecognition")
ear.addListener("publishText", python.name, "heard");
ear.addMouth(mouth)

######################################################################
# MRL Routing webkitspeechrecognition/ear -> program ab -> htmlfilter -> mouth
######################################################################
ear.addTextListener(pinocchio)
pinocchio.addTextListener(htmlfilter)
htmlfilter.addTextListener(mouth)

######################################################################
# Start up the inmoov and attach stuff.
######################################################################
i01 = Runtime.createAndStart("i01", "InMoov")
i01.setMute(True)
if startInMoov:
  #i01.startAll(leftPort, rightPort)
  i01.startMouth()
  i01.startMouthControl(leftPort)
  i01.head.jaw.map(0,180,60,90)
  i01.mouthControl.setmouth(60,90)
  i01.head.jaw.setRest(90)
  i01.head.jaw.setVelocity(100)
  i01.head.neck.map(0,180,20,160)
  i01.head.neck.setRest(90)
  i01.head.neck.setVelocity(185)
  i01.head.neck.setMaxVelocity(185)
  i01.head.rothead.map(0,180,0,180)
  i01.head.rothead.setRest(90)
  i01.head.rothead.setVelocity(210)
  i01.head.rothead.setMaxVelocity(210)
  i01.head.eyeY.setMinMax(85,150)
  #i01.head.eyeY.map(0,180,80,100)
  i01.head.eyeY.setRest(115)
  i01.head.eyeX.setMinMax(75,115)
  #i01.head.eyeX.map(0,180,70,100)
  i01.head.eyeX.setRest(95)
  i01.ear = ear
  i01.head.rest()
  #i01.beginCheckingOnInactivity(120)
  #i01.startPIR(leftPort,23)
else:
  i01.mouth = mouth
    
######################################################################
# Launch the web gui and create the webkit speech recognition gui
# This service works in Google Chrome only with the WebGui
#################################################################
#webgui=Runtime.create("WebGui","WebGui")
#webgui.autoStartBrowser(False)
#webgui.startService()

######################################################################
# END MAIN SERVICE SETUP SECTION
######################################################################


######################################################################
# Helper functions and various gesture definitions
######################################################################
language = "english"
i01.loadGestures(initPath)
i01.loadGestures(gesturesPath)

sleep(3)

startAll()
pinocchio.getResponse("hello");
#pinocchio.getResponse("start in move")
#startIK3D() 

i01.startVinMoov()
i01.startIntegratedMovement()
