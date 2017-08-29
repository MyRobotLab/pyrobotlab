# A script to show how to syncronize two servos using the publish / subscribe pattern
# Works from version 1.0.1739
speech = Runtime.createAndStart("Speech","AcapelaSpeech")
speech.setVoice("Will")
speech.speakBlocking("Startting Arduino")
# Minimal script to syncronize 2 servos
arduino = Runtime.createAndStart("Arduino","Arduino")
arduino.connect("/dev/ttyACM0")
# Connect the left eye
leftEyeX = Runtime.createAndStart("LeftEyeX","Servo")
leftEyeX.attach(arduino,10)
# Remap the left eye since it is 10 degrees offset to the right
leftEyeX.map(0,180,-10,170)
# Connect the right eye
rightEyeX = Runtime.createAndStart("RightEyeX","Servo")
rightEyeX.setMinMax(60,120)
rightEyeX.setRest(90)
rightEyeX.attach(arduino,11)
rightEyeX.rest()
# Make the left eye follow the right
rightEyeX.addServoEventListener(leftEyeX)
rightEyeX.eventsEnabled(True)
def lookRight():
	rightEyeX.moveTo(120)
	speech.speakBlocking("Looking right")
def lookLeft():
	rightEyeX.moveTo(60)
	speech.speakBlocking("Looking left")
def lookForward():
	rightEyeX.rest()
	speech.speakBlocking("Looking forward")
lookRight()
lookLeft()
lookForward()
