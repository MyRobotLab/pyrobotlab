#LONK AT http://www.myai.cloud/
#FOR SERVER NAME AND BOT STATUS
#IT S A SMALL COMPUTER FOR NOW

# SETUP
# ##############################################################################
#Your language ( FR/IT/ES/RU etc .... )
#Jokes only works in FRENCH for now please send me CSV !
lang="FR"
BotURL="http://myai.cloud/bot1.php"
JokeType="CARAMBAR" # JokeType=BLONDES / CUL / CARAMBAR
#désolé c'est vraiment des blagues pouries niveau CM2... faites tourner en csv pour alimenter
#pas d'aprentissage pour le moment ca va venir . peut etre

# ##############################################################################

#dependencies
from java.lang import String
import random
import threading
import itertools
import random


BotURL=BotURL+"?lang="+lang


#french margaux voice laugh emotions
laugh = ["#LAUGH01#", "#LAUGH02#", "#LAUGH03#", ""]
troat = ["#THROAT01#", "#THROAT02#", "#THROAT03#", ""]

http = Runtime.createAndStart("http","HttpClient")
Runtime.createAndStart("chatBot", "ProgramAB")
Runtime.createAndStart("ear", "WebkitSpeechRecognition") 
Runtime.createAndStart("webGui", "WebGui")
Runtime.createAndStart("htmlFilter", "HtmlFilter")
Runtime.createAndStart("mouth", "AcapelaSpeech")  
Runtime.createAndStart("Image", "ImageDisplay") 

mouth.setVoice("Margaux")
mouth.setLanguage("FR")
ear.addTextListener(chatBot)
chatBot.startSession( "default", "rachel") 
chatBot.addTextListener(htmlFilter) 
htmlFilter.addListener("publishText", python.name, "talk") 

def talk(data):
	mouth.speak(data)
  	print "chatbot dit :", data
def FindImage(image):
	mouth.speak("JE te montre "+image)
	#PLEASE USE REAL LANGUAGE PARAMETER :
	#lang=XX ( FR/EN/RU/IT etc...)
	#A FAKE LANGUAGE WORKS BUT DATABASE WILL BROKE
	a = String(http.get(BotURL+"&type=pic&pic="+image.replace(" ", "%20")))
	Image.display(a)
	
def Joke():
	a = http.get(BotURL+"&type=joke").replace(" : ", random.choice(troat)).decode( "utf8" )
	mouth.speak(a+random.choice(laugh))
