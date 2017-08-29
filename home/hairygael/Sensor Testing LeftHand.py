#This simple sensor InMoov script was tested on MyRobotLab version 1.0.1851
#The result should be seen in the Oscope and in the java tab.
#Based on moz4r test script.
#This function listen from analog pin values

left=Runtime.create("i01.left", "Arduino")
left.setBoard("atmega2560")
left = Runtime.start("i01.left", "Arduino")
left.connect("COM20")
 


global TimerIndex
TimerIndex=100
#Value to translate analog pin reaction
global SensorCounter
SensorCounter=0
#If SensorReaction=1 so the sensor had detected something interesting !!
global SensorReaction
SensorReaction=0

#I use publishPin loop to make a timer counter
global PrivateTimer
PrivateTimer=0
global PrivateTimerStart
PrivateTimerStart=0




def SensorHadSendNoFakeValueFunc():
		global SensorReaction
		if SensorReaction==1:
			print ("speak detected")
			talk("Great! My sensors are functionnal, I felt something in my hand")
			SensorReaction=0
			i01.leftHand.attach()
			i01.moveHand("right",110,120,120,80,80,2)
			leftArm.bicep.attach()
			leftArm.bicep.moveTo(20)
			leftArm.shoulder.attach()
			leftArm.rotate.attach()
			leftArm.shoulder.moveTo(90)
			leftArm.rotate.moveTo(130)
			leftArm.omoplate.moveTo(40)
			i01.moveHead (50,120) 
			sleep(4)
			talk("I wish I knew what this is")
			sleep(4)
			i01.moveHead (40,120) 
			leftArm.bicep.detach()
			leftArm.shoulder.detach()
			leftHand.wrist.detach()
			leftArm.rotate.detach()
			leftArm.omoplate.detach()
			detachHard()
			sleep(2)
			i01leftHand.detach()
		
	



def StartSensorDemo():
	global PleaseRobotDontSleep
	PleaseRobotDontSleep=1
	StandByDemo()


def StandByDemo():
	global SensorReaction
	global SensorCounter
	i01.leftHand.attach()
	i01.moveHead (50,120) 
	i01.moveHand("right",100,120,120,100,120,2)
	leftArm.bicep.attach()
	leftArm.bicep.moveTo(180)
	leftArm.shoulder.attach()
	leftArm.shoulder.moveTo(30)
	sleep(2)
	leftArm.bicep.detach()
	leftArm.shoulder.detach()
	leftHand.wrist.detach()
	detachHard()
	sleep(2)
	i01.leftHand.thumb.detach()
	i01.leftHand.majeure.detach()
	i01.leftHand.ringFinger.detach()
	i01.leftHand.pinky.detach()
	sleep(1)
	SensorCounter=0
	SensorReaction=1
	

def publishPin(pins):
	global TimerIndex
	global PrivateTimer
	global PrivateTimerStart

	#the timer init
	if PrivateTimerStart==1:
		PrivateTimer+=1
		
	global SensorCounter

	for pin in range(0, len(pins)):
		#ok my hall effect sensor send interesting data after 710
		if pins[pin].value > 700:
			#debug
			print "RESIST !",pins[pin].value,SensorCounter,PrivateTimer
			#we found interesting data we check if they are not fake
			PrivateTimerStart=1
			SensorCounter+=1
		
			#I want 100 values on 1 second  ( publishPin run every 1 second / TimerIndex )
			if PrivateTimer>=TimerIndex:
				if SensorCounter>5:
					
					print "DETECTED HALL EFFECT"
					SensorHadSendNoFakeValueFunc()
					PrivateTimerStart=0
				SensorCounter=0
				PrivateTimer=0
		
 
left.addListener("publishPinArray","python","publishPin")

#how many values I want every 1 second
left.setBoard("atmega2560")
left.enablePin(54,TimerIndex)	# TimerIndex IS HOW MANY POLLS / SECONDS
	
	
	
	











