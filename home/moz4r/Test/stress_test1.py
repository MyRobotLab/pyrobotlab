# stress test

from time import sleep
import random

leftPort = "COM3"

i01 = Runtime.createAndStart("i01", "InMoov")

sleep(1)
i01.startMouth()
i01.startHead(leftPort)
i01.head.jaw.setSpeed(1.0)
i01.head.jaw.map(0,180,85,100)
i01.startLeftHand(leftPort)
sleep(1)
i01.startMouthControl(leftPort)

i01.mouth.speakBlocking("voice test voice test")
i01.mouth.speakBlocking("voice test voice test")


	
MoveRandomTimer = Runtime.start("MoveRandomTimer","Clock")

def MoveRandom(timedata):
	i01.leftHand.thumb.setVelocity(random.uniform(10,300))
	i01.leftHand.thumb.moveTo(random.uniform(10.1,140.2))
	MoveRandomTimer.setInterval(random.randint(500,900))
	i01.mouth.speak("test")
	
MoveRandomTimer.addListener("pulse", python.name, "MoveRandom")
MoveRandomTimer.startClock()
