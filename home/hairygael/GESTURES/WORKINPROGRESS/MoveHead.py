MoveHeadTimer = Runtime.start("MoveHeadTimer","Clock")
MoveHeadTimer.setInterval(10)

def MoveHead(timedata):
	i01.setHeadSpeed(0.5, 0.5)
	rollneck.setSpeed(0.5)
	i01.moveHead(random.randint(70,100), random.randint(60,90))
	rollneck.moveTo(random.randint(50,130))
	MoveHeadTimer.setInterval(random.randint(5000,20000))

MoveHeadTimer.addListener("pulse", python.name, "MoveHead")		
