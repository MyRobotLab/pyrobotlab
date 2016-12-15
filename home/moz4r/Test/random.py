import random
from time import sleep

i01 = Runtime.createAndStart("i01", "InMoov")
i01.startHead("COM3")

sleep(1)


#this is a function that do a job ( called inside the timer )
def MoveHeadRandomize():
	if IcanMoveHeadRandom==1:
		i01.moveHead(random.randint(50,130),random.randint(50,130))
		
#we create the timer object
MoveHeadTimer = Runtime.start("MoveHeadTimer","Clock")
MoveHeadTimer.setInterval(1001)


#this is the main timer function called by the time
def MoveHead(timedata):

	MoveHeadRandomize()
	#we random the next time
	MoveHeadTimer.setInterval(random.randint(600,1200))
		

#this is called when we use MoveHeadTimer.stopClock()
def MoveHeadStopped():

	if IcanMoveHeadRandom==1:
		i01.moveHead(90,90)
		HeadSide.moveTo(90)
		
#this is called when we use MoveHeadTimer.startClock()
def MoveHeadStart():
	MoveHeadRandomize()
	
MoveHeadTimer.addListener("pulse", python.name, "MoveHead")
MoveHeadTimer.addListener("clockStopped", python.name, "MoveHeadStopped")		
MoveHeadTimer.addListener("clockStarted", python.name, "MoveHeadStart")


#we start the clock
MoveHeadTimer.startClock()

#start to move head random 10 seconds
IcanMoveHeadRandom=1
sleep(10)
IcanMoveHeadRandom=0


