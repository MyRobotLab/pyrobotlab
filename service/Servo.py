#########################################
# Servo.py
# categories: servo
# more info @: http://myrobotlab.org/service/Servo
#########################################
# virtual = True

servoPin = 4
# port = "/dev/ttyUSB0"
port = "COM15"

# start optional virtual arduino service, used for test
if ('virtual' in globals() and virtual):
    virtualArduino = Runtime.start("virtualArduino", "VirtualArduino")
    virtualArduino.connect(port)

# create a servo controller and a servo 
arduino = Runtime.start("arduino","Arduino")
servo = Runtime.start("servo","Servo")

# initialize arduino
# arduino.connect("/dev/ttyUSB0")
arduino.connect(port)

# TODO - set limits
servo.setMinMax(0, 180)

# attach servo
servo.attach(arduino.getName(), servoPin)

# fast sweep
servo.moveTo(179)
sleep(0.5)

servo.moveTo(10)
sleep(0.5)

servo.moveTo(179)
sleep(0.5)

servo.moveTo(10)
sleep(0.5)

servo.moveTo(179)
sleep(0.5)

servo.moveTo(10)
sleep(0.5)

# speed changes
servo.setVelocity(15) # set velocity to something slow
servo.moveToBlocking(60)

servo.setVelocity(200) # set velocity to something fast
servo.moveToBlocking(180)

servo.setVelocity(-1) # set velocity to maximum

# moving to rest position
servo.rest()
sleep(2)

# turn off power
servo.disable()

# detaching servo from controller
servo.detach()