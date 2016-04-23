# Ce programme introduit les bases d'utilisation du service wikidatafetcher

import random
import codecs
import socket
from java.lang import String

chatBot=Runtime.createAndStart("chatBot", "ProgramAB")
ear=Runtime.createAndStart("ear", "WebkitSpeechRecognition")
mouth=Runtime.createAndStart("mouth", "AcapelaSpeech")
htmlFilter=Runtime.createAndStart("htmlFilter", "HtmlFilter")
webgui=Runtime.createAndStart("webgui", "WebGui")

chatBot.startSession("ProgramAB", "sweety", "sweety")
wdf=Runtime.createAndStart("wdf", "WikiDataFetcher") # WikiDataFetcher cherche des données sur les sites wiki
wdf.setLanguage("fr") # on cherche en français
wdf.setWebSite("frwiki") # On fait des recherches sur le site français de wikidata
sleep(2)
mouth.setLanguage("FR") # on parle francais !
mouth.setVoice("Antoine") # on choisis une voix ( voir la liste des voix sur http://www.acapela-group.com/?lang=fr
ear.addTextListener(chatBot) # On creer une liaison de webKitSpeechRecognition vers Program AB
ear.setLanguage("fr-FR")
chatBot.addTextListener(htmlFilter) # On creer une liaison de Program AB vers html filter
htmlFilter.addListener("publishText", python.name, "talk") # On creer une liaison de htmlfilter vers mouth



def talk(data): # cette fonction "dit" vocalement le texte qu'elle reçoit (data)
	if data!="":
		mouth.speak(data)
  		print "chatbot :", data
  		
def askWiki(query): # retourne la description du sujet (query)
	query = unicode(query,'utf-8')# on force le format de police UTF-8 pour prendre en charge les accents
	if query[1]== "\'" : # Si le sujet contient un apostrophe , on efface tout ce qui est avant ! ( "l'été" -> "été")
		query2 = query[2:len(query)]
		query = query2
	print query # petit affichage de contrôle dans la console python ..
	word = wdf.cutStart(query) # on enlève le derminant ("le chat" -> "chat")
	start = wdf.grabStart(query) # on garde que le déterminant ( je ne sais plus pourquoi j'ai eu besoin de ça, mais la fonction existe ...)
	wikiAnswer = wdf.getDescription(word) # récupère la description su wikidata
	answer = ( query + " est " + wikiAnswer)
	if wikiAnswer == "Not Found !": # Si le document n'ai pas trouvé , on réponds "je ne sais pas"
		answer = "Je ne sais pas"
	chatBot.getResponse("say " + answer) #on demande a programAB de faire le perroquet !

def getProperty(query, what): # retourne la valeur contenue dans la propriété demandée (what)
	query = unicode(query,'utf-8')
	what = unicode(what,'utf-8')
	if query[1]== "\'" :
		query2 = query[2:len(query)]
		query = query2
	if what[1]== "\'" :
		what2 = what[2:len(what)]
		what = what2
		print "what = " + what + " - what2 = " + what2
	ID = "error"
	# le fichier propriété.txt contient les conversions propriété -> ID . wikidata n'utilise pas des mots mais des codes (monnaie -> P38)
	f = codecs.open(u"C:/Users/papa/git/pyrobotlab/home/beetlejuice/propriétés_ID.txt",'r',"utf-8") # set you propertiesID.txt path
	
	for line in f:
    		line_textes=line.split(":")
    		if line_textes[0]== what:
	    		ID= line_textes[1]
	f.close()
	print "query = " + query + " - what = " + what + " - ID = " + ID
	wikiAnswer= wdf.getData(query,ID) # récupère la valeur de la propriété si elle existe dans le document
	answer = ( what +" de " + query + " est " + wikiAnswer)
	
	if wikiAnswer == "Not Found !":
		answer = "Je ne sais pas"
	chatBot.getResponse("say " + answer)
	return answer

def getDate(query, ID):# Cette fonction permet d'afficher une date personnalisée (mardi, le 10 juin, 1975, 12h38 .....)
	answer = ( wdf.getTime(query,ID,"day") +" " +wdf.getTime(query,ID,"month") + " " + wdf.getTime(query,ID,"year"))
	print " La date est : " + answer
	chatBot.getResponse("say Le " + answer)
def getIp(): # cette fonction annonce l'adresse IP locale, elle n'ai pas dans le fichier aiml wikidata, a vous de l'ajouter ;) 
	ip = str(socket.gethostbyname(socket.gethostname()))
	ip = ip.replace('.',' point ')
	chatBot.getResponse("say Mon adresse IP est  " + ip)
	