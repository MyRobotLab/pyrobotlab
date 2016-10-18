# a minimal tracking script - this will start all peer
# services and attach everything appropriately
# change parameters depending on your pan tilt, pins and
# Arduino details
# all commented code is not necessary but allows custom
# options

port = "/dev/ttyACM0"
xServoPin = 11
yServoPin = 10

tracker = Runtime.createAndStart("tracker", "Tracking")

# set specifics on each Servo
servoX = tracker.getX()
servoX.setPin(xServoPin)
servoX.setMinMax(30, 130)

servoY = tracker.getY()
servoY.setPin(yServoPin)
servoY.setMinMax(30, 130)

# changing PID values change the 
# speed and "jumpyness" of the Servos
xpid = tracker.getXPID()
ypid = tracker.getYPID()

# these are default setting
# adjust to make more smooth
# or faster
# xpid.setPID(5.0, 5.0, 0.1)
# ypid.setPID(5.0, 5.0, 0.1)

# optional filter settings
opencv = tracker.getOpenCV()

# setting camera index to 1 default is 0
opencv.setCameraIndex(1) 

# connect to the Arduino
tracker.connect(port)

# Gray & PyramidDown make face tracking
# faster - if you dont like these filters - you
# may remove them before you select a tracking type with
# the following command
# tracker.clearPreFilters()

# simple face detection and tracking
tracker.faceDetect()

# scans for faces - tracks if found
# tracker.findFace()
