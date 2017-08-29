# Sweety's service
import random
from java.lang import String

Runtime.createAndStart("sweety", "Sweety")
sweety.chatBot.startSession("ProgramAB", "default", "sweety")
sweety.chatBot.setPredicate("default","name","unknow")


# Add route from webKitSpeechRecognition to Program AB
sweety.ear.addTextListener(sweety.chatBot)
# Add route from Program AB to html filter
sweety.chatBot.addTextListener(sweety.htmlFilter)
# Add route from html filter to mouth
sweety.htmlFilter.addListener("publishText", python.name, "talk");
 

def talk(data):
	sweety.mouth.speak(data)
  	print "Saying :", data
