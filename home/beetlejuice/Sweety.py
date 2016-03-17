# Sweety's service
import random
from java.lang import String

comPort = "COM3"
board = "atmega2560"

Runtime.createAndStart("sweety", "Sweety")
sweety.chatBot.startSession("ProgramAB", "sweety", "sweety")


# Add route from webKitSpeechRecognition to Program AB
sweety.ear.addTextListener(sweety.chatBot)
# Add route from Program AB to html filter
sweety.chatBot.addTextListener(sweety.htmlFilter)
# Add route from html filter to mouth
sweety.htmlFilter.addListener("publishText", python.name, "talk");
 
sweety.arduino.setBoard(board)
sweety.connect(comPort)
sleep(1) # give a second to the arduino for connect
sweety.startServos()
sweety.attach()
sweety.posture("neutral")
#sweety.startUltraSonic()
sweety.mouthState("smile")
sleep(1)
# set delays for led sync (delayTime, delayTimeStop, delayTimeLetter)
sweety.setdelays(50,200,50)


def talk(data):
	sweety.mouth.speak(data)
  	print "Saying :", data
  		
def handOpen():
	sweety.rightArm(-1, -1, -1, -1, 75)
	sweety.leftArm(-1, -1, -1, -1, 80)

def handClose():
	sweety.rightArm(-1, -1, -1, -1, 10)
	sweety.leftArm(-1, -1, -1, -1, 150)
def trackFace():
	sweety.startTrack()
	sweety.eyesTracker.opencv.setCameraIndex(0)
	sweety.eyesTracker.findFace()
def stopTracking():
	sweety.stopTrack()
