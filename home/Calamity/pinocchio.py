from java.lang import String
import random
from threading import Timer
import math


#OPTIONS
faceRecognizer=False
joystick=False
randomMove=False
headTracking=True
lastName="christian"

leftPort="COM20"
rightPort="COM21"

webgui=Runtime.create("WebGui","WebGui")
webgui.autoStartBrowser(False)
webgui.startService()

#start speech recognition and AI
wksr=Runtime.createAndStart("webkitspeechrecognition","WebkitSpeechRecognition")
pinocchio = Runtime.createAndStart("pinocchio", "ProgramAB")
pinocchio.startSession("christian", "pinocchio")
htmlfilter=Runtime.createAndStart("htmlfilter","HtmlFilter")
mouth=Runtime.createAndStart("i01.mouth","AcapelaSpeech")
wksr.addListener("publishText","python","heard")
pinocchio.addTextListener(htmlfilter)
htmlfilter.addTextListener(mouth)

#Start inMoov
i01 = Runtime.createAndStart("i01", "InMoov")
i01.startMouth()
i01.startMouthControl(leftPort)

#Head
i01.head.jaw.setMinMax(60,90)
i01.mouthControl.setmouth(60,90)
i01.head.jaw.setRest(90)
i01.head.neck.map(0,180,25,180)
i01.head.neck.setRest(90)
i01.head.rothead.map(0,180,25,170)
i01.head.rothead.setRest(115)
i01.head.eyeY.setMinMax(85,150)
#i01.head.eyeY.map(0,180,80,100)
i01.head.eyeY.setRest(115)
i01.head.eyeX.setMinMax(75,115)
#i01.head.eyeX.map(0,180,70,100)
i01.head.eyeX.setRest(95)

#Left Arm
i01.startLeftArm(leftPort)
i01.leftArm.shoulder.map(0,180,30,100)
i01.leftArm.omoplate.map(0,180,10,75)
i01.leftArm.rotate.map(0,180,46,160)
i01.leftArm.shoulder.setRest(30)
i01.leftArm.omoplate.setRest(15)
i01.leftArm.rotate.setRest(90)


#Right Arm
i01.startRightArm(rightPort)
i01.rightArm.shoulder.map(0,180,00,180)
i01.rightArm.omoplate.map(0,180,10,70)
i01.rightArm.rotate.map(0,180,46,160)
i01.rightArm.bicep.map(0,180,5,82)
i01.rightArm.shoulder.setRest(20)
i01.rightArm.omoplate.setRest(15)
i01.rightArm.rotate.setRest(90)
i01.rightArm.bicep.setRest(10)

i01.rest()


# OpenCV
opencv = i01.startOpenCV()
opencv.setCameraIndex(2)
opencv.capture()
opencvR = Runtime.createAndStart("opencvR","OpenCV")
opencvR.setCameraIndex(1)
opencvR.capture()


pinocchio.addListener("publishResponse","python","randomMoveAction")  


def headTrackingInit():
	i01.startEyesTracking(leftPort)
	i01.startHeadTracking(leftPort)

	i01.headTracking.faceDetect()
	i01.eyesTracking.faceDetect()


#i01.autoPowerDownOnInactivity(120)


def randomMoveAction(data):
  if randomMove:
    #print "test1"
    i01.setHeadSpeed(1.0,1.0)
    neck=i01.head.neck.getPos()+random.randint(-10,10)
    rothead=i01.head.rothead.getPos()+random.randint(-20,20)
    if neck<45 or neck>135:
      neck=90
    if rothead<45 or rothead>135:
      rothead=90
    i01.moveHead(neck,rothead)
    i01.setHeadSpeed(1.0,1.0)
  else:
    print "test2"

def heard(data):
	global lastName
	if(faceRecognizer):
		lastName=fr.getLastRecognizedName()
		if((lastName+"-pinocchio" not in pinocchio.getSessionNames())):
			mouth.speak("Hello "+lastName)
			sleep(2)
	pinocchio.getResponse(lastName,data)

def joystickInit():
	joystickId = 3
	global uberjoy
	global controllerButtonMap
	global controllerButtonMapTrigger
	global controllerButtonReverse
	global controllerButtonTrigger
	global controllerButtonTriggerState
	uberjoy = Runtime.createAndStart("uberjoy", "Joystick")
	uberjoy.setController(joystickId)
	uberjoy.startPolling()

	controllerButtonMap={"x":i01.leftArm.rotate,"y":i01.leftArm.bicep,"z":i01.rightArm.rotate,"rz":i01.rightArm.bicep,"4":i01.head.neck,"5":i01.head.neck,"6":i01.head.rothead,"7":i01.head.rothead}
	controllerButtonMapTrigger={"x":i01.leftArm.omoplate,"y":i01.leftArm.shoulder,"z":i01.rightArm.omoplate,"rz":i01.rightArm.shoulder}
	controllerButtonReverse={"x":True,"y":True,"z":False,"rz":True,"4":True,"5":False,"6":True,"7":False}
	controllerButtonTrigger={"x":"10","y":"10","z":"11","rz":"11"}
	controllerButtonTriggerState={"10":False,"11":False}
	
	for button,servo in controllerButtonMap.iteritems():
		servo.setSpeedControlOnUC(False)

	uberjoy.addListener("publishInput", "python", "joystickOnPublishInput")
	
def joystickOnPublishInput(data):
	global controllerButtonTriggerState
	if(controllerButtonReverse.get(data.id)):
		data.value*=-1
	if(controllerButtonTriggerState.has_key(data.id)):
		print "trigger button pressed"
		for k,v in controllerButtonTrigger.iteritems():
			if v==data.id:
				if controllerButtonTriggerState.get(data.id):
					controllerButtonMapTrigger.get(k).stop()
				else:
					controllerButtonMap.get(k).stop()
		controllerButtonTriggerState[data.id]=bool(data.value)
		return
	if(controllerButtonMap.has_key(data.id)):
		servotmp=[None]
		if(controllerButtonMapTrigger.has_key(data.id)):
			print "found trigger "+data.id+" = "+ controllerButtonMapTrigger.get(data.id).getName()
			if(controllerButtonTriggerState.get(controllerButtonTrigger.get(data.id))):
				servotmp[0]=controllerButtonMapTrigger.get(data.id)
				print "using alt servo: "+servotmp[0].getName()
			else:
				servotmp[0]=controllerButtonMap.get(data.id)
				print "using normal servo: "+ servotmp[0].getName()
		else:
			servotmp[0]=controllerButtonMap.get(data.id)
			print "using normal servo: "+ servotmp[0].getName()
		servo=servotmp[0]
		print servo.getName()
		absValue = math.fabs(data.value)
  		if (absValue < 0.300):
    			servo.stop()
    			return
		absValue = absValue-0.01
  		servo.setSpeed(absValue)
		delay = int((1-absValue) * 200)+25
		servo.stop()
  		if (data.value > 0.0):
			#servo.sweep(servo.getPos(), int(servo.getMax()), delay, 1, True)
			servo.sweep(servo.getPos(), 180, delay, 1, True)
		else:
			servo.sweep(0, servo.getPos(), delay, -1, True)

if (headTracking):
	headTrackingInit()

if(joystick):
	joystickInit()

headTilt=Runtime.createAndStart("headTilt","Servo")
headTilt.attach(i01.arduinos.get(leftPort).getName(),30)
headTilt.setMinMax(30,180)
headTilt.setRest(105)

def power_up():
	headTilt.attach()

def power_down():
	headTilt.detach()

i01.beginCheckingOnInactivity(60)


i01.startPIR(leftPort,23)
pinocchio.getResponse("Initialize Pinocchio")
