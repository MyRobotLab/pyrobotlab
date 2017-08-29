#file : InMoov3.minimalHead.py

# this will run with versions of MRL above 1695
# a very minimal script for InMoov
# although this script is very short you can still
# do voice control of a right hand or finger box
# It uses WebkitSpeechRecognition, so you need to use Chrome as your default browser for this script to work

# Start the webgui service without starting the browser
webgui = Runtime.create("WebGui","WebGui")
webgui.autoStartBrowser(False)
webgui.startService()
# Then start the browsers and show the WebkitSpeechRecognition service named i01.ear
webgui.startBrowser("http://localhost:8888/#/service/i01.ear")

# As an alternative you can use the line below to show all services in the browser. In that case you should comment out all lines above that starts with webgui. 
# webgui = Runtime.createAndStart("webgui","WebGui")

# Change to the port that you use
leftPort = "COM8"

#aimlPath = ""
aimlUserName = "Nolan"
aimlBotName = "inmoovWebKit"

inmoovWebKit = Runtime.createAndStart("inmoovWebKit", "ProgramAB")
#inmoovWebKit.setPath(aimlPath)
inmoovWebKit.startSession(aimlUserName, aimlBotName)

######################################################################
# Html filter to clean the output from programab.  (just in case)
htmlfilter = Runtime.createAndStart("htmlfilter", "HtmlFilter")

######################################################################

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
#i01.head.jaw.map(0,180,43,101)
#i01.mouthControl.setmouth(43,95)
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
i01.startEyesTracking(leftPort)
i01.startHeadTracking(leftPort)
############################################################
#to tweak the default PID values
i01.eyesTracking.xpid.setPID(25.0,5.0,0.1)
i01.eyesTracking.ypid.setPID(25.0,5.0,0.1)
i01.headTracking.xpid.setPID(15.0,5.0,0.2)
i01.headTracking.ypid.setPID(15.0,5.0,0.2)
############################################################

# verbal commands
ear = i01.ear
ear.attach(mouth)
 
ear.addCommand("rest", "python", "rest")

######################################################################
# MRL Routing webkitspeechrecognition/ear -> program ab -> htmlfilter -> mouth
######################################################################
ear.addTextListener(inmoovWebKit)
inmoovWebKit.addTextListener(htmlfilter)
htmlfilter.addTextListener(mouth)
######################################################################

# Confirmations and Negations are not supported yet in WebkitSpeechRecognition
# So commands will execute immediatley
ear.addComfirmations("yes","correct","yeah","ya")
ear.addNegations("no","wrong","nope","nah")

ear.startListening()

# set up a message route from the ear --to--> python method "heard"
ear.addListener("recognized", "python", "heard")
inmoov.addTextListener(i01.mouth)


def lookrightside():
  i01.setHeadSpeed(0.70, 0.70)
  i01.moveHead(85,40)

def lookrightside():
  i01.setHeadSpeed(0.70, 0.70)
  i01.moveHead(85,40)

def lookinmiddle():
  i01.setHeadSpeed(0.70, 0.70)
  i01.moveHead(85,86)




