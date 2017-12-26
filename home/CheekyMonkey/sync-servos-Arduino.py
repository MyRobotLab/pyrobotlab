#########################################
# synchronising servo movements - Arduino connected servos
# Acapulco Rolf
# December 15 2017
#########################################

# Arduino Nano Pins
# http://www.pighixxx.com/test/pinouts/boards/nano.pdf

servoPin01 = 4
servoPin02 = 5
#servoPin03 = 4

port = "/dev/ttyUSB1"
# port = "COM5"

# create a servo controller and three servos
arduino = Runtime.start("arduino","Arduino")
servo01 = Runtime.start("servo01","Servo")
servo02 = Runtime.start("servo02","Servo")
#servo03 = Runtime.start("servo03","Servo")

# initialize arduino
print("connecting the arduino to serial port")
arduino.connect(port)

print("setting min and max servo limits")
servo01.setMinMax(10, 170)
servo02.setMinMax(10, 170)
#servo03.setMinMax(30, 130)
#servo02.setInverted(True)

# attach servos
print("attaching servos to the controller")
servo01.attach(arduino.getName(), servoPin01)
servo02.attach(arduino.getName(), servoPin02)
#servo03.attach(arduino.getName(), servoPin03)


# print info
print("servo position :{}".format(servo01.getPos()))
print("servo pin :{}".format(servo01.getPin()))
print("servo rest position :{}".format(servo01.getRest()))
print("servo velocity :{}".format(servo01.getVelocity()))
print("servo is inverted :{}".format(servo01.isInverted()))
print("servo min :{}".format(servo01.getMin()))
print("servo max :{}".format(servo01.getMax()))

print("servo position :{}".format(servo02.getPos()))
print("servo pin :{}".format(servo02.getPin()))
print("servo rest position :{}".format(servo02.getRest()))
print("servo velocity :{}".format(servo02.getVelocity()))
print("servo is inverted :{}".format(servo02.isInverted()))
print("servo min :{}".format(servo02.getMin()))
print("servo max :{}".format(servo02.getMax()))

#print("servo position :{}".format(servo03.getPos()))
#print("servo pin :{}".format(servo03.getPin()))
#print("servo rest position :{}".format(servo03.getRest()))
#print("servo velocity :{}".format(servo03.getVelocity()))
#print("servo is inverted :{}".format(servo03.isInverted()))
#print("servo min :{}".format(servo03.getMin()))
#print("servo max :{}".format(servo03.getMax()))

# sync servo02 with servo01
# servo2 will be a slave to servo01
print("syncing servo02 with servo01")
servo02.sync(servo01)

# sync servo03 with servo01
# servo3 will be a slave to servo01
#print("syncing servo03 with servo01")
#servo03.sync(servo01)


def moveservos1():
	for myangle in range (10,170,15):
		print("servo angle "+str(myangle))
		servo01.moveTo(myangle)
		sleep(0.3)

	for myangle in range (170,10,15):
		print("servo angle "+str(myangle))
		servo01.moveTo(myangle)
		sleep(0.3)

		
def moveservos():
	servo01.moveTo(10)
	sleep(3)
	servo01.moveTo(160)
	sleep(3)
	servo01.moveTo(10)
	sleep(3)
	servo01.moveTo(160)

		
def move():		
	for kount in range (1,10):
		print ("servo sweep pass " + str(kount))
		moveservos()
		sleep(2)
			
move()

# turn off power
print("turn off servos pwm")
servo01.disable()
servo02.disable()
#servo03.disable()
	
