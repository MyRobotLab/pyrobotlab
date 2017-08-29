arduino = Runtime.createAndStart("arduino", "Arduino")
arduino.connect("COM11")

def test(data):
  print data

arduino.addListener("publishCustomMsg","python","test")

arduino.customMsg(55,44)
