Runtime.createAndStart("chatBot", "ProgramAB")
sleep (1)
chatBot.startSession( "default", "wikiTest")
wdf = Runtime.createAndStart("wikiDataFetcher", "WikiDataFetcher")
wdf.setLanguage("en")

def talk(data):
	sweety.mouth.speak(data)
  	print "Saying :", data


def askWiki(start,query):
	answer = ( start + " " + query + " is " + wdf.getDescription(query))
	print " send aswer to the bot : " + answer
	chatBot.getResponse("say " + answer)

def getProperty(query, ID, what):
	answer = ( query +" " + what + " " + wdf.getProperty(query,ID))
	print " send aswer to the bot : " + answer
	chatBot.getResponse("say " + answer)

def getDate(query, ID):
	answer = ( wdf.getTime(query,ID,"day") +" " + wdf.getTime(query,ID,"month") + " " + wdf.getTime(query,ID,"year"))
	print " send to the bot : The " + answer
	chatBot.getResponse("say The " + answer)
