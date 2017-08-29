# -*- coding: utf-8 -*- 
#This function listen from analog pin values

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




def HallEffectSensorHadSendNoFakeValueFunc():
		global SensorReaction
		if SensorReaction==1:
			print ("speak detected")
			talk("Youpi! Les capteurs fonctionnent, j'ai détecté la pomme dans ma main")
			SensorReaction=0
			i01.rightHand.attach()
			i01.moveHand("right",110,120,120,80,80,2)
			rightArm.bicep.attach()
			rightArm.bicep.moveTo(20)
			rightArm.shoulder.attach()
			rightArm.omoplate.attach()
			rightArm.rotate.attach()
			rightArm.shoulder.moveTo(90)
			rightArm.rotate.moveTo(130)
			rightArm.omoplate.moveTo(40)
			i01.moveHead (50,120) 
			sleep(4)
			talk("c'est domage que je ne puisse pas la manger, elle à l'air trop bonne")
			sleep(4)
			i01.moveHead (40,120) 
			rightArm.bicep.detach()
			rightArm.shoulder.detach()
			rightHand.wrist.detach()
			rightArm.rotate.detach()
			rightArm.omoplate.detach()
			detachHard()
			sleep(2)
			i01.rightHand.detach()
		
	



def StartSensorDemo():
	global PleaseRobotDontSleep
	PleaseRobotDontSleep=1
	StandByDemoHallEffect()


def StandByDemoHallEffect():
	global SensorReaction
	global SensorCounter
	i01.rightHand.attach()
	i01.moveHead (50,120) 
	i01.moveHand("right",100,120,120,100,120,2)
	rightArm.bicep.attach()
	rightArm.bicep.moveTo(180)
	rightArm.shoulder.attach()
	rightArm.shoulder.moveTo(30)
	sleep(2)
	rightArm.bicep.detach()
	rightArm.shoulder.detach()
	rightHand.wrist.detach()
	detachHard()
	sleep(2)
	i01.rightHand.thumb.detach()
	i01.rightHand.majeure.detach()
	i01.rightHand.ringFinger.detach()
	i01.rightHand.pinky.detach()
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
					HallEffectSensorHadSendNoFakeValueFunc()
					PrivateTimerStart=0
				SensorCounter=0
				PrivateTimer=0
		
 
right.addListener("publishPinArray","python","publishPin")
#Ok i use halleffect sensors the signal is not straigh so I need to tweak the analog values

#how many values I want every 1 second
right.setBoard("atmega2560")
right.enablePin(54,TimerIndex)	
	
	
	
	











