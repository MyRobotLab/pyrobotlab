# Sweety's motors test
import random

Runtime.createAndStart("sweety", "Sweety")
sweety.arduino.setBoard("atmega2560")
sweety.connect("COM8")
sleep(1) # give a second to the arduino for connect
sweety.attach()
sweety.posture("neutral")
sweety.mouthState("smile")
sleep(1)

joystick = runtime.createAndStart("joystick","Joystick")
joystick.setController(3) # Set controller index
joystick.startPolling() # Start the polling of the device this

#create a message route from joy to python so we can listen for button
joystick.addXListener("python", "x")
joystick.add0Listener("python", "a")
joystick.addYListener("python", "y")

# Joystick
move = False
vitesseMax = 75

def y(data):
	global vitesseMax
	data = data * -1 # invert
	vitesse = int(255*data)
	if (vitesse > vitesseMax ) :
		vitesse = vitesseMax
	if (vitesse < vitesseMax * -1) :
		vitesse = vitesseMax * -1
	sweety.moveMotors(vitesse,0)
	return

def x(data):
	global vitesseMax
	vitesse = int(255*data)
	if (vitesse > vitesseMax ) :
		vitesse = vitesseMax
	if (vitesse < vitesseMax * -1) :
		vitesse = vitesseMax * -1
	sweety.moveMotors(0, vitesse)
	return
    
def a(data):
	sweety.moveMotors(0,0)
	return

 
#create a message route from joy to python so we can listen for button
joystick.addListener("XAxisRaw", python.getName(), "x")
joystick.addListener("button0", python.getName(), "a")
joystick.addListener("YAxisRaw", python.getName(), "y")
