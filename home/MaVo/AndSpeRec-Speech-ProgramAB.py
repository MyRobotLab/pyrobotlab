#AndroidSpeechRecognition combined with Speech & ProgramAB
from java.lang import String
 
#creating services
asr = Runtime.start("asr", "AndroidSpeechRecognition")
speech = Runtime.start("speech", "Speech")
pab = Runtime.start("pab", "ProgramAB")
pab.startSession()
 
#recognition-def
def heard(data):
 print data
 resp = pab.getResponse(data)
 print resp
 #speech.speakBlocking(resp)
 #asr.sendToClient(data)
 asr.startRecognition()
 
#adding listeners
asr.addListener("recognized", python.name, "heard", String().getClass())
pab.addTextListener(speech)
