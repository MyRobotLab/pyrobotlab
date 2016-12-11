# Gas sensor MQ2 
# reads a butane sensor on analog 5
# waits for voice control from user before speaking back the butane level measured

from java.lang import String
from org.myrobotlab.service import Speech
from org.myrobotlab.service import Sphinx
from org.myrobotlab.service import Runtime 
ear = Runtime.createAndStart("ear","Sphinx")
mouth = Runtime.createAndStart("mouth","Speech")

ear.startListening("hi james|gas levels please|again")

ear.addListener("recognized", python.name, "heard");
arduino = Runtime.createAndStart("arduino","Arduino")
arduino.connect("COM4")
 
readAnalogPin = 5  # butane sensor MQ2 is wired to analog 5

# arduino.setSampleRate(8000)   # make friendly sample rate

butain=0    # butane level variable
global butane

arduino.addListener("publishPin", "python", "publishPin")   # add call back route
def heard(data):
      global butane
      #print "heard ", data
      if (data == "hi james"):
         #mouth.speak("hi james")
         mouth.speak("hi gareth")
         mouth.speak("how can i help you")
      elif (data == "gas levels please"):  
         print ("give me gas levels please") 
         mouth.speak("for sure")
         mouth.speak(str(butane))
         mouth.speak("parts per million")   # p.p.m needs to be calibrated for this 
      elif (data == "again"):  
         print ("give me gas levels please") 
         mouth.speak(str(butane))
         mouth.speak("parts per million")   # p.p.m needs to be calibrated for this 
          
# my call-back
def publishPin(pin):
 global butane
 butane= pin.value
 print butane
 
# get data from analog pin for 5 seconds
arduino.arduino.enablePin(readAnalogPin)
sleep(200)
arduino.arduino.disablePin(readAnalogPin) 
ear.attach("mouth") 
