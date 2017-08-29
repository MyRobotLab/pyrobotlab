######################################################################
# Create the webkit speech recognition gui
######################################################################
wksr = Runtime.createAndStart("webkitspeechrecognition", "WebkitSpeechRecognition")
######################################################################
# create the html filter to filter the output of program ab
######################################################################
htmlfilter = Runtime.createAndStart("htmlfilter", "HtmlFilter")
######################################################################
# the mouth
######################################################################
mouth = Runtime.createAndStart("mouth", "AcapelaSpeech")

voices = mouth.getVoices()
for voice in voices:
    mouth.setVoice("Vittorio")

# add a link between the webkit speech to publish to ProgramAB
wksr.addTextListener(jarvis)
# Add route from Program AB to html filter
jarvis.addTextListener(htmlfilter)
# Add route from html filter to mouth
htmlfilter.addTextListener(mouth)
