# stress test

from time import sleep
import random

leftPort = "COM3"

i01 = Runtime.createAndStart("i01", "InMoov")
sleep(1)
i01.startMouth()
i01.startHead(leftPort)
i01.startLeftHand(leftPort)
i01.head.jaw.map(0,180,85,110)
i01.startMouthControl(leftPort)


i01.leftHand.thumb.setVelocity(random.randint(100,300))
	
MoveRandomTimer = Runtime.start("MoveRandomTimer","Clock")

def MoveRandom(timedata):
	
	i01.leftHand.thumb.moveTo(random.randint(50,130))
	MoveRandomTimer.setInterval(random.randint(10000,11000))
	i01.mouth.speak("voice test voice test")
	
MoveRandomTimer.addListener("pulse", python.name, "MoveRandom")
MoveRandomTimer.startClock()
