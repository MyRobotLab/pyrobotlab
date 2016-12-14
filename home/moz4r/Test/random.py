import random
from time import sleep

i01 = Runtime.createAndStart("i01", "InMoov")
i01.startHead("COM3")

sleep(1)


def MoveHeadRandomize():
	if IcanMoveHeadRandom==1:
		i01.moveHead(random.randint(50,130),random.randint(50,130))
		

MoveHeadTimer = Runtime.start("MoveHeadTimer","Clock")
MoveHeadTimer.setInterval(1001)


def MoveHead(timedata):

	MoveHeadRandomize()
	MoveHeadTimer.setInterval(random.randint(600,1200))
		
def MoveHeadStopped():

	if IcanMoveHeadRandom==1:
		i01.moveHead(90,90)
		HeadSide.moveTo(90)
		

def MoveHeadStart():
	MoveHeadRandomize()
	
MoveHeadTimer.addListener("pulse", python.name, "MoveHead")
MoveHeadTimer.addListener("clockStopped", python.name, "MoveHeadStopped")		
MoveHeadTimer.addListener("clockStarted", python.name, "MoveHeadStart")

MoveHeadTimer.startClock()

#start to move head random 10 seconds
IcanMoveHeadRandom=1
sleep(10)
IcanMoveHeadRandom=0


