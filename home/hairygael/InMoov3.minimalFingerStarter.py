#file : InMoov3.minimalFingerStarter.py

# this will run with versions of MRL above 1695
# a very minimal script for InMoov
# although this script is very short you can still
# do voice control of a finger starter
# It uses WebkitSpeechRecognition, so you need to use Chrome as your default browser for this script to work
#The Finger Starter is considered here to be right index, 
#so make sure your servo is connected to pin3 of you Arduino

# Start the webgui service without starting the browser
webgui = Runtime.create("WebGui","WebGui")
webgui.autoStartBrowser(False)
webgui.startService()
# Then start the browsers and show the WebkitSpeechRecognition service named i01.ear
webgui.startBrowser("http://localhost:8888/#/service/i01.ear")

# As an alternative you can use the line below to show all services in the browser. In that case you should comment out all lines above that starts with webgui. 
# webgui = Runtime.createAndStart("webgui","WebGui")

# Change to the port that you use
rightPort = "COM4"

i01 = Runtime.createAndStart("i01", "InMoov")
i01.startEar()

# starting parts
i01.startMouth()
#to tweak the default voice
i01.mouth.setVoice("Ryan")
##############

# verbal commands
ear = i01.ear

ear.addCommand("attach finger", "i01.rightHand.Index", "attach")
ear.addCommand("disconnect finger", "i01.rightHand.Index", "detach")
ear.addCommand("rest", i01.getName(), "rest")
ear.addCommand("open finger", "python", "fingeropen")
ear.addCommand("close finger", "python", "fingerclose")
ear.addCommand("finger to the middle", "python", "fingermiddle")
ear.addCommand("capture gesture", ear.getName(), "captureGesture")
ear.addCommand("manual", ear.getName(), "lockOutAllGrammarExcept", "voice control")
ear.addCommand("voice control", ear.getName(), "clearLock")

# Confirmations and Negations are not supported yet in WebkitSpeechRecognition
# So commands will execute immediatley 
ear.addComfirmations("yes","correct","yeah","ya") 
ear.addNegations("no","wrong","nope","nah")

ear.startListening()
i01.startRightHand(rightPort)

def fingeropen():
  i01.moveHand("right",0,0,0,0,0)

def fingerclose():
  i01.moveHand("right",180,180,180,180,180)

def fingermiddle():
  i01.moveHand("right",90,90,90,90,90)
