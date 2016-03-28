from time import sleep
Runtime.createAndStart("chatBot", "ProgramAB")
sleep (1)
chatBot.startSession( "default", "wikiAuto")
wdf = Runtime.createAndStart("wikiDataFetcher", "WikiDataFetcher")
wdf.setLanguage("fr")
wdf.setWebSite("frwiki")


def talk(data):
	sweety.mouth.speak(data)
  	print "Saying :", data


def askWiki(query):
	query = unicode(query,'utf-8')
	word = wdf.cutStart(query)
	start = wdf.grabStart(query)
	answer = ( query + " est " + wdf.getDescription(word))
	print " send aswer to the bot : " + answer
	chatBot.getResponse("say " + answer)

def getProperty(query, ID, what):
	query = unicode(query,'utf-8')
	what = unicode(what,'utf-8')
	print "query : "+ query
	print "ID : "+ ID
	wikiAnswer= wdf.getData(query,ID)
	answer = ( query +" " + what + " " + wikiAnswer)
	print " send aswer to the bot : " + answer
	chatBot.getResponse("say " + answer)

def getDate(query, ID):
	answer = ( wdf.getTime(query,ID,"day") +" " +wdf.getTime(query,ID,"month") + " " + wdf.getTime(query,ID,"year"))
	print " La date est : " + answer
	chatBot.getResponse("say Le " + answer)