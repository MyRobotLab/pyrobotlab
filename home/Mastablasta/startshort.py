import random
from java.lang import String
holygrail = Runtime.createAndStart("holygrail", "WebGui")
wksr = Runtime.createAndStart("webkitspeechrecognition", "WebkitSpeechRecognition")
alice2 = Runtime.createAndStart("alice2", "ProgramAB")
alice2.startSession("ProgramAB", "User", "alice2")
htmlfilter = Runtime.createAndStart("htmlfilter", "HtmlFilter")
mouth = Runtime.createAndStart("i01.mouth", "MarySpeech")
wksr.addTextListener(alice2)
alice2.addTextListener(htmlfilter)
htmlfilter.addTextListener(mouth)
