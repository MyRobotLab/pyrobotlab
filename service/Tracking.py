# a minimal tracking script - this will start all peer
# services and attach everything appropriately
# change parameters depending on your pan tilt, pins and
# Arduino details
# all commented code is not necessary but allows custom
# options

port = "COM19"   #change COM port to your own port
xServoPin = 13   #change this to the right servo pin if needed, for inmoov this is right
yServoPin = 12   #change this to the right servo pin if needed, for inmoov this is right

tracker = Runtime.start("tracker", "Tracking")
gui = Runtime.start("gui", "SwingGui")
opencv=tracker.getOpenCV()

# set specifics on each Servo
servoX = tracker.getX()
servoX.setMinMax(30, 150)  #minimum and maximum settings for the X servo
# servoX.setInverted(True) # invert if necessary

servoY = tracker.getY()
servoY.setMinMax(30, 150)  #minimum and maximum settings for the Y servo
# servoY.setInverted(True) # invert if necessary

# changing Pid values change the 
# speed and "jumpyness" of the Servos
# pid = tracker.getPID()

# these are default setting
# adjust to make more smooth
# or faster
# xpid.setPID(5.0, 5.0, 0.1)
# ypid.setPID(5.0, 5.0, 0.1)

# optional filter settings
opencv = tracker.getOpenCV()

# not for you, it's for test
if ('virtual' in globals() and virtual):
  virtualArduino = Runtime.start("virtualArduino", "VirtualArduino")
  virtualArduino.connect(port)
  
# connect to the Arduino ( 0 = camera index )
tracker.connect(port, xServoPin, yServoPin, 0)

if ('virtual' in globals() and virtual):
  opencv.stopCapture()
  opencv.setMinDelay(500)
  opencv.setFrameGrabberType("org.bytedeco.javacv.FFmpegFrameGrabber")
  opencv.setInputSource("file")
  opencv.setInputFileName("resource/OpenCV/testData/monkeyFace.mp4")

gui.undockTab("tracker.opencv")
opencv.broadcastState();
sleep(1)

# Gray & PyramidDown make face tracking
# faster - if you dont like these filters - you
# may remove them before you select a tracking type with
# the following command
# tracker.clearPreFilters()

# diffrent types of tracking

# lkpoint - click in video stream with 
# mouse and it should track
# simple point detection and tracking
# tracker.startLKTracking()
tracker.faceDetect()

# scans for faces - tracks if found
# tracker.findFace()