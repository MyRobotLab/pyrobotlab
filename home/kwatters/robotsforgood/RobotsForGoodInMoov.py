#############################################################
# Robots For Good
# This script runs on MyRobotLab running on a remote InMoov
#############################################################
# Harry is an InMooved powered by a Ras PI2
# Initially we'll start simple
# It will use ProgramAB & Webkit for all interactions with
# the bot.
#############################################################
import threading

# All bot specific hardware configuration goes here.
leftPort = "/dev/ttyACM0"
rightPort = "/dev/ttyACM1"
headPort = leftPort
gesturesPath = "/home/pi/myrobotlab/pyrobotlab/home/kwatters/harry/gestures"

aimlPath = "/home/pi/myrobotlab/pyrobotlab/home/kwatters/harry"
aimlBotName = "harry"
aimlUserName = "Kevin"
botVoice = "Rod"

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
harry = Runtime.createAndStart("harry", "ProgramAB")
harry.setPath(aimlPath)
harry.startSession(aimlUserName, aimlBotName)

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
ear.addTextListener(harry)
harry.addTextListener(htmlfilter)
htmlfilter.addTextListener(mouth)

######################################################################
# Start up the inmoov and attach stuff.
######################################################################
i01 = Runtime.createAndStart("i01", "InMoov")
i01.setMute(True)
if startInMoov:
  left = Runtime.start("i01.left", "Arduino")
  left.connect(leftPort)
  right = Runtime.start("i01.right", "Arduino")
  right.connect(rightPort)
  i01.startHead(headPort);
  # print "Left Port: " + leftPort + " Right Port : " + rightPort + " Head Port: " + headPort
  i01.startAll(leftPort, rightPort)
  # calibrate harry specific stuff. 
  i01.head.rothead.detach()
  i01.head.neck.detach()
  i01.head.rothead.setController("i01.right")
  i01.head.neck.setController("i01.right")
  i01.head.rothead.attach()
  i01.head.neck.attach()  
  
else:
  i01.mouth = mouth
    
# Harry doesn't have a forward servo, but i'm adding it here as a 
# place holder
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
# Start the remote adapter and tell it to start listening. 
######################################################################
remote = Runtime.createAndStart("remote", "RemoteAdapter")
remote.startListening()

### Load the python gestures for harry.
i01.loadGestures(gesturesPath)

