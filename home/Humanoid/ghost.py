###################################################
# This is a basic script to carry on a conversation
# with ghost
###################################################

# create service 
ghost = Runtime.start("ghost", "WebGui")
ear = Runtime.start("ear", "WebkitSpeechRecognition")
ghostchat = Runtime.start("ghostchat", "ProgramAB")
htmlfilter = Runtime.start("htmlfilter", "HtmlFilter")
mouth = Runtime.start("mouth", "NaturalReaderSpeech")

# start a chatbot session
ghostchat.startSession("ProgramAB/bots", "ghostchat")

voices = mouth.getVoices()
# I've also tried removing this because I got an iteration error for this line
# for voice in voices:  
#          NaturalReaderSpeech.setVoice("Ryan")

# - I'll need to check on these - might
# need to just "attach" some services together
ear.addTextListener(ghostchat)
ghostchat.addTextListener(htmlfilter)
htmlfilter.addTextListener(mouth)
