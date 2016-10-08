arduino = Runtime.createAndStart("arduino","Arduino")
arduino.connect("COM11")

bno = Runtime.createAndStart("bno","Bno055")
bno.setController(arduino)
if bno.begin():
  event = bno.getEvent()
  print event.orientation.x
  print event.orientation.y
  print event.orientation.z
