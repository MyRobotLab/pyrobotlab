
mouth = Runtime.createAndStart("i01.mouth","NaturalReaderSpeech")


arduino = Runtime.createAndStart("arduino","Arduino")
arduino.connect("COM4")

arduino.enablePin("54") 
arduino.enablePin("55") 

pin0 = 54
pin1 = 55

left = 300
right = 300

leftstedy = 600
rightstedy = 600

leftval = left - leftstedy
rightval = right - rightstedy

arduino.analogReadPollingStart(pin0)
arduino.analogReadPollingStart(pin1)

# make friendly sample rate
arduino.setSampleRate(1000)

arduino.addListener("publishPin", "python", "publishPin")

mouth.speak("starting")

# my call-back
def publishPin(pin):
  global publishPin

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
  
  if (leftval >= rightval + 30 ):
    arduino.removeListener("publishPin", "python", "publishPin")
    mouth.speak("left")
    sleep(3)
    arduino.addListener("publishPin", "python", "publishPin")


  elif (rightval >= leftval + 30 ):
    arduino.removeListener("publishPin", "python", "publishPin")
    mouth.speak("right")
    sleep(3)
    arduino.addListener("publishPin", "python", "publishPin")

    
#  print left
#  print leftstedy
#  print right
#  print rightstedy
  print leftval
  print rightval
 
