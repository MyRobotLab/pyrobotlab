def MoveHeadRandomize():

	if IsInmoovArduino==1 and IcanMoveHeadRandom==1:
		
		head.neck.setSpeed(NeckSpeed-0.1)
		head.rothead.setSpeed(RotHeadSpeed-0.1)
		HeadSide.setSpeed(PistonSideSpeed-0.1)
		i01.moveHead(random.randint(50,130),random.randint(50,130))
		HeadSide.moveTo(random.randint(50,130))



MoveHeadTimer = Runtime.start("MoveHeadTimer","Clock")
MoveHeadTimer.setInterval(1001)


def MoveHead(timedata):

	MoveHeadRandomize()
	MoveHeadTimer.setInterval(random.randint(600,1200))
		
def MoveHeadStopped():

	if IsInmoovArduino==1 and IcanMoveHeadRandom==1:
		i01.moveHead(NeckRest,RotHeadRest)
		HeadSide.moveTo(HeadSideRest)
		

def MoveHeadStart():
	MoveHeadRandomize()
	
MoveHeadTimer.addListener("pulse", python.name, "MoveHead")
MoveHeadTimer.addListener("clockStopped", python.name, "MoveHeadStopped")		
MoveHeadTimer.addListener("clockStarted", python.name, "MoveHeadStart")

