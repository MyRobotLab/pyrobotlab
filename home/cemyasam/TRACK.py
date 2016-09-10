# a minimal tracking script - this will start all peer
# services and attach everything appropriately
# change parameters depending on your pan tilt, pins and
# Arduino details
# all commented code is not necessary but allows custom
# options

port = "COM6"   #change COM port to your own port
xServoPin = 7   #change this to the right servo pin if needed, for inmoov this is right
yServoPin = 8   #change this to the right servo pin if needed, for inmoov this is right

# Create the arduino service
arduino = Runtime.createAndStart("tracker.arduino", "Arduino")
# connect the arduino service to the specified port
arduino.connect(port)

# create the tracker.x servo and attach it with min/max values to the arduino
servoX = Runtime.createAndStart("tracker.x", "Servo")
servoX.attach(arduino, xServoPin)
servoX.setMinMax(30, 150)  #minimum and maximum settings for the X servo
# servoX.setInverted(True) # invert if necessary

# create the tracker.y servo and attach it with min/max values to the arduino
servoY = Runtime.createAndStart("tracker.y", "Servo")
servoY.attach(arduino, yServoPin)
servoY.setMinMax(30, 150)  #minimum and maximum settings for the Y servo
# servoY.setInverted(True) # invert if necessary

# start the tracker service
tracker = Runtime.createAndStart("tracker", "Tracking")

# changing PID values change the 
# speed and "jumpyness" of the Servos
# pid = tracker.getPID()

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

# diffrent types of tracking

# simple face detection and tracking
# tracker.faceDetect()

# lkpoint - click in video stream with 
# mouse and it should track
tracker.startLKTracking()

# scans for faces - tracks if found
# tracker.findFace() 

