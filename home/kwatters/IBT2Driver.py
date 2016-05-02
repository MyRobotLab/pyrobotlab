from org.myrobotlab.service import Runtime
from org.myrobotlab.service import Arduino
from time import sleep

port = "COM30"
ard1 = Runtime.create("ard1", "Arduino")
ard1.connect(port)

right = 5
left = 6

ard1.pinMode(right, Arduino.OUTPUT)
ard1.pinMode(left, Arduino.OUTPUT)

speed = 200
ard1.analogWrite(left, 0);
ard1.analogWrite(right, speed);

sleep(10)

ard1.analogWrite(left, speed);
ard1.analogWrite(right, 0);

sleep(10)

ard1.analogWrite(left, 0);
ard1.analogWrite(right, 0);
# IBT uses 2 pins for control  (forward vs reverse)
