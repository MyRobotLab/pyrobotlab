# This part will execute every time the left eye changes position
# and will make the right eye servo move in sync with the left
# This also allows for a point to adjust any offset between the eyes
# and also the posibility to have the servos move in opposite direction
def onServoEvent(pos):
	eyeXR.moveTo(pos)
# Get the handle to the Python service
python = Runtime.getService("python")
# Start the Arduino service and connect to it
arduino = Runtime.createAndStart("arduino","Arduino")
arduino.connect("COM5")
# Start the left eye and set it's rest position
# Left eye
eyeXL = Runtime.createAndStart("eyeXLeft","Servo")
eyeXL.setRest(90)
eyeXL.attach(arduino,10)
eyeXL.rest()
# Start the right eye and set it's rst position
# Right Eye
eyeXR = Runtime.createAndStart("eyeXRight","Servo")
eyeXR.setRest(90)
eyeXR.attach(arduino,11)
eyeXR.rest()
# Add python as a listener to changes of servo positions
# and enable the pblishing of servoevents
eyeXL.addServoEventListener(python)
eyeXL.eventsEnabled(True)
