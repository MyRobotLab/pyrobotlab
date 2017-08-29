from java.lang import String
import random
import codecs
import socket
Runtime.createAndStart("chatBot", "ProgramAB") #  Crea servicio de bot de charla
Runtime.createAndStart("ear", "WebkitSpeechRecognition") # servicio de google de reconoocimiento de habla ( necesita navegados Chrome por defecto )
#Runtime.createAndStart("webGui", "WebGui") # "instala" MRL en una pagina web
Runtime.createAndStart("mouth", "NaturalReaderSpeech") # AcapelaSpeech ce connecte net et rapatrie les texte converti en mp3
Runtime.createAndStart("htmlFilter", "HtmlFilter") # htmlFilter nettoye le texte AIML en retirant les balises avant de le lire


mouth.setVoice("Alberto") # Selecciona voz de alberto( ver posibles voces https://www.naturalreaders.com/)

chatBot.startSession("ProgramAB","fede", "max") #inicia bot de charla. nombre usuario fede, y nombre de bot max
ear.addTextListener(chatBot) # enlaza el reconocimiento de vozde google con el bot de charla 
ear.setLanguage("es-AR") # le dice que la voz a reconocer es argentina
chatBot.addTextListener(htmlFilter) # enlaza Program AB con el filtro html 
htmlFilter.addListener("publishText", python.name, "talk") # enlaza filtro html con la funcion python llamada "talk"



def talk(data):
	mouth.speak(data)
  	print "chatbot dice :", data
