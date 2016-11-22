from java.lang import String
 
######################################################################
# A helper function to print the recognized text to the python window.
# semi-useful for debugging.
######################################################################
def heard(data):
  print "Speech Recognition Data:", data

######################################################################
# Create and Start Logging
######################################################################
log = Runtime.createAndStart("Log","Log")  

######################################################################
# Create ProgramAB chat bot
######################################################################
aimlPath = "C:/github/pyrobotlab/home/brotherbrown831/inmoov"
marvin = Runtime.createAndStart("marvin", "ProgramAB")
marvin.setPath(aimlPath)
# this starts a session between username "nolan" and the chat bot named
# "marvin"  (AIML for the bots are in the develop/ProgramAB/bots directory.
marvin.startSession("nolan", "marvin")

######################################################################
# create the speech recognition service
# Speech recognition is based on WebSpeechToolkit API
######################################################################
# Start the new WebGuiREST API for MRL
webgui = Runtime.create("webgui","WebGui")
webgui.autoStartBrowser(True)
webgui.startService()
# Then start the browsers and show the WebkitSpeechRecognition service named i01.ear
webgui.startBrowser("http://localhost:8888/#/service/webkitspeechrecognition")

######################################################################
# Create the webkit speech recognition gui
# This service works in Google Chrome only with the WebGui
######################################################################
wksr = Runtime.createAndStart("webkitspeechrecognition", "WebkitSpeechRecognition")
######################################################################
# create the html filter to filter the output of program ab
# this service will strip out any html markup and return only the text
# from the output of ProgramAB
######################################################################
htmlfilter = Runtime.createAndStart("htmlfilter", "HtmlFilter")
 
######################################################################
# create the speech to text service (named the same as the marvin's)
# This service will listen to the output from the htmlfilter and
# call out to the Acapela group to get the an MP3 that represents the
# text to be spoken.  That mp3 will be played back by an AudioFile 
# service.
######################################################################
mouth = Runtime.createAndStart("i01.mouth", "AcapelaSpeech")

# debugging in python route.
# wksr.addListener("publishText", python.name, "heard", String().getClass());

######################################################################
# MRL Routing webkitspeechrecognition -> program ab -> htmlfilter -> mouth
######################################################################
# add a link between the webkit speech to publish text to ProgramAB
wksr.addTextListener(marvin)
# Add route from Program AB to publish text to the html filter
marvin.addTextListener(htmlfilter)
# Add route to publish text from html filter to mouth
htmlfilter.addTextListener(mouth)



######################################################################
# Physical Components
######################################################################
leftPort = "COM8"

i01 = Runtime.createAndStart("i01", "InMoov")
i01.startEar()

# starting parts
i01.startMouth()
mouth = i01.mouth
i01.startMouthControl(leftPort)
#to tweak the default voice
i01.mouth.setVoice("Ryan")
##############
i01.startHead(leftPort)
##############
# tweaking default settings of Head
#i01.head.jaw.setMinMax(43,101)
i01.head.jaw.map(0,180,43,101)
#i01.mouthControl.setmouth(10,170)
#i01.head.jaw.setRest(43)
# tweaking default settings of eyes
#i01.head.eyeY.setMinMax(63,107)
#i01.head.eyeY.map(0,180,107,63)
#i01.head.eyeY.setRest(90)
#i01.head.eyeX.setMinMax(64,105)
#i01.head.eyeX.map(0,180,105,64)
#i01.head.eyeX.setRest(90)
i01.head.neck.setMinMax(55,105)
i01.head.neck.map(0,180,105,55)
i01.head.neck.setRest(70)
#i01.head.rothead.setMinMax(45,135)
#i01.head.rothead.map(0,180,45,135)
#i01.head.rothead.setRest(86)
#################
