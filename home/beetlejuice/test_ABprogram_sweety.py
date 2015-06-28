# Sweety's service
import random
from java.lang import String

Runtime.createAndStart("sweety", "Sweety")
sweety.arduino.setBoard("atmega2560")
sweety.connect("COM8")
sleep(1) # give a second to the arduino for connect
sweety.attach()
sweety.posture("neutral")
sweety.mouthState("smile")
sweety.mouth.setGoogleURI("http://thehackettfamily.org/Voice_api/api2.php?voice=Rod&txt=")

sweety.chatBot.startSession("ProgramAB", "default", "sweety")
######################################################################
# create the speech recognition service
######################################################################
pats = sweety.chatBot.listPatterns("chatBot")
# create the grammar for the speech recognition service
sphinx_grammar = "|".join(pats)
sweety.ear.startListening(sphinx_grammar)

######################################################################
# MRL Routing   sphinx -> program ab -> htmlfilter -> sweety
######################################################################
# add a route from Sphinx to ProgramAB
sweety.ear.addTextListener(sweety.chatBot)
 
# Add route from Program AB to html filter
sweety.chatBot.addTextListener(sweety.htmlFilter)
# Add route from html filter to mouth
sweety.htmlFilter.addListener("publishText", python.name, "talk", String().getClass());
 
# make sure the ear knows if it's speaking.
sweety.ear.attach(sweety.mouth)

def talk(data):
	sweety.saying(data)
  	print "Saying :", data
