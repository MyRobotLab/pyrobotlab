# variables dependent on your setup

boardType = "atmega2560"  # atmega168 | atmega328p | atmega2560 | atmega1280 | atmega32u4
comPort = "COM8" # com4 for atmega328 com8 for mega2560
SHIFT = 47
LATCH = 48
DATA = 49


# start Arduino service named arduino
arduino = Runtime.createAndStart("arduino", "Arduino")
arduino.setBoard(boardType) # atmega168 | mega2560 | etc
arduino.connect(comPort)
# set pinMode
arduino.pinMode(SHIFT, Arduino.OUTPUT)
arduino.pinMode(LATCH, Arduino.OUTPUT)
arduino.pinMode(DATA, Arduino.OUTPUT)


# Create shiftOut fonction
def shiftOut(value):
	arduino.digitalWrite(LATCH, arduino.LOW)		# Stop the copy
	for byte in value:
		if byte == 1 :
			arduino.digitalWrite(DATA,arduino.HIGH)  
		else :
			arduino.digitalWrite(DATA,arduino.LOW)
		arduino.digitalWrite(SHIFT, arduino.HIGH) 
		arduino.digitalWrite(SHIFT, arduino.LOW)
	arduino.digitalWrite(LATCH, arduino.HIGH)	# copy    

# leds patterns
# smile = 00111011
# notHappy = "01111100"
# speechLess = "00111101"
# Speaking B00000000,B00100000,B00111000,B00100000,B10000000

def smile():
	shiftOut([1,1,0,1,1,1,0,0]) #	send data
def notHappy():	
	shiftOut([0,0,1,1,1,1,1,0]) #	send data
def speechLess():
	shiftOut([1,0,1,1,1,1,0,0]) # send data
def talk():
	shiftOut([0,0,0,0,0,0,0,0]) #	send data
	sleep(0.05)
	shiftOut([0,0,0,0,0,1,0,0]) #	send data
	sleep(0.05)
	shiftOut([0,0,0,1,1,1,0,0]) #	send data
	sleep(0.05)
	shiftOut([0,0,0,0,0,1,0,0]) #	send data
	sleep(0.05)

while (1) :
	smile()
	sleep(1)
	notHappy()
	sleep(1)
	speechLess()
	for i in range(0,10) :
		talk()
