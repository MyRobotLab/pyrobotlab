MoveHeadTimer = Runtime.start("MoveHeadTimer","Clock")
MoveHeadTimer.setInterval(10)


def MoveHead(timedata):
	if IsInmoovArduino==1:
		i01.setHeadSpeed(0.1, 0.1)
		i01.moveHead(random.randint(50,130),random.randint(50,130))
		HeadSide.moveTo(random.randint(50,130))
		HeadSide.setSpeed(0.1)
		MoveHeadTimer.setInterval(1000)
	
MoveHeadTimer.addListener("pulse", python.name, "MoveHead")
