# stress test

from time import sleep
import random

leftPort = "COM3"

i01 = Runtime.createAndStart("i01", "InMoov")

sleep(1)
i01.startMouth()
i01.startLeftHand(leftPort)
sleep(1)


i01.mouth.speakBlocking("voice test voice test")
i01.mouth.speakBlocking("voice test voice test")

i01.leftHand.thumb.setVelocity(random.uniform(100,300))
	
MoveRandomTimer = Runtime.start("MoveRandomTimer","Clock")

def MoveRandom(timedata):
	
	i01.leftHand.thumb.moveTo(random.uniform(10.1,140.2))
	MoveRandomTimer.setInterval(random.randint(1000,2000))
	i01.mouth.speak("voice test voice test")
	
MoveRandomTimer.addListener("pulse", python.name, "MoveRandom")
MoveRandomTimer.startClock()
	
