arduino = Runtime.createAndStart("arduino","Arduino")
arduino.connect("COM11")

bno = Runtime.createAndStart("bno","Bno055")
bno.setController(arduino)
if bno.begin():
  print bno.getEvent().orientation.x
  print bno.getEvent().orientation.y
  print bno.getEvent().orientation.z
