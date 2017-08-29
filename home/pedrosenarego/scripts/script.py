 
Runtime.createAndStart("chatBot", "ProgramAB") 
sleep (1)
chatBot.startSession( "default", "wikidataFR") 
Runtime.createAndStart("ear", "WebkitSpeechRecognition") 
mouth=Runtime.createAndStart("mouth", "AcapelaSpeech")
htmlFilter=Runtime.createAndStart("htmlFilter", "HtmlFilter")

sleep(1)
ear.addListener("publishText", python.name, "talk") 
# Add route from Program AB to html filter
chatBot.addTextListener(htmlFilter)
# Add route from html filter to mouth
htmlFilter.addListener("publishText", python.name, "say");
mouth.setLanguage("FR");
mouth.setVoice("Antoine");
ear.setLanguage("fr-FR")
Runtime.createAndStart("webGui", "WebGui") 

def say(data):
	mouth.speakBlocking(data)
	print "chatbot :", data
	
def talk(data):
	if data!="":
		data = data.replace("\'", " ") # Replace quote by a blank space
		chatBot.getResponse(data) # Ask the chatBot 
  		print "chatbot :", data