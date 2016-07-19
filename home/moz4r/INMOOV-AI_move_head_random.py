MoveHeadTimer = Runtime.start("MoveHeadTimer","Clock")
MoveHeadTimer.setInterval(1000)


def MoveHead(timedata):
	if IsInmoovLeft==1:
		i01.setHeadSpeed(0.5, 0.5)
		i01.moveHead(random.randint(30,150),random.randint(30,150))
	
MoveHeadTimer.addListener("pulse", python.name, "MoveHead")
