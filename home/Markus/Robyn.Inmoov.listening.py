from org.myrobotlab.service import Speech
mouth = Runtime.createAndStart("mouth","Speech")
from org.myrobotlab.service import Servo

servo1 = Runtime.create("servo1","Servo")
servo2 = Runtime.create("servo2","Servo")
servo1.startService()
servo2.startService()

arduino = Runtime.createAndStart("arduino","Arduino")
arduino.connect("COM3")

pin0 = 54
pin1 = 55

left = 300
right = 300

leftstedy = 600
rightstedy = 600

leftval = left - leftstedy
rightval = right - rightstedy

servo1.attach("arduino", 13)
servo2.attach("arduino", 12)

servo1.setSpeed(0.8)
servo2.setSpeed(0.8)

arduino.arduino.enablePin(pin0)
arduino.arduino.enablePin(pin1)

# make friendly sample rate
# arduino.setSampleRate(1000)

arduino.addListener("publishPin", "python", "publishPin")

# my call-back
def publishPin(pin):

  if (pin.pin == 54):
    pin0 = pin
    global left
    left = pin0.value
    if (left <= leftstedy ):
      global left
      left = leftstedy
    global leftstedy
    leftstedy = ((leftstedy * 49) + pin0.value) / 50    
    global leftval
    leftval = left - leftstedy
    
  if (pin.pin == 55):
    pin1 = pin
    global right
    right = pin1.value
    if (right <= rightstedy ):
      global right
      right = rightstedy
    global rightstedy
    rightstedy = ((rightstedy * 49) + pin1.value) / 50   
    global rightval
    rightval = right - rightstedy  
  
  if (leftval >= rightval + 50 ):
#    mouth.speak("pin 0")
    servo1.moveTo(30)
    sleep (4)

  elif (rightval >= leftval + 50 ):
#    mouth.speak("pin 1")
    servo1.moveTo(150)
    sleep (4)

  else :
    servo1.moveTo(90)

    
#  print left
#  print leftstedy
#  print right
#  print rightstedy
  print leftval
  print rightval
