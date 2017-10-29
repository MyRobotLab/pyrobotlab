# crash test FaceRecognizer + faceDetect
port = "COM19"   
xServoPin = 13
yServoPin = 12

tracker = Runtime.start("tracker", "Tracking")
gui = Runtime.start("gui", "SwingGui")
opencv=tracker.getOpenCV()

servoX = tracker.getX()
servoX.setMinMax(30, 150) 

servoY = tracker.getY()
servoY.setMinMax(30, 150)
pid = tracker.getPID()

pid.setPID("x",5.0, 5.0, 0.1)
pid.setPID("y",5.0, 5.0, 0.1)

# optional filter settings
opencv = tracker.getOpenCV()

# not for you, it's for test
virtual=1
if ('virtual' in globals() and virtual):
  virtualArduino = Runtime.start("virtualArduino", "VirtualArduino")
  virtualArduino.connect(port)
  
# connect to the Arduino ( 0 = camera index )
tracker.connect(port, xServoPin, yServoPin, 0)

if ('virtual' in globals() and virtual):
  opencv.stopCapture()
  opencv.setMinDelay(500)
  opencv.setMinDelay(500)
  opencv.captureFromImageFile("resource/OpenCV/testData/ryan.jpg")

tracker.faceDetect()
fr=opencv.addFilter("FaceRecognizer")