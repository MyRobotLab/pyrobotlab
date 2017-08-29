Runtime.createAndStart("sweety", "Sweety")

sweety.chatBot.startSession("default", "wikiTest")
sweety.chatBot.setPredicate("default","name","unknow")
wdf = Runtime.createAndStart("wikiDataFetcher", "WikiDataFetcher")


# Add route from webKitSpeechRecognition to Program AB
sweety.ear.addTextListener(sweety.chatBot)
# Add route from Program AB to html filter
sweety.chatBot.addTextListener(sweety.htmlFilter)
# Add route from html filter to mouth
sweety.htmlFilter.addListener("publishText", python.name, "talk");
sweety.mouth.setLanguage("EN");
sweety.mouth.setVoice("Laura");

def talk(data):
	sweety.mouth.speakBlocking(data)
  	print "Saying :", data


def askWiki(start,query):
	data = wdf.getDescription(query)
	answer = ( start + " " + query + " is " + data )
	print " send aswer to the bot : " + answer
	if data == "Not found" :
		sweety.chatBot.getResponse("I don't know")
	else :
		sweety.chatBot.getResponse("say " + answer)

def getProperty(query, ID, what):
	data = wdf.getData(query,ID)
	answer = ( query +" " + what + " " + data)
	print " send aswer to the bot : " + answer
	if data == "Not found" :
		sweety.chatBot.getResponse("I don't know")
	else :
		sweety.chatBot.getResponse("say " + answer)