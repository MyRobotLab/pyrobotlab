# A small script to test tracking
from org.myrobotlab.opencv import OpenCVFilterAffine
#
cameraIndex = 0
port = 'COM3'
arduino = Runtime.start("tracker.controller","Arduino")
sleep(5)
arduino.connect(port)
sleep(4)
x = Runtime.start("tracker.x","Servo")
y = Runtime.start("tracker.y","Servo")
# y.setInverted(True)
sleep(5)
x.attach(arduino,8)
x.setVelocity(25)
y.attach(arduino,12)
y.setMinMax(60,140)
#
tracker = Runtime.start("tracker","Tracking")
affine = OpenCVFilterAffine("affine")
affine.setAngle(180.0)
opencv = Runtime.getService("tracker.opencv")
tracker.preFilters.add(affine)
opencv.setDisplayFilter("affine")
def restart():
	print 'Facedetect started'
	tracker.faceDetect()
	sleep(30)
	print 'Facedetect stop'
	tracker.stopTracking()
	x.rest()
	y.rest()
	sleep(3)
while (1==1):
	restart()	
