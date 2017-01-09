def VieAleatoire():
	#if MoveBodyRandom==1 and MoveHeadRandom==1:
	global MoveBodyRandom
	global MoveHeadRandom
	MoveBodyRandomize()
	MoveHeadRandomize()
	MoveHeadTimer.startClock()
	MoveBodyTimer.startClock()
	MoveBodyRandom=1
	MoveHeadRandom=1
	
	
