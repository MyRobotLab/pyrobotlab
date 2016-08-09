MoveHeadTimer = Runtime.start("MoveHeadTimer","Clock")
MoveHeadTimer.setInterval(1000)


def MoveHead(timedata):
	if IsInmoovLeft==1:
		i01.setHeadSpeed(0.8, 0.8)
		i01.moveHead(random.randint(50,130),random.randint(50,130))
	
MoveHeadTimer.addListener("pulse", python.name, "MoveHead")
