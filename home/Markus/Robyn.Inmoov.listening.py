from org.myrobotlab.service import Speech
mouth = Runtime.createAndStart("mouth","Speech")
from org.myrobotlab.service import Servo

servo1 = Runtime.create("servo1","Servo")
servo1.startService()

arduino = Runtime.createAndStart("arduino","Arduino")
arduino.connect("COM3")

pin0 = 54
pin1 = 55

left = 300
right = 300

leftstedy = 600
rightstedy = 600

servo1.attach("arduino", 13)

servo1.setSpeed(0.8)

arduino.analogReadPollingStart(pin0)
arduino.analogReadPollingStart(pin1)

# make friendly sample rate
arduino.setSampleRate(1000)

arduino.addListener("publishPin", "python", "publishPin")

# my call-back
def publishPin(pin):

  if (pin.pin == 54):
    pin0 = pin
    global left
    left = (left + pin0.value) / 2
    global leftstedy
    leftstedy = ((leftstedy * 29) + pin0.value) / 30    
    
  elif (pin.pin == 55):
    pin1 = pin
    global right
    right = (right + pin1.value) / 2 
    global rightstedy
    rightstedy = ((rightstedy * 29) + pin1.value) / 30   
  
  if (left >= leftstedy + 50 ):
    mouth.speak("pin 0")
    servo1.moveTo(50)
    sleep (4)

  elif (right >= rightstedy + 50 ):
    mouth.speak("pin 1")
    servo1.moveTo(130)
    sleep (4)


    
  print left
  print leftstedy
  print right
  print rightstedy
