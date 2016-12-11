arduino = Runtime.createAndStart("arduino", "Arduino")
arduino.connect("COM6")

m1 = Runtime.createAndStart("m1","Motor")
arduino.motorAttach("m1", "TYPE_LPWM_RPWM", 5, 6)

readAnalogPin = 0
# arduino.setSampleRate(9600)
arduino.addListener("publishPin", "python", "publishPin")
arduino.arduino.enablePin(readAnalogPin)

def publishPin(pin):
  print pin.pin, pin.value
  if (pin.value >= 1018):
     print ("right")
     m1.move(-0.5)
  if (pin.value <= 965):
     print ("left")
     m1.move(0.5)
  if (pin.value >= 965) and (pin.value <= 1018):
     print ("stop")
     m1.stop()
