#Variables
#Working with build 2234
saberPort = "/dev/ttyUSB0"

#Initializing Motorcontroller
saber = Runtime.start("saber", "Sabertooth")
saber.connect(saberPort)
sleep(1)

#Initializing Joystick
joystick = Runtime.start("joystick","Joystick")
print(joystick.getControllers())
python.subscribe("joystick","publishJoystickInput")
joystick.setController(0)

for x in range(0,100):
	print("power", x)
	saber.driveForwardMotor1(x)
	sleep(0.5)

for x in range(100,-1,-1):
	print("power", x)
	saber.driveForwardMotor1(x)
	sleep(0.5)
