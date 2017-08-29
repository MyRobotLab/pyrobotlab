from org.myrobotlab.service import Arduino
from org.myrobotlab.service import Servo
from org.myrobotlab.service import Runtime

from time import sleep

servo1Pin = 12
servo2Pin = 13
servo3Pin = 26
servo4Pin = 4

# comPort = "/dev/ttyUSB0"
comPort = "COM6"

# create the services
arduino = Runtime.start("arduino","Arduino")
servo01 = Runtime.start("servo01","Servo")

# initialize arduino
# arduino.connect("/dev/ttyUSB0")
arduino.connect(comPort)

# TODO - set limits
servo01.setMinMax(60, 120)
  
# attach servo
servo01.attach(arduino.getName(), servo1Pin)

# fast sweep
servo01.moveTo(90)



