from org.myrobotlab.service import Speech
mouth = Runtime.createAndStart("mouth","Speech")

arduino = Runtime.createAndStart("arduino","Arduino")
arduino.connect("COM4")

Pin0 = 14
Pin1 = 15

pin0 = None
pin1 = None

Ana0 = 10

arduino.analogReadPollingStart(Pin0)
arduino.analogReadPollingStart(Pin1)

# make friendly sample rate
arduino.setSampleRate(8000)

arduino.addListener("publishPin", "python", "publishPin")

# my call-back
def publishPin(pin):

  #print pin.value

  if (pin.pin == 14):
    print("pin14.value ", pin.value)
    pin0 = pin
    if (pin.value >= 500):
      mouth.speak("pin 0")
      sleep(2)
    
  elif (pin.pin == 15):
    print("pin15.value ", pin.value)
    pin1 = pin
    if (pin.value >= 500):
      mouth.speak("pin 1")
      sleep(2)
  
  if (pin0.value >= pin1.value ):
    print("pin0 is greater than pin1")


#  print pin.pin, pin.value, pin.type, pin.source,
