#AndroidVoiceRecognition combined with Speech & ProgramAB
from java.lang import String
 
#creating services
avr = Runtime.start("avr", "AndroidVoiceRecognition")
speech = Runtime.start("speech", "Speech")
pab = Runtime.start("pab", "ProgramAB")
pab.startSession()
 
#recognition-def
def heard(data):
 print data
 resp = pab.getResponse(data)
 print resp
 #speech.speakBlocking(resp)
 #avr.sendToClient(data)
 avr.startRecognition()
 
#adding listeners
avr.addListener("recognized", python.name, "heard", String().getClass())
pab.addTextListener(speech)
