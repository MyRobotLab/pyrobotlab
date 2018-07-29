# Connects a serial device on Windows this would COMx 
# You will need MRLComm.ino loaded on the Arduino
from time import sleep
from org.myrobotlab.service import Arduino
 
arduino = Runtime.createAndStart("arduino","Arduino")
arduino.connect("COM5")

sleep(2)
arduino.broadcastState()
arduino.setBoardMega()

redpin = 44
bluepin = 45
greenpin = 46

fadespeed = 0.025

arduino.pinMode(redpin, Arduino.OUTPUT)
arduino.pinMode(bluepin, Arduino.OUTPUT)
arduino.pinMode(greenpin, Arduino.OUTPUT)


r = 0
g = 0
b = 0

while (True):
	# fade from blue to violet
	for r in range(0, 255,5): 
		arduino.analogWrite(redpin, r)
		sleep(fadespeed)
	
	# fade from violet to red
	for b in range(255, 0, -5):
		arduino.analogWrite(bluepin, b)
		sleep(fadespeed)

  # fade from red to yellow
	for g in range(0, 255,5):
		arduino.analogWrite(greenpin, g)
		sleep(fadespeed)

	# fade from yellow to green
	for r in range(255, 0, -5):
		arduino.analogWrite(redpin, r)
		sleep(fadespeed)

	# fade from green to teal
	for b in range(0, 255,5):
		arduino.analogWrite(bluepin, b)
		sleep(fadespeed)

	# fade from teal to blue
	for g in range(255, 0, -5): 
		arduino.analogWrite(greenpin, g)
		sleep(fadespeed)
