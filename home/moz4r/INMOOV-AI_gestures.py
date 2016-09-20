
def rest():
	if IsInmoovArduino==1:
		i01.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
		i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
		i01.setHeadSpeed(0.2, 0.2)
		i01.setTorsoSpeed(1.0, 1.0, 1.0)
		i01.moveHead(80,86,82,78,76)
		i01.moveArm("left",5,90,0,10)
		i01.moveHand("left",2,2,2,2,2,90)
		i01.moveTorso(80,90,80)
		i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
		i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
		i01.moveArm("right",5,90,0,12)
		i01.moveHand("right",2,2,2,2,2,90)
		HeadSide.rest()
		i01.detach()
		
def No(data):
	global MoveHeadRandom
	MoveHeadRandom=0
	# WE MOVE THE ROTHEAD OR PISTONMOD
	if IsInmoovArduino==1:
		if random.randint(0,1)==1:
			#i01.attach()
			i01.setHeadSpeed(0.3, 0.3)
			i01.moveHead(80,130)
			sleep(0.5)
			i01.moveHead(80,50)
			sleep(0.5)
			i01.moveHead(81,130)
			sleep(0.5)
			i01.moveHead(79,50)
			sleep(0.5)
			i01.moveHead(83,130)
			sleep(1)
			i01.moveHead(80,90)
			i01.head.jaw.rest()
		else:
			HeadSide.setSpeed(0.3)
			HeadSide.moveTo(50)
			sleep(0.5)
			HeadSide.moveTo(120)
			sleep(1)
			HeadSide.moveTo(90)
			i01.head.jaw.rest()

def Yes(data):
	global MoveHeadRandom
	MoveHeadRandom=0
	if IsInmoovArduino==1:
		#i01.attach()
		i01.setHeadSpeed(0.3, 0.3)
		i01.moveHead(130,90)
		sleep(0.5)
		i01.moveHead(50,93)
		sleep(0.5)
		i01.moveHead(130,90)
		sleep(0.5)
	#Light(0,1,1)
	if IsInmoovArduino==1:
		i01.moveHead(60,91)
		sleep(0.5)
		i01.moveHead(120,88)
	if IsInmoovArduino==1:
		i01.moveHead(70,90)
		sleep(0.5)
		i01.moveHead(95,90)
	sleep(0.5)
	#Light(1,1,1)
	if IsInmoovArduino==1:
		i01.moveHead(90,90)
	if IsInmoovArduino==1:
		i01.head.jaw.rest()
	

def MoveHand(side,thumb,index,majeure,ringFinger,pinky):
	print side
	if side=="left":
		if thumb != -1:
			i01.leftHand.thumb.attach()
			i01.leftHand.thumb.moveTo(thumb)
			
		if index != -1:
			i01.leftHand.index.attach()
			i01.leftHand.index.moveTo(index)
			
		if majeure != -1:
			i01.leftHand.majeure.attach()
			i01.leftHand.majeure.moveTo(majeure)
			
		if ringFinger != -1:
			i01.leftHand.ringFinger.attach()
			i01.leftHand.ringFinger.moveTo(ringFinger)
			
		if pinky != -1:
			i01.leftHand.pinky.attach()
			i01.leftHand.pinky.moveTo(pinky)
		
		sleep(1)
		i01.leftHand.detach()
			
	if side=="right":
		if thumb != -1:
			i01.rightHand.thumb.attach()
			i01.rightHand.thumb.moveTo(thumb)
			
		if index != -1:
			i01.rightHand.index.attach()
			i01.rightHand.index.moveTo(index)
			
		if majeure != -1:
			i01.rightHand.majeure.attach()
			i01.rightHand.majeure.moveTo(majeure)
			
		if ringFinger != -1:
			i01.rightHand.ringFinger.attach()
			i01.rightHand.ringFinger.moveTo(ringFinger)
			
		if pinky != -1:
			i01.rightHand.pinky.attach()
			i01.rightHand.pinky.moveTo(pinky)
			
		sleep(1)
		i01.rightHand.detach()

def LookAtTheSky():
	global MoveHeadRandom
	MoveHeadRandom=0
	i01.setHeadSpeed(0.2, 0.2)
	i01.moveHead(00,90)
	sleep(5)
	i01.setHeadSpeed(0.1, 0.1)
	i01.moveHead(90)
	
	
def LookAtYourFeet():
	global MoveHeadRandom
	MoveHeadRandom=0
	i01.setHeadSpeed(0.2, 0.2)
	i01.moveHead(180,90)
	sleep(5)
	i01.setHeadSpeed(0.1, 0.1)
	i01.moveHead(90)
	
	
def LookAtYourLeft():
	global MoveHeadRandom
	MoveHeadRandom=0
	i01.setHeadSpeed(0.2, 0.2)
	i01.moveHead(120,20)
	sleep(5)
	i01.setHeadSpeed(0.1, 0.1)
	i01.moveHead(90,90)
	
def LookAtYourRight():
	global MoveHeadRandom
	MoveHeadRandom=0
	i01.setHeadSpeed(0.2, 0.2)
	i01.moveHead(120,160)
	sleep(5)
	i01.setHeadSpeed(0.1, 0.1)
	i01.moveHead(90,90)

	
	
def LookAroundYou():
	global MoveHeadRandom
	MoveHeadRandom=0
	i01.setHeadSpeed(0.2, 0.2)
	i01.moveHead(160,160)
	sleep(1)
	i01.setHeadSpeed(0.2, 0.2)
	i01.moveHead(160,20)
	sleep(1)
	i01.setHeadSpeed(0.2, 0.2)
	i01.moveHead(20,20)
	sleep(1)
	i01.setHeadSpeed(0.2, 0.2)
	i01.moveHead(20,160)
	sleep(1)
	i01.setHeadSpeed(0.1, 0.1)
	i01.moveHead(90,90)