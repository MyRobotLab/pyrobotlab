#This script allows to control a robot with differential steering using a joystick for example xbox360-controller
#worky on build 2234
from math import expm1
#Variables
saberPort = "/dev/ttyUSB0"
controller = 3

#Initializing Motorcontroller
saber = Runtime.start("saber", "Sabertooth")
saber.connect(saberPort)
sleep(5)

#Initializing Joystick
joystick = Runtime.start("joystick","Joystick")
#joystick = Runtime.createAndStart("joystick","Joystick")
#joystick.setController(controller)
#joystick.addInputListener(python)
print(joystick.getControllers())
python.subscribe("joystick","publishJoystickInput")
joystick.setController(controller)
joystick.startPolling()

motMixLOld = 0
motMixROld = 0
rT2 = 0
joyY = 0
joyX = 0


def onJoystickInput(data):
	print (data)
	global joyY
	global joyX
	global rT2
	global motMixL
	global motMixR
	global motMixLOld
	global motMixROld
	#Treshhold at which the pivot action starts
	global pivYLimit
	pivYLimit = 32.0
	global accTreshhold
	accTreshhold = 20.0
	#Temporary variables
	global motPremixL
	global motPremixR
	global pivSpeed
	global pivScale
	#Controller wird "ausgelesen"
	if (data.id == "y"):
		joyY = data.value * -120
		#joyY = (math.expm1(joyY))/(math.expm1(120))
		if (abs(joyY) <= 10):
			joyY = 0
		#print ("updated value of y")
	if (data.id == "x"):
		joyX = data.value * 120
		if (abs(joyX) <= 5):
			joyX = 0
		#print ("updated value of x")
	if (data.id == "Right Thumb 2"):
		rT2 = data.value
		joyY = 0
		joyX = 0
		print ("R Thumb 2 pressed")
	
	#Calculation of the motor speeds
	if (joyY >= 0):
		#Forward
		if (joyX >= 0): 
			motPremixL = 127.0 
		else: 
			motPremixL = (127 + joyX)
		if (joyX >= 0): 
			motPremixR = (127.0-joyX) 
		else: 
			motPremixR = 127.0
	else:
		#Reverse
		print ("2")
		if (joyX >= 0): 
			motPremixR = 127.0 
		else: 
			motPremixR = (127 + joyX)
		if (joyX >= 0): 
			motPremixL = (127.0-joyX)
		else: 
			motPremixL = 127.0
	#if freins = pressed: stopp!
	if (rT2 ==1):
		motPremixL = 0
		motPremixR = 0
			
	print ("motPremixR: ", motPremixR, " / ", "motPremixL: ", motPremixL)
	#Scale Drive output due to Joystick Y input
	motPremixL = motPremixL * joyY/128.0
	motPremixR = motPremixR * joyY/128.0
	print ("motPremixRScaled: ", motPremixR, " / ", "motPremixLScaled: ", motPremixL)
	#Calculate pivot amount
	pivSpeed = joyX
	if (abs(joyY)>pivYLimit):
		pivScale = 0.0 
	else:
		pivScale = (1.0 - abs(joyY)/pivYLimit)
	print ("pivSpeed: ", pivSpeed, " / ", "pivScale: ", pivScale)
	
	#Calculate final mix of Drive and Pivot
	motMixL = (1.0-pivScale)*motPremixL + pivScale * (pivSpeed)
	motMixR = (1.0-pivScale)*motPremixR + pivScale * (-pivSpeed)
	print ("motMixR: ", motMixR, " / ", "motMixL: ", motMixL)
	
	#Acceleration Control
	#if (abs(motMixL - motMixLOld) > accTreshhold):
	#	if (motMixL > motMixLOld):
	#		motMixL = motMixL + accTreshhold
	#	else:
	#		motMixL = motMixL - accTReshhold
	#if (abs(motMixR - motMixROld) > accTreshhold):
	#	if (motMixR > motMixROld):
	#		motMixR = motMixR + accTreshhold
	#	else:
	#		motMixL = MotMixR - accTReshhold

	#Convert to Motor Signal
	motMixLOld = motMixL
	motMixROld = motMixR
	print ("rSpeed: ", motMixR, " / ", "lSpeed: ", motMixL)
	if (motMixL >= 0): saber.driveForwardMotor1(int(motMixL))
	else: saber.driveBackwardsMotor1(int(-motMixL))
	if (motMixR >= 0): saber.driveForwardMotor2(int(motMixR))
	else: saber.driveBackwardsMotor2(int(-motMixR))


#Motor test purpose
#for x in range(0,100):
#	print("power", x)
#	saber.driveForwardMotor1(x)
#	sleep(0.5)

#for x in range(100,-1,-1):
#	print("power", x)
#	saber.driveForwardMotor1(x)
#	sleep(0.5)
