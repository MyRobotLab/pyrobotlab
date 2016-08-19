#file : this is Zoooorba
# this will run with versions of MRL above 1695
# a very minimal script for InMoov
# although this script is very short you can still
# do voice control of a right hand or finger box
# It uses WebkitSpeechRecognition, so you need to use Chrome as your default browser for this script to work
import random
import threading
import itertools


webgui = Runtime.create("WebGui","WebGui")
webgui.autoStartBrowser(False)
webgui.startService()
# Then start the browsers and show the WebkitSpeechRecognition service named i01.ear
webgui.startBrowser("http://localhost:8888/#/service/i01.ear")

# As an alternative you can use the line below to show all services in the browser. In that case you should comment out all lines above that starts with webgui. 
# webgui = Runtime.createAndStart("webgui","WebGui")

# Change to the port that you use
rightPort = "/dev/ttyACM0"

i01 = Runtime.createAndStart("i01", "InMoov")
i01.startEar()

# starting parts
i01.startMouth()
#to tweak the default voice
i01.mouth.setVoice("WillBadGuy")

############################################################
 
helvar = 1


##############
i01.startRightHand(rightPort)
# tweaking defaults settings of right hand
i01.rightHand.thumb.setMinMax(20,155)
i01.rightHand.wrist.setMinMax(20,165)
i01.rightHand.index.setMinMax(35,150)
i01.rightHand.majeure.setMinMax(38,150)
i01.rightHand.ringFinger.setMinMax(30,170)
i01.rightHand.pinky.setMinMax(20,150)
i01.rightHand.thumb.map(0,180,20,155)
i01.rightHand.wrist.map(0,180,20,165)
i01.rightHand.index.map(0,180,30,130)
i01.rightHand.majeure.map(0,180,38,150)
i01.rightHand.ringFinger.map(0,180,30,170)
i01.rightHand.pinky.map(0,180,30,150)
#################

# currently attached servos
#i01.detach()
#i01.attach()

# verbal commands
ear = i01.ear

ear.addCommand("connect", "i01.rightHand", "attach")
ear.addCommand("disconnect", "i01.rightHand", "detach")
ear.addCommand("rest", i01.getName(), "rest")
ear.addCommand("open", "python", "handopen")
ear.addCommand("close", "python", "handclose")
ear.addCommand("capture gesture", ear.getName(), "captureGesture")
ear.addCommand("manual", ear.getName(), "lockOutAllGrammarExcept", "voice control")
ear.addCommand("voice control", ear.getName(), "clearLock")

ear.addCommand("say goodbye", "python", "waveGoodbye")
ear.addCommand("how are you", "python", "howareyou")
ear.addCommand("hello", "python", "hello")

# Confirmations and Negations are not supported yet in WebkitSpeechRecognition
# So commands will execute immediatley
ear.addComfirmations("yes","correct","yeah","ya")
ear.addNegations("no","wrong","nope","nah")

ear.startListening()


def handopen():
  i01.moveHand("right",0,0,0,0,0)
  i01.mouth.speak("Hands open, come closer, come closer")
  
def waveGoodbye():
  i01.mouth.speak("you moron, i need the rest of the arm first")
  
def howareyou():
  i01.mouth.speak("It's a bit hot, i need some fresh beverage, maybe some blood with a bit of lemon")  

def handclose():
  i01.moveHand("right",180,180,180,180,180)
  i01.mouth.speak("Hands closed, on your neck....")
  
def hello():
  if helvar <= 1:    
    i01.mouth.speak("hello")
    global helvar
    helvar += 1
  elif helvar == 2:
    i01.mouth.speak("you have already said that")
    helvar += 1
  elif helvar == 3:
    i01.mouth.speak("you are starting to annoy me...hmmm")
    helvar += 1
  elif helvar == 4:
    i01.mouth.speak("you are so lucky i don't have more then an arm")
  
  
       
  
  

