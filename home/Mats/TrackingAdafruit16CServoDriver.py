port = "COM4"
xServoPin = 2
yServoPin = 3
mouthServoPin = 4

# Create the Tracker service to be able setup how it should connect before starting it 
tracker = Runtime.create("tracker","Tracking")
sleep(1)
servoX = tracker.getX()
servoY = tracker.getY() 

# Create the Adafruit16CServoDriver service to be able setup how it should connect before starting it 
servodriver = Runtime.create("servodriver","Adafruit16CServoDriver")
sleep(1)
servodriver.attach(tracker.arduino)
servodriver.startService()
servodriver.arduino.connect(port)

# Connect the servos to the pins
print "Attaching servos"
servoX.setMinMax(40,140)
servoX.setInverted(True)
servoX.attach(servodriver,xServoPin)

servoY.setMinMax(60,120)
servoY.setInverted(True)
servoY.attach(servodriver,yServoPin)

# Start face tracking
tracker.startService()
tracker.faceDetect()
