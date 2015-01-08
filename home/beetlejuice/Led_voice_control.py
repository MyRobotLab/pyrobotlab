from java.lang import String
from org.myrobotlab.service import Speech
from org.myrobotlab.service import Sphinx
from org.myrobotlab.service import Runtime
from time import sleep
from org.myrobotlab.service import Arduino
 
# This is a little speech recognition script.
# Use "Led On" or "Led off" to control the led .
# The led is connected on pin 13 by default
# Change the value of the variable "ledPin" if you connect the led on an other pin 
# Set the right com port in the variable " comPort " and the right arduino board
 
 
# set the pin for the led
ledPin = 13
 
# set the com port for the arduino
comPort = "COM4"
 
# create ear and mouth
ear = Runtime.createAndStart("ear","Sphinx")
mouth = Runtime.createAndStart("mouth","Speech")
 
# create an Arduino service named arduino
arduino = Runtime.createAndStart("arduino","Arduino")
 
# set the board type
arduino.setBoard("atmega328") # atmega168 | mega2560 | etc
 
# set serial device
arduino.setSerialDevice(comPort,57600,8,1,0)
sleep(1) # give it a second for the serial device to get ready
 
# update the gui with configuration changes
arduino.publishState()

# Test arduino
arduino.digitalWrite(ledPin,1)
sleep(1) # sleep half a second 
arduino.digitalWrite(ledPin,0)
# start listening for the words we are interested in
ear.startListening("led on | led off | test")
 
# set up a message route from the ear --to--> python method "heard"
ear.addListener("recognized", python.name, "heard", String().getClass()); 
 
# this method is invoked when something is 
# recognized by the ear - in this case we
# actuate the led state and print the word recognized
 
def heard():
      data = msg_ear_recognized.data[0]
      print "heard ", data
      if (data == "led on"):
         print "Turning on the light" 
         arduino.digitalWrite(ledPin,1)
         sleep(0.5) # sleep half a second
         mouth.speak("The led is on ")
      elif (data == "led off"):
         print  "Turning off the light"
         arduino.digitalWrite(ledPin,0)
         sleep(0.5) # sleep half a second
         mouth.speak("The led is off ")
      elif (data == "test"):
      	print  "The system is ok"
      	arduino.digitalWrite(ledPin,0)
      	sleep(0.5) # sleep half a second
      	mouth.speak("The system is ok ")
    # ... etc
 
# prevent infinite loop - this will suppress the
# recognition when speaking - default behavior
# when attaching an ear to a mouth :)
ear.attach("mouth")
