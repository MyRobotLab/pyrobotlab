# 2016-02-12 juerg maier
# Use Danevit Hartenberg parameters to calculate current x,y,z Position of Palm
# As I could not make JNumeric work I used my own matrix calcs

from copy import copy, deepcopy
import math

leftPort = "/dev/ttyACM1"
rightPort = "/dev/ttyACM0"

i01 = Runtime.createAndStart("i01", "InMoov")

leftHand = i01.startLeftHand(leftPort)
rightHand = i01.startRightHand(rightPort)
leftArm = i01.startLeftArm(leftPort)
rightArm = i01.startRightArm(rightPort)

head = i01.startHead(leftPort)
head.neck.setMinMax(15,140)
head.rothead.setMinMax(35,145)

# self-levelling hand, activate for demo
arduino = Runtime.getService("i01.right")
keepHorizontalOutPin = 12
keeHorizontal = True
arduino.pinMode(keepHorizontalOutPin, Arduino.OUTPUT)
arduino.digitalWrite(keepHorizontalOutPin, 1)

dhLeftArm = [
     [   0.0, 110.0,   0.0,  90.0],	# body rotation      
     [  63.0,   0.0, 330.0,   0.0],	# body bend
     [-153.0,   0.0,  40.0, -90.0],	# omoplate
     [  90.0,  80.0,   0.0,  90.0],	# shoulder (front/back)
     [ 180.0, 280.0,   0.0,  90.0],	# rotate arm
     [ 180.0,   0.0,   0.0,  90.0],	# bicep
     [   0.0, 300.0,   0.0,  90.0],	# wrist rotation
     [ 180.0,   0.0,   0.0,  90.0],	# wrist bend
     [  90.0, 100.0,   0.0,   0.0]]	# palm center

dhRightArm = [
     [   0.0, 110.0,   0.0,  90.0],          
     [ 117.0,   0.0, 330.0,   0.0],
     [ -27.0,   0.0, -40.0,  90.0],
     [ -90.0, -80.0,   0.0,  90.0],
     [ 180.0, 280.0,   0.0,  90.0],
     [ 180.0,   0.0,   0.0,  90.0],
     [   0.0, 300.0,   0.0,  90.0],
     [ 180.0,   0.0,   0.0,  90.0],
     [  90.0, 100.0,   0.0,   0.0]]

dhHead = [
	[   0.0, 110.0,   0.0,  90.0],	#body yaw to body roll
	[  90.0,   0.0, 440.0,   0.0],	#body roll to neck base
	[   0.0, -35.0,   0.0,  90.0],	#neck base to neck pitch
	[   0.0,   0.0,  80.0,   0.0],	#neck pitch to neck yaw	
	[  90.0,   0.0,   0.0,  90.0], 	#dummy to allow rothead
	[   0.0,   0.0,   0.0,   0.0]]	#rothead
    

# first joint is Z rotation (fixed values for InMoov body Z rotation)
T = [[ 1.0, 0.0, 0.0, 0.0],
	[ 0.0, 1.0, 0.0, 0.0],
	[ 0.0, 0.0, 1.0, 0.0],
	[ 0.0, 0.0, 0.0, 1.0]]

########################################
# matrix multiply for 2 4*4 matrices
########################################
def matrixMul(t0, t1):
	t2 = deepcopy(t0)
	for j in range(0, 4):
		for k in range(0, 4):
			t2[j][k] = 0.0
			for n in range(0, 4):
				t2[j][k] += t0[j][n]*t1[n][k]
	return t2


#######################################
# walk through all the joints
#######################################
def dhCalc(dhTable):

	t0 = deepcopy(T)	# initial Z rotation
	
	for i in range(0, len(dhTable)):
		ct = math.cos(math.radians(dhTable[i][0]))  #cosinus(theta)
		st = math.sin(math.radians(dhTable[i][0]))  #sinus(theta)
		ca = math.cos(math.radians(dhTable[i][3]))  #cosinus(alpha)
		sa = math.sin(math.radians(dhTable[i][3]))  #sinus(alpha)

		#set the matrix values from the dh-List
		t1 = [	
			[   ct, -st*ca,  st*sa,  ct*dhTable[i][2]],
			[   st,  ct*ca, -ct*sa,  st*dhTable[i][2]],
			[  0.0,     sa,     ca,     dhTable[i][1]],
			[  0.0,    0.0,    0.0,               1.0] ]
		
		t0 = matrixMul(t0, t1)
		print t0[0][3],t0[1][3],t0[2][3]

	return t0

##########################################
# set current hand positions into DH-table
##########################################
def lookatHand(focus):
	
	if focus == "left":
		dhTable = deepcopy(dhLeftArm)

		# set current joint values into dhParameters
		# calculate degrees from servo settings
		dhTable[2][0] = leftArm.omoplate.getPos() - 153		#omoplate - 153
		dhTable[3][0] = 90 - leftArm.shoulder.getPos() 		#shoulder
		dhTable[4][0] = 270 - leftArm.rotate.getPos()			#rotate
		dhTable[5][0] = 180 - leftArm.bicep.getPos()			#bicep

		print "left o,s,r,b", leftArm.omoplate.getPos(), leftArm.shoulder.getPos(), leftArm.rotate.getPos(), leftArm.bicep.getPos()
		print "dh   o,s,r,b", dhTable[2][0], dhTable[3][0], dhTable[4][0], dhTable[5][0]	

		result = dhCalc(dhTable)
		posPalm = [result[0][3], result[1][3], result[2][3]]
		
	else:	#right arm
		dhTable = deepcopy(dhRightArm)
		
		# set current joint values into dhParameters
		# calculate degrees from servo settings
		dhTable[2][0] = -rightArm.omoplate.getPos() - 27		#-omoplate - 27
		dhTable[3][0] = -90 - rightArm.shoulder.getPos()	#shoulder, down at 15
		dhTable[4][0] = rightArm.rotate.getPos()-270			#rotate
		dhTable[5][0] = 180 - rightArm.bicep.getPos()		#bicep

		result = dhCalc(dhTable)
		posPalm = [result[0][3], result[1][3], result[2][3]]
	
	#print "InMoov head.neck: {x:3.2f}, {y:3.2f}, {z:3.2f}".format(x=posPalm[0],y=PosPalm[1],z=PosPalm[2])
	print "palm: ", posPalm
	
	dhTableHead = deepcopy(dhHead)

	# as changing head neck/rotate changes also the head position
	# this might need to be done 2 or 3 times (TODO)
	result = dhCalc(dhTableHead)
	posHead = [result[0][3], result[1][3], result[2][3]]
	print "head: ", posHead

	# Position differences between head and palm
	pd = (posHead[0] - posPalm[0], posHead[1] - posPalm[1], posHead[2] - posPalm[2])

	# Z-rotation, atan of opposite (pd[1],y) / adjacent (pd[0],x)
	rotZ = math.degrees(math.atan(pd[1]/pd[0]))

	# X-rotation atan of opposite / adjacent (pd[2], z)
	# opposite sqrt(x*x, y*y)
	rotX = math.degrees(math.atan(math.sqrt(math.pow(pd[0], 2) + math.pow(pd[1], 2))/pd[2]))

	print "rotX, rotZ", rotX, rotZ

	# My InMoov has a limit of the neck of about +-45 real world degrees with 
	# servo degrees 15..130
	korrFactorForNeckServo =  45.0/75.0
	neck = int(rotX * korrFactorForNeckServo)
	if neck > 130:
		neck = 130;
	if neck < 15:
		neck = 15
		
	head.neck.moveTo(neck)
	print "InMoov head.neck: ", neck

	# my InMoov head has a yaw range of about +-55 real world degrees with
	# servo degrees 35..145.
	if rotZ > 0:
		rothead = int(rotZ)
	else:
		rothead = 180+int(rotZ)
	if rothead > 145:
		rothead = 145
	if rothead < 35:
		rothead = 35
		
	head.rothead.moveTo(rothead)
	print "InMoov head.rothead", rothead
	
###############################################
###############################################
def init():
	print "start lookat Test"
	i01.attach()
	i01.moveHand("left", 90,90,90,90,90,90)
	i01.moveArm("left", 5,90,30,10)
	i01.moveHand("right", 90,90,90,90,90,90)
	i01.moveArm("right", 5,90,30,10)
	i01.setHeadSpeed(0.95,0.95)
	i01.head.rothead.moveTo(90)
	i01.head.neck.moveTo(90)
	sleep(4)

def Pos1():
	# create position 1
	leftArm.omoplate.moveTo(10)	# 3 o-153
	leftArm.shoulder.moveTo(30)	# 4 90-s
	leftArm.rotate.moveTo(90)	# 5 90+r
	leftArm.bicep.moveTo(80)		# 6 180-b
	sleep(2)
	lookatHand("left")

def Pos2():
	# create a position
	rightArm.omoplate.moveTo(20)	# 3 -o-27
	rightArm.shoulder.moveTo(30)	# 4 Theta DH = -90-s+15
	rightArm.rotate.moveTo(130)	# 5 r
	rightArm.bicep.moveTo(68)	# 6 180-b
	sleep(1)
	lookatHand("right")

def Pos3():
	leftArm.omoplate.moveTo(20)	# 3 o-153
	leftArm.shoulder.moveTo(50)	# 4 90-s
	leftArm.rotate.moveTo(130)	# 5 r
	leftArm.bicep.moveTo(80)		# 6 180-b
	sleep(1)
	lookatHand("left")

def done():
	i01.moveArm("right", 5,90,30,10)	#rest
	i01.moveArm("left", 5,90,30,10)
	head.rothead.moveTo(90)
	head.neck.moveTo(90)
	sleep(2)
	
	i01.detach()
	print "done"

#################################################
init()
sleep(15)
Pos1()
sleep(5)

Pos2()
sleep(5)

Pos3()
sleep(5)

done()
