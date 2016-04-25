#LONK AT http://www.myai.cloud/
#FOR SERVER NAME AND BOT STATUS
#IT S A SMALL COMPUTER FOR NOW

# SETUP
# ##############################################################################
#Your language ( FR/IT/ES/RU etc .... )
#Jokes only works in FRENCH for now please send me CSV !
lang="FR"
BotURL="http://myai.cloud/bot1.php"
JokeType="RANDOM" # JokeType=RANDOM / BLONDES / CUL / CARAMBAR
#RAMDOM=Tout sauf cul, ca vole pas bien haut mais il peut y avoir des enfants...
#désolé c'est vraiment des blagues tres pouries niveau CM2... j ai trouvé que ça
#si vous en avez peu importe le format, n hesitez pas !
#pas d'aprentissage blagues pour le moment ca va venir . peut etre

# ##############################################################################

#dependencies
from java.lang import String
import random
import threading
import itertools
import random


BotURL=BotURL+"?lang="+lang+"?FixPhpCache="+str(random.randint(0,99999999))


#french margaux voice laugh emotions
laugh = [" #LAUGH01# ", " #LAUGH02# ", " #LAUGH03# ", " ", " "]
troat = [" #THROAT01# ", " #THROAT02# ", " #THROAT03# ", " : ", " : ", " : "]

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
	a = http.get(BotURL+"&type=joke&genre="+JokeType).replace(":", random.choice(troat)).decode( "utf8" )
	mouth.speak(a+' '+random.choice(laugh))
