###############################

from org.myrobotlab.service import Runtime

from java.lang import String

Ghost = Runtime.createAndStart("Ghost", "WebGui")

wksr = Runtime.createAndStart("webkitspeechrecognition", "WebkitSpeechRecognition")

ghostchat = Runtime.createAndStart("ghostchat", "ProgramAB")

ghostchat.startSession("ProgramAB/bots", "ghostchat")

htmlfilter = Runtime.createAndStart("htmlfilter", "HtmlFilter")

NaturalReaderSpeech = Runtime.createAndStart("speech", "NaturalReaderSpeech")

voices = NaturalReaderSpeech.getVoices()

for voice in voices:  //I've also tried removing this because I got an iteration error for this line

          NaturalReaderSpeech.setVoice("Ryan")

wksr.addTextListener(ghostchat)

ghostchat.addTextListener(htmlfilter)

htmlfilter.addTextListener(NaturalReaderSpeech)
