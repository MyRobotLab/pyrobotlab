from org.myrobotlab.service import Speech
mouth = Runtime.createAndStart("mouth","Speech")

arduino = Runtime.createAndStart("arduino","Arduino")
arduino.connect("COM4")

Pin0 = 14
Pin1 = 15

Ana0 = 10

arduino.analogReadPollingStart(Pin0)
arduino.analogReadPollingStart(Pin1)

# make friendly sample rate
arduino.setSampleRate(8000)

arduino.addListener("publishPin", "python", "publishPin")

# my call-back
def publishPin(pin):

  print pin.value

  if (pin.pin == 14 and pin.value >= 500):
    mouth.speak("pin 0")
    sleep(2)
    
  elif (pin.pin == 15 and pin.value >= 500):
    mouth.speak("pin 1")
    sleep(2)


#  print pin.pin, pin.value, pin.type, pin.source,