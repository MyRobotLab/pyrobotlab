#AndroidSpeechRecognition combined with Speech
from java.lang import String

#creating services
asr = Runtime.start("asr", "AndroidSpeechRecognition")
speech = Runtime.start("speech", "Speech")

#recognition-def
def heard(data):
 print data
 speech.speakBlocking(data);
 #asr.sendToClient(data);
 asr.startRecognition();

#adding listener
asr.addListener("recognized", python.name, "heard", String().getClass());
