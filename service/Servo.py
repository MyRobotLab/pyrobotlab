#########################################
# Servo.py
# categories: servo
# more info @: http://myrobotlab.org/service/Servo
#########################################
# uncomment for virtual hardware
# virtual = True

servoPin01 = 4
servoPin02 = 5

# port = "/dev/ttyUSB0"
port = "COM15"

# start optional virtual arduino service, used for test
if ('virtual' in globals() and virtual):
    virtualArduino = Runtime.start("virtualArduino", "VirtualArduino")
    virtualArduino.connect(port)

# create a servo controller and a servo
arduino = Runtime.start("arduino","Arduino")
servo01 = Runtime.start("servo01","Servo")
servo02 = Runtime.start("servo02","Servo")

# initialize arduino
# arduino.connect("/dev/ttyUSB0")
arduino.connect(port)

# TODO - set limits
servo01.setMinMax(0, 180)

# attach servo
servo01.attach(arduino.getName(), servoPin01)
servo02.attach(arduino.getName(), servoPin02)

# auto disable - this enables (starts pwm) before a movement
# and disables (stops pwm) after a movement
# servo01.setAutoDisable(True) - FIXME waiting for mrl fix in Servo.java

# fast sweep
servo01.moveTo(179)
sleep(0.5)

# print info
print("servo position :{}".format(servo01.getPos()))
print("servo pin :{}".format(servo01.getPin()))
print("servo rest position :{}".format(servo01.getRest()))
print("servo velocity :{}".format(servo01.getVelocity()))
print("servo is inverted :{}".format(servo01.isInverted()))
print("servo min :{}".format(servo01.getMin()))
print("servo max :{}".format(servo01.getMax()))

servo01.moveTo(10)
sleep(0.5)

servo01.moveTo(179)
sleep(0.5)

# sync servo02 with servo01
# now servo2 will be a slave to servo01
servo02.sync(servo01)

servo01.moveTo(10)
sleep(0.5)

servo01.moveTo(179)
sleep(0.5)

servo01.moveTo(10)
sleep(0.5)

# speed changes
servo01.setSpeed(0.99) # set speed to 99% of full speed
servo01.moveTo(90)
sleep(0.5)

servo01.setSpeed(0.50) # set speed to 50% of full speed
servo01.moveTo(180)
sleep(4)

servo01.setSpeed(1.0) # set speed to 100% of full speed

# moving to rest position
servo01.rest()
sleep(0.5)

# writing position in us
servo01.writeMicroseconds(1875)
print("servo position :{}".format(servo01.getPos())) # check if correct ?

servo01.moveTo(10)
sleep(0.5)

servo01.moveTo(179)
sleep(0.5)

servo01.moveTo(10)
sleep(0.5)

# speed changes
servo01.setVelocity(15) # set velocity to something slow
servo01.moveToBlocking(60)

servo01.setVelocity(200) # set velocity to something fast
servo01.moveToBlocking(180)

servo01.setVelocity(-1) # set velocity to maximum

# moving to rest position
servo01.rest()
sleep(2)

# turn off power
servo01.disable()
servo02.disable()

# detaching servo01 from controller
# TODO - make arduino.detach() detach all services
servo01.detach()
servo02.detach()
