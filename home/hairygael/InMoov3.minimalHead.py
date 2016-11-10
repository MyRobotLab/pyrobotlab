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
leftPort = "COM20"

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
#i01.head.neck.setMinMax(55,105)
#i01.head.neck.map(0,180,105,55)
#i01.head.neck.setRest(70)
#i01.head.rothead.setMinMax(45,135)
#i01.head.rothead.map(0,180,45,135)
#i01.head.rothead.setRest(86)
#################
i01.startEyesTracking(leftPort)
i01.startHeadTracking(leftPort)
############################################################
#to tweak the default PID values
i01.eyesTracking.pid.setPID("eyeX",12.0,1.0,0.1)
i01.eyesTracking.pid.setPID("eyeY",12.0,1.0,0.1)
i01.headTracking.pid.setPID("rothead",5.0,1.0,0.1)
i01.headTracking.pid.setPID("neck",5.0,1.0,0.1)
############################################################

# verbal commands
ear = i01.ear
ear.attach(mouth)
 
ear.addCommand("rest", "python", "rest")

ear.addCommand("attach head", "i01.head", "attach")
ear.addCommand("disconnect head", "i01.head", "detach")
ear.addCommand("attach eyes", "i01.head.eyeY", "attach")
ear.addCommand("disconnect eyes", "i01.head.eyeY", "detach")
ear.addCommand("capture gesture", ear.getName(), "captureGesture")
ear.addCommand("manual", ear.getName(), "lockOutAllGrammarExcept", "voice control")
ear.addCommand("voice control", ear.getName(), "clearLock")

ear.addCommand("search humans", "python", "trackHumans")
ear.addCommand("quit search", "python", "stopTracking")
ear.addCommand("track", "python", "trackPoint")
ear.addCommand("freeze track", "python", "stopTracking")

ear.addCommand("look on your right side", "python", "lookrightside")
ear.addCommand("look on your left side", "python", "lookleftside")
ear.addCommand("look in the middle", "python", "lookinmiddle")

# Confirmations and Negations are not supported yet in WebkitSpeechRecognition
# So commands will execute immediatley
ear.addComfirmations("yes","correct","yeah","ya")
ear.addNegations("no","wrong","nope","nah")

ear.startListening()

# set up a message route from the ear --to--> python method "heard"
ear.addListener("recognized", "python", "heard")
#inmoov.addTextListener(i01.mouth)


def lookrightside():
  i01.setHeadSpeed(0.70, 0.70)
  i01.moveHead(85,40)

def lookrightside():
  i01.setHeadSpeed(0.70, 0.70)
  i01.moveHead(85,40)

def lookinmiddle():
  i01.setHeadSpeed(0.70, 0.70)
  i01.moveHead(85,86)

def trackHumans():
  i01.headTracking.faceDetect()
  i01.eyesTracking.faceDetect()
  fullspeed()

def trackPoint():
  i01.headTracking.startLKTracking()
  i01.eyesTracking.startLKTracking()
  fullspeed()

def stopTracking():
  i01.headTracking.stopTracking()
  i01.eyesTracking.stopTracking()




