# file : chatbot.py

#aimlPath = "c:\mrl\marvinDialog"
aimlPath = "C:\mrl\mrl_2132\inmoov\inmoovVocal"
aimlBotName = "de"
aimlUserName = "juerg"
botVoice = "dfki-pavoque-neutral-hsmm"

# Start InMoov
i01 = Runtime.createAndStart("i01","InMoov")

######################################################################
# create the speaking service 
######################################################################
i01.mouth = Runtime.createAndStart("mouth", "MarySpeech")
i01.mouth.setVoice(botVoice)

i01.startMouth()


######################################################################
# Create the command listener
######################################################################
ear = Runtime.createAndStart("i01.ear", "WebkitSpeechRecognition")
ear.setLanguage("de-DE")

######################################################################
# Create ProgramAB chat bot
######################################################################
marvin = Runtime.createAndStart("marvin", "ProgramAB")
marvin.setPath(aimlPath)
marvin.startSession(aimlUserName, aimlBotName)

######################################################################
# create the html filter to filter the output of programAB
######################################################################
htmlfilter = Runtime.createAndStart("htmlfilter", "HtmlFilter")


######################################################################
# MRL Routing listener -> chatbot -> htmlfilter -> speaker
######################################################################
ear.addListener("publishText","python","replaceUmlaute")

# Send text from chatbot to htmlfilter
marvin.addTextListener(htmlfilter)

# send htmlfilter results to speaker
htmlfilter.addTextListener(i01.mouth)

i01.mouth.speakBlocking("Hier spricht Marvin, noch etwas Geduld bitte")


def replaceUmlaute(data):
	data = data.replace(chr(228),"AE")
	data = data.replace(chr(246),"OE")
	data = data.replace(chr(252),"UE")
	print data
	marvin.getResponse(data)


