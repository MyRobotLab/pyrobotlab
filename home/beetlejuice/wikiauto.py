from time import sleep
import codecs
Runtime.createAndStart("chatBot", "ProgramAB") # On lance la gestion des chatBots
sleep (1)
chatBot.startSession( "default", "wikiAuto") # On demarre une session chatbot wikiAuto avec utilisateur par defaut
wdf = Runtime.createAndStart("wikiDataFetcher", "WikiDataFetcher") # WikiDataFetcher cherche des données sur les sites wiki
wdf.setLanguage("fr") # on cherche en français
wdf.setWebSite("frwiki") # On fait des recherches sur le site français de wikidata
Runtime.createAndStart("ear", "WebkitSpeechRecognition") # La reconnaissance vocale ( necessite le navigateur Chrome par default )
Runtime.createAndStart("webGui", "WebGui") # Webgui "installe" MRL dans une page Web
Runtime.createAndStart("mouth", "AcapelaSpeech") # AcapelaSpeech ce connecte net et rapatrie les texte converti en mp3
Runtime.createAndStart("htmlFilter", "HtmlFilter") # htmlFilter nettoye le texte AIML en retirant les balises avant de le lire

mouth.setLanguage("FR") # on parle francais !
mouth.setVoice("Antoine") # on choisis une voix ( voir la liste des voix sur http://www.acapela-group.com/?lang=fr


	
def talk(data):
	sweety.mouth.speak(data)
  	print "Saying :", data


def askWiki(query):
	query = unicode(query,'utf-8')
	print query
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
	wikiAnswer= wdf.getData(query,ID)
	answer = ( what +" de " + query + " est " + wikiAnswer)
	
	if wikiAnswer == "Not Found !":
		answer = "Je ne sais pas"
	chatBot.getResponse("say " + answer)
	print " send aswer to the bot : " + answer
	return answer

def getDate(query, ID):
	answer = ( wdf.getTime(query,ID,"day") +" " +wdf.getTime(query,ID,"month") + " " + wdf.getTime(query,ID,"year"))
	print " La date est : " + answer
	chatBot.getResponse("say Le " + answer)