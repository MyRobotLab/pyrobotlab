 
arduino = Runtime.createAndStart("arduino", "Arduino")
arduino.connect("COM1") # change this

readAnalogPin = 0 # change this
arduino.setSampleRate(9600)  # change this
arduino.addListener("publishPin", "python", "publishPin")
arduino.analogReadPollingStart(readAnalogPin)

def publishPin(pin):
  print pin.pin, pin.value
  if (pin.value >= X):
     print ("hello world")