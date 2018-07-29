#Variables
saberPort = "/dev/ttyUSB0"

#Initializing Motorcontroller
saber = Runtime.start("saber", "Sabertooth")
m1 = Runtime.start("m1","MotorPort")
m2 = Runtime.start("m2","MotorPort")
# configure services
m1.setPort("m1")
m2.setPort("m2")
# in some cases its necessary to "invert" a motor
m1.setInverted(False)
m2.setInverted(False)


#Initializing Joystick
joystick = Runtime.start("joystick","Joystick")
print(joystick.getControllers())
python.subscribe("joystick","publishJoystickInput")
joystick.setController(0)
joystick.startPolling()

# attach services
saber.attach(m1)
saber.attach(m2)

#Initializing Joystick
joystick = Runtime.start("joystick","Joystick")
#m1.attach(joystick.getAxis("ry"))
#m2.attach(joystick.getAxis("rx")) 
saber.connect(saberPort)
m1.stop();
m2.stop();
sleep(1)


def onJoystickInput(data):
	print (data)
	global joyY
	global joyX
	global rT2
	
	#Controller wird "ausgelesen"
	if (data.id == "y"):
		joyY = data.value * -120
		#joyY = (math.expm1(joyY))/(math.expm1(120))
		if (abs(data.value) <= deadspot):
			joyY = 0
		#print ("updated value of y")
	if (data.id == "x"):
		joyX = data.value * 120
		if (abs(data.value) <= deadspot):
			joyX = 0
		#print ("updated value of x")
	if (data.id == "Right Thumb"):
		rT2 = data.value
		joyX = 0
		joyY = 0
		m1.stop()
		m2.stop()
		print ("R Thumb pressed")
	drive(joyY, joyX)
		
def drive(joyY, joyX):
	global motMixL
	global motMixR
	global motMixLOld
	global motMixROld
	#Treshhold at which the pivot action starts
	global pivYLimit
	pivYLimit = 32.0
	global accTreshhold
	accTreshhold = 20.0
	#Values for smoother control
	global exponentialcoeff
	exponentialcoeff = 30
	global deadspot
	deadspot = 0.1
	#Temporary variables
	global motPremixL
	global motPremixR
	global pivSpeed
	global pivScale
	#Calculation of the motor speeds before mixing
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
	#To Do
	
	#Convert to Motor Signal	
	if (motMixL > 0):
		motMixL = ((exponentialcoeff**(motMixL/120))-1)/(exponentialcoeff-1)
	else:
		motMixL = -((exponentialcoeff**(abs(motMixL/120)))-1)/(exponentialcoeff-1)
	if (motMixR > 0):
		motMixR = ((exponentialcoeff**(motMixR/120))-1)/(exponentialcoeff-1)
	else:
		motMixR = -((exponentialcoeff**(abs(motMixR)/120))-1)/(exponentialcoeff-1)

	motMixLOld = motMixL
	motMixROld = motMixR
	print ("rSpeed: ", motMixR, " / ", "lSpeed: ", motMixL)
	m1.move(motMixL)
	m2.move(motMixR)

