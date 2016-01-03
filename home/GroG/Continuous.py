from java.lang import String
from org.myrobotlab.service import Speech
from org.myrobotlab.service import Sphinx
from org.myrobotlab.service import Runtime
  
# create mouth arduino and servo
ear = Runtime.createAndStart("ear","Sphinx")
arduino = Runtime.createAndStart("arduino","Arduino")
arduino.connect("COM4")
servo = Runtime.createAndStart("servo","Servo")
servo.attach(arduino, 10)
  
# start listening for the words we are interested in
ear.startListening("go forward|go backwards|stop")
  
# set up a message route from the ear --to--> python method "heard"
ear.addListener("recognized", python.name, "heard", String().getClass()); 
  
# this method is invoked when something is 
# recognized by the ear - in this case we
# have the mouth "talk back" the word it recognized
def heard(phrase):
      print("I heard ", phrase)
      if phrase == "go forward":
        servo.moveTo(170)
      elif phrase == "go backwards":
        servo.moveTo(10)
      elif phrase == "stop":
        servo.moveTo(90)
      
