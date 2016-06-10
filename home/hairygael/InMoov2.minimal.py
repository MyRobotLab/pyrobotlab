#file : InMoov2.minimal.py

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
rightPort = "COM4"

i01 = Runtime.createAndStart("i01", "InMoov")
i01.startEar()

# starting parts
i01.startMouth()
#to tweak the default voice
i01.mouth.setVoice("Ryan")
##############
i01.startRightHand(rightPort)
# tweaking defaults settings of right hand
#i01.rightHand.thumb.setMinMax(55,135)
#i01.rightHand.index.setMinMax(0,160)
#i01.rightHand.majeure.setMinMax(0,140)
#i01.rightHand.ringFinger.setMinMax(48,145)
#i01.rightHand.pinky.setMinMax(45,146)
#i01.rightHand.thumb.map(0,180,55,135)
#i01.rightHand.index.map(0,180,0,160)
#i01.rightHand.majeure.map(0,180,0,140)
#i01.rightHand.ringFinger.map(0,180,48,145)
#i01.rightHand.pinky.map(0,180,45,146)
#################

# verbal commands
ear = i01.ear

ear.addCommand("attach right hand", "i01.rightHand", "attach")
ear.addCommand("disconnect right hand", "i01.rightHand", "detach")
ear.addCommand("rest", i01.getName(), "rest")
ear.addCommand("open hand", "python", "handopen")
ear.addCommand("close hand", "python", "handclose")
ear.addCommand("capture gesture", ear.getName(), "captureGesture")
ear.addCommand("manual", ear.getName(), "lockOutAllGrammarExcept", "voice control")
ear.addCommand("voice control", ear.getName(), "clearLock")

# Confirmations and Negations are not supported yet in WebkitSpeechRecognition
# So commands will execute immediatley
ear.addComfirmations("yes","correct","yeah","ya")
ear.addNegations("no","wrong","nope","nah")

ear.startListening()
i01.righthand.attach()

def handopen():
  i01.moveHand("left",0,0,0,0,0)
  i01.moveHand("right",0,0,0,0,0)

def handclose():
  i01.moveHand("left",180,180,180,180,180)
  i01.moveHand("right",180,180,180,180,180)
