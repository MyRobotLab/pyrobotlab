#
# This is a smaller script to just test the servos in the head
# Start all services
arduino = Runtime.start("arduino","Arduino")
jaw = Runtime.start("jaw","Servo")
rothead = Runtime.start("RotHead","Servo")
leftEyeX = Runtime.start("LeftEyeX","Servo")
rightEyeX = Runtime.start("RightEyeX","Servo")
eyeY = Runtime.start("EyeY","Servo")
# 
# Connect the Arduino
arduino.connect("/dev/ttyACM0")
#
# Start of main script
jaw.attach(arduino,9)
jaw.setMinMax(80,120)
# Connect the head turn left and right
rothead.setRest(100)
rothead.attach(arduino,8)
rothead.setVelocity(20)
rothead.rest()
# Connect the left eye
leftEyeX.setMinMax(50,110)
leftEyeX.setRest(80)
leftEyeX.attach(arduino,10)
leftEyeX.rest()
# Connect the right eye
rightEyeX.setMinMax(60,120)
rightEyeX.setRest(90)
rightEyeX.attach(arduino,11)
rightEyeX.rest()
# Make the left eye follow the right
# runtime.subscribe("rightEyeX","publishServoEvent","leftEyeY","MoveTo")
# rightEyeX.eventsEnabled(True)
# Connect eyes up/down
eyeY.setMinMax(60,140)
eyeY.setRest(90)
eyeY.attach(arduino,12)
eyeY.rest()
def lookRight():
	rightEyeX.moveTo(120)
def lookLeft():
	rightEyeX.moveTo(60)
def lookForward():
	rightEyeX.rest()
	eyeY.rest()
def lookDown():
	EyeY.moveTo(60)
def lookUp():
	EyeY.moveTo(140)
def headRight():
	rothead.moveTo(70)
def headLeft():
	rothead.moveTo(130)
def headForward():
	rothead.rest()
lookRight()
sleep(2)
lookLeft()
sleep(2)
lookForward()
sleep(2)
lookUp()
sleep(2)
lookDown()
sleep(2)
lookForward()
sleep(2)
headRight()
sleep(5)
headLeft()
# sleep(5)
# headForward()
# sleep(5)
