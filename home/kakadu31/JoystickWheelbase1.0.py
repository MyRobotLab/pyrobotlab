python = Runtime.start("python","Python")

#Variables
saberPort = "/dev/ttyUSB0"
arduinoPort = "/dev/ttyACM0"
controller = 3
servoNeckPin = 3
servoRotPin = 9
servoNeckPos = 90
servoRotPos = 70

#Initialising arduino
arduino = Runtime.start("arduino","Arduino")
arduino.connect(arduinoPort)

#Initialising Joystick
joy = Runtime.createAndStart("joy","Joystick")
joy.setController(controller)
joy.addInputListener(python)

#Initialising Servos
servoNeck = Runtime.start("servoNeck","Servo")
servoRot = Runtime.start("servoRot","Servo")
servoNeck.attach(arduino, servoNeckPin)
servoRot.attach(arduino, servoRotPin)
servoNeck.setMinMax(40,120)
servoRot.setMinMax(30,110)
servoNeck.moveTo(servoNeckPos)
servoRot.moveTo(servoRotPos)

#Initializing Sabertooth
saber = Runtime.start("saber","Sabertooth")
saber.connect(saberPort)
(1)

def onJoystickInput(data):
	speed = 30 
	global servoNeckPos
	global servoRotPos
	#print dir(data)
	print data.id
	print data.value
	if(data.id == 'W' and data.value == 1):
		saber.driveForwardMotor1(speed)
		saber.driveForwardMotor2(speed)
	elif(data.id == 'A' and data.value == 1):
		saber.driveForwardMotor2(speed)
		saber.driveBackwardsMotor1(speed)
	elif(data.id == 'S' and data.value == 1):
		saber.driveBackwardsMotor1(speed)
		saber.driveBackwardsMotor2(speed)
	elif(data.id == 'D' and data.value == 1):
		saber.driveBackwardsMotor2(speed)
		saber.driveForwardMotor1(speed)
	#Camera Controll
	elif(data.id == 'I' and data.value == 1):
		servoNeckPos = servoNeckPos + 5
		servoNeck.moveTo(servoNeckPos)
	elif(data.id == 'K' and data.value == 1):
		servoNeckPos = servoNeckPos - 5
		servoNeck.moveTo(servoNeckPos)
	elif(data.id == 'J' and data.value == 1):
		servoRotPos = servoRotPos + 5
		servoRot.moveTo(servoRotPos)
	elif(data.id == 'L' and data.value == 1):
		servoRotPos = servoRotPos - 5
		servoRot.moveTo(servoRotPos)
	else:
		saber.driveForwardMotor1(0)
		saber.driveForwardMotor2(0)