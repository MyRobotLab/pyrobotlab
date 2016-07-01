# Start the Arduino
arduino = Runtime.createAndStart("Arduino","Arduino")
arduino.connect("COM4")
leftneckPin = 14
rightneckPin = 15
# Function to keep the servo movements in sync
# If both servos should rotate in the same direction, change from "- delta" to "+ delta"
def neckMoveTo(restPos,delta):
	leftneckServo.moveTo(restPos + delta)
	rightneckServo.moveTo(restPos - delta)
#	
leftneckServo = Runtime.createAndStart("leftNeck","Servo")
rightneckServo = Runtime.createAndStart("rightNeck","Servo")
leftneckServo.attach(arduino,leftneckPin)
rightneckServo.attach(arduino,rightneckPin)
restPos = 90
delta = 0
neckMoveTo(restPos,delta)
sleep(1)
delta = 45 
neckMoveTo(restPos,delta)
sleep(2)
delta = -45 
neckMoveTo(restPos,delta)
sleep(2)
delta = 0
neckMoveTo(restPos,delta)
sleep(2)
def neckMoveTo(restPos,delta):
	leftneckServo.moveTo(restPos + delta)
	rightneckServo.moveTo(restPos - delta)
