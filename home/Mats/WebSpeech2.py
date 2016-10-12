from java.lang import String
 
######################################################################
# A helper function to print the recognized text to the python window.
# semi-useful for debugging.
######################################################################
def heard(data):
  print "Speech Recognition Data:", data

######################################################################
# Create a hook to python
######################################################################
python = Runtime.createAndStart("python", "Python")
######################################################################
# Create ProgramAB chat bot
######################################################################
lloyd = Runtime.createAndStart("lloyd", "ProgramAB")
lloyd.startSession("kevin", "alice2")

######################################################################
# create the speech recognition service
# Speech recognition is based on WebSpeechToolkit API
######################################################################
# Start the new WebGuiREST API for MRL
webgui = Runtime.createAndStart("webgui","WebGui")
######################################################################
# Create the webkit speech recognition gui
######################################################################
wksr = Runtime.createAndStart("webkitspeechrecognition", "WebkitSpeechRecognition")
######################################################################
# create the html filter to filter the output of program ab
######################################################################
htmlfilter = Runtime.createAndStart("htmlfilter", "HtmlFilter")
 
######################################################################
# create the speech to text service (named the same as the inmoov's)
######################################################################
mouth = Runtime.createAndStart("i01.mouth", "AcapelaSpeech")
mouth.setVoice("Will")
######################################################################
# MRL Routing webkitspeechrecognition -> program ab -> htmlfilter -> inmoov
#####################################################################
# add a link between the webkit speech to publish to ProgramAB
wksr.addTextListener(lloyd)
# Add route from Program AB to html filter
lloyd.addTextListener(htmlfilter)
# Add route from html filter to mouth
htmlfilter.addTextListener(mouth)
# Send a question to ProgramAB
def askPgmAB(text):
	mouth.speakBlocking(text)
	lloyd.onText(text)
sleep(5)
askPgmAB("Your name is Robyn")
sleep(5)
askPgmAB("What is your name?")
sleep(5)
askPgmAB("What time is it?")
sleep(5)
