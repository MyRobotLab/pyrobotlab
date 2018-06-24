#########################################
# Small script to access InMoov chatbot through python script
#########################################
Language = "en"

def heard(data):
  print "Speech Recognition Data:"+str(data)

# create a ProgramAB service and start a session
Runtime.createAndStart("htmlFilter", "HtmlFilter")
chatBot=Runtime.start("chatBot", "ProgramAB")
chatBot.setPath("C:\mrl\myrobotlab.1.0.2693\InMoov\chatbot")
chatBot.startSession("default",Language)

# Start the WebGui service without starting the browser
WebGui = Runtime.create("WebGui","WebGui")
WebGui.autoStartBrowser(False)
WebGui.startService()

# Then start the browsers and show the WebkitSpeechRecognition service named webkitspeechrecognition
WebGui.startBrowser("http://localhost:8888/#/service/ear")
ear = Runtime.start("ear","WebkitSpeechRecognition")
ear.setLanguage("en")
ear.addListener("publishText", python.name, "heard");

# create a Speech service
mouth = Runtime.start("mouth", "MarySpeech")
mouth.installComponentsAcceptLicense("cmu-bdl-hsmm")
mouth.setVoice("cmu-bdl-hsmm")

# auto rearm microphone
ear.setAutoListen(True)
# speedup recognition if False
ear.setContinuous(False)

######################################################################
# MRL Routing ear -> program ab -> htmlfilter -> mouth
######################################################################
htmlfilter = Runtime.createAndStart("htmlfilter", "HtmlFilter")
ear.addMouth(mouth)
ear.addTextListener(chatBot)
chatBot.addTextListener(htmlfilter)
htmlfilter.addTextListener(mouth)
