#AndroidVoiceRecognition combined with Speech
from java.lang import String

#creating services
avr = Runtime.start("avr", "AndroidVoiceRecognition")
speech = Runtime.start("speech", "Speech")

#recognition-def
def heard(data):
 print data
 speech.speakBlocking(data);
 #avr.sendToClient(data);
 avr.startRecognition();

#adding listener
avr.addListener("recognized", python.name, "heard", String().getClass());
