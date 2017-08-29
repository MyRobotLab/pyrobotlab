import random
from org.myrobotlab.service import Arduino
from org.myrobotlab.service import Servo
from org.myrobotlab.service import Runtime
from java.lang import String
from time import sleep
holygrail = Runtime.createAndStart("holygrail", "WebGui")
wksr = Runtime.createAndStart("webkitspeechrecognition", "WebkitSpeechRecognition")
simple = Runtime.createAndStart("simple", "ProgramAB")
simple.startSession("default", "simple")
htmlfilter = Runtime.createAndStart("htmlfilter", "HtmlFilter")
acapelaSpeech = Runtime.createAndStart("speech", "AcapelaSpeech")
voices = acapelaSpeech.getVoices()
for voice in voices:
    acapelaSpeech.setVoice("Ryan")
wksr.addTextListener(simple)
simple.addTextListener(htmlfilter)
htmlfilter.addTextListener(acapelaSpeech)
