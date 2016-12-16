from java.lang import String
import random
import codecs
import socket
Runtime.createAndStart("chatBot", "ProgramAB") # ProgramAB qui lit et interprete les fichiers AIML
Runtime.createAndStart("ear", "WebkitSpeechRecognition") # La reconnaissance vocale ( necessite le navigateur Chrome par default )
#Runtime.createAndStart("webGui", "WebGui") # Webgui "installe" MRL dans une page Web
Runtime.createAndStart("mouth", "AcapelaSpeech") # AcapelaSpeech ce connecte net et rapatrie les texte converti en mp3
Runtime.createAndStart("htmlFilter", "HtmlFilter") # htmlFilter nettoye le texte AIML en retirant les balises avant de le lire

#mouth.setLanguage("FR") # on parle francais !
mouth.setVoice("Antonio") # on choisis une voix ( voir la liste des voix sur http://www.acapela-group.com/?lang=fr
#chatBot.startSession("fede","max") # on demarre la session qui est dans le dossier sweety
chatBot.startSession("ProgramAB","fede", "max")
ear.addTextListener(chatBot) # On creer une liaison de webKitSpeechRecognition vers Program AB
ear.setLanguage("es-AR")
chatBot.addTextListener(htmlFilter) # On creer une liaison de Program AB vers html filter
htmlFilter.addListener("publishText", python.name, "talk") # On creer une liaison de htmlfilter vers mouth

#chatBot.setPredicate("default","prenom","unknow") # Ca c est pour moi, j efface le nom de l interlocuteur en debut de session

def talk(data):
	mouth.speak(data)
  	print "chatbot dice :", data