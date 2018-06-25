# servo events


arduino = Runtime.start("arduino","Arduino")
eyelid = Runtime.start("eyelid","Servo")
eyebrows = Runtime.start("eyebrows","Servo")

arduino.connect("COM15")

# set limits
eyelid.map(0, 180, 10, 120)
eyebrows.map(0, 180, 0, 180)

eyelid.setVelocity(50)
eyebrows.setVelocity(30)

eyelid.attach(arduino.getName(), 1)
eyebrows.attach(arduino.getName(), 2)

eyelid.moveToBlocking(180)
eyelid.moveToBlocking(0)
eyelid.moveToBlocking(180)
eyelid.moveToBlocking(0)

# listen for position events
python.subscribe(eyelid,"publishServoEvent")

def onServoEvent(data):
  if data>90:
    eyebrows.moveTo(180)
  else:
    eyebrows.moveTo(0)
