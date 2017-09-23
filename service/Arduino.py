# Connects a serial device on Windows this would COMx 
# You will need MRLComm.ino loaded on the Arduino
from time import sleep
from org.myrobotlab.service import Arduino

# create an Arduino service named arduino
arduino = Runtime.createAndStart("arduino","Arduino")
port="COM3"

# start optional virtual arduino service, used for test
if ('virtual' in globals() and virtual):
    virtualArduino = Runtime.start("virtualArduino", "VirtualArduino")
    virtualArduino.connect(port)

#you have to replace COMX with your arduino serial port number
# arduino.connect("/dev/ttyUSB0") - Linux way
arduino.connect(port)

# give it a second for the serial device to get ready
sleep(1)

# update the GUI with configuration changes
arduino.broadcastState()

# set the pinMode of pin 8 to output (you can change the pin number if you want)
arduino.pinMode(8, Arduino.OUTPUT)

# turn pin 8 on and off 5 times
print "start to play with pin output"
for x in range(0, 5):
	arduino.digitalWrite(8,1)
	sleep(1) # sleep a second
	arduino.digitalWrite(8,0)
	sleep(1) # sleep a second
print "stop to play with pin output"

# analog input pins - you can see input
# on the oscope 
# analog pin range are 14-18 on uno, 54-70 on mega
# rate is the number of polling / sec
arduino.setBoardMega()
arduino.setAref("DEFAULT")
def publishPin(pins):	  
	for pin in range(0, len(pins)):print(pins[pin].value)
arduino.addListener("publishPinArray","python","publishPin")

print "start to poll pin input"
arduino.enablePin(13, 1)
sleep(5)
print "stop to poll pin input"
arduino.disablePin(13)