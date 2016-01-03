# Sweety's service
import random


Runtime.createAndStart("sweety", "Sweety")
sweety.arduino.setBoard("atmega2560")
sweety.connect("COM8")
sleep(1) # give a second to the arduino for connect
sweety.attach()
sweety.startPosition()
#sweety.startUltraSonic()
sweety.startTrack()
sweety.mouthState("smile")
sleep(1)
# set delays for led sync (delayTime, delayTimeStop, delayTimeLetter)
sweety.setdelays(50,200,50)
sweety.mouth.setLanguage("en")
sweety.saying("Hello,my name is sweety.")



sweety.ear.addCommand("open hand", "python", "handOpen")
sweety.ear.addCommand("close hand", "python", "handClose")
sweety.ear.addCommand("track face", "python", "trackFace")
sweety.ear.addCommand("stop tracking", "python", "stopTracking")


sweety.ear.startListening("hello | goodbye") #  | open hand | close hand
 
# set up a message route from the ear --to--> python method "heard"
sweety.ear.addListener("recognized", "python", "heard")
 
def heard(data):
	
	if (data == "hello"):
		x = (random.randint(1, 3))
		if x == 1:
			sweety.saying("hello")
		if x == 2:
			sweety.saying("hi")
		if x == 3:
			sweety.saying("nice to meet you")

	if (data == "goodbye"):
		x = (random.randint(1, 3))
		if x == 1:
			sweety.saying("bye")
		if x == 2:
			sweety.saying("see you later")
		if x == 3:
			sweety.saying("have a nice day")

		
def handOpen():
	sweety.rightArm(-1, -1, -1, -1, 75)
	sweety.leftArm(-1, -1, -1, -1, 80)
	sweety.saying("my hands are open")

def handClose():
	sweety.rightArm(-1, -1, -1, -1, 10)
	sweety.leftArm(-1, -1, -1, -1, 150)
	sweety.saying("my hands are close")
def trackFace():
	sweety.startTrack()
	sweety.eyesTracker.opencv.setCameraIndex(0)
	sweety.eyesTracker.findFace()
def stopTracking():
	sweety.stopTrack()
