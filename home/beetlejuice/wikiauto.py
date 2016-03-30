from time import sleep
import codecs
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

def getProperty(query, what):
	query = unicode(query,'utf-8')
	what = unicode(what,'utf-8')
	
	ID = "error"
	f = codecs.open(u"C:/Users/papa/git/pyrobotlab/home/beetlejuice/propriétés_ID.txt",'r',"utf-8") # set you propertiesID.txt path
	
	for line in f:
    		line_textes=line.split(":")
    		if line_textes[0]== what:
	    		ID= line_textes[1]
	f.close()
	print "query : "+ query
	print "property : " + what
	print "ID : "+ ID
	wikiAnswer= wdf.getData(query,ID)
	answer = ( query +" " + what + " " + wikiAnswer)
	print " send aswer to the bot : " + answer
	chatBot.getResponse("say " + answer)

def getDate(query, ID):
	answer = ( wdf.getTime(query,ID,"day") +" " +wdf.getTime(query,ID,"month") + " " + wdf.getTime(query,ID,"year"))
	print " La date est : " + answer
	chatBot.getResponse("say Le " + answer)