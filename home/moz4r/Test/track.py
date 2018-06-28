servoPin01 = 4
servoPin02 = 5
port = "COM15"

# create a servo controller and a servo
arduino = Runtime.start("arduino","Arduino")
servo01 = Runtime.start("servo01","Servo")
servo02 = Runtime.start("servo02","Servo")
arduino.connect(port)
servo01.attach(arduino.getName(), servoPin01)
servo02.attach(arduino.getName(), servoPin02)
def trackHumans():
  servo01.setVelocity(30)
  servo02.setVelocity(30)
  servo01.moveTo(90)
  servo02.moveTo(90)
  tracker = Runtime.start("tracker", "Tracking")
  opencv=tracker.getOpenCV()
  pid = tracker.getPID()
  # these are default setting
  # adjust to make more smooth
  # or faster
  pid.setPID("x",20.0, 5.0, 0.1)
  pid.setPID("y",20.0, 5.0, 0.1)
  tracker.connect(opencv, servo01, servo02)
  tracker.faceDetect(False)
  servo01.setVelocity(-1)
  servo02.setVelocity(-1)
  
trackHumans()
