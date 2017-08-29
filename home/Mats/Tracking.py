# A small script to test tracking
from org.myrobotlab.opencv import OpenCVFilterAffine
#
cameraIndex = 0
port = 'COM3'
arduino = Runtime.start("tracker.controller","Arduino")
pid = Runtime.start("tracker.pid","Pid")
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
pid.setPID("x", 20.0, 5.0, 0.1);
pid.setPID("y", 20.0, 5.0, 0.1);
affine = OpenCVFilterAffine("affine")
affine.setAngle(180.0)
opencv = Runtime.getService("tracker.opencv")
tracker.preFilters.add(affine)
opencv.setDisplayFilter("affine")
tracker.faceDetect()

