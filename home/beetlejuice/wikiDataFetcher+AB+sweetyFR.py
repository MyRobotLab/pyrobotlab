Runtime.createAndStart("sweety", "Sweety")

sweety.chatBot.startSession("default", "wikiTestFR")
sweety.chatBot.setPredicate("default","name","unknow")
wdf = Runtime.createAndStart("wikiDataFetcher", "WikiDataFetcher")
wdf.setLanguage("fr")
wdf.setWebSite("frwiki")


# Add route from webKitSpeechRecognition to Program AB
sweety.ear.addTextListener(sweety.chatBot)
# Add route from Program AB to html filter
sweety.chatBot.addTextListener(sweety.htmlFilter)
# Add route from html filter to mouth
sweety.htmlFilter.addListener("publishText", python.name, "talk");
sweety.mouth.setLanguage("FR");
sweety.mouth.setVoice("Antoine");

print cutStart("Le chat")

def talk(data):
	sweety.mouth.speak(data)
  	print "Saying :", data



def askWiki(start,query):
	query = unicode(query,'utf-8')
	answer = ( start + " " + query + " est " + wdf.getDescription(query))
	print " send aswer to the bot : " + answer
	sweety.chatBot.getResponse("say " + answer)

def getProperty(query, ID, what):
	query = unicode(query,'utf-8')
	what = unicode(what,'utf-8')
	print " query : " + query
	answer = ( query +" " + what + " " + wdf.getSnak(query,ID))
	print " send aswer to the bot : " + answer
	sweety.chatBot.getResponse("say " + answer)