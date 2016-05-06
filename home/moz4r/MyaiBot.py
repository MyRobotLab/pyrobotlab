# ##############################################################################
# 							*** SETUP ***
# ##############################################################################
# -----------------------------------
# MayAi bot Version 0.9 By Moz4r
# 
# Wikidatafetcher By Beetlejuice
# -----------------------------------
#Your language ( FR/EN )
lang="FR"
BotURL="http://myai.cloud/bot1.php"
#jokeBOT:
JokeType="RANDOM" # JokeType=RANDOM / BLONDES / CUL / CARAMBAR
#WeatherBOT -> Your city :
CITY="paris"
units="metric" # or : imperial
# ##
#LONK AT http://www.myai.cloud/
#FOR SERVER NAME AND BOT STATUS
#
#IF YOU WANT INMOOV MOUTH CONTROL ( inmoov ) set inmoov=1
#IF YOU DIDNT HAVE MOTORS set inmoov=0 
IsInmoov=1
leftPort = "COM3"
rightPort = "COM4"
jawMin = 45
jawMax = 60
# Ligh if you have
IhaveLights = 1
MASSE=27
ROUGE=29
VERT=28
BLEU=30
# ###
# 
# ##############################################################################
#  						*** END SETUP ***
# ##############################################################################




IdontWant=""

import urllib2
from java.lang import String
import random
import threading
import itertools
import random
import time
import textwrap
import codecs
import socket
import os



BotURL=BotURL+"?lang="+lang+"&FixPhpCache="+str(time.time())


#voice emotions
laugh = [" #LAUGH01# ", " #LAUGH02# ", " #LAUGH03# ", " ", " "]
troat = [" #THROAT01# ", " #THROAT02# ", " #THROAT03# ", " ", " ", " "]

Runtime.createAndStart("chatBot", "ProgramAB")
Runtime.createAndStart("ear", "WebkitSpeechRecognition") 
Runtime.createAndStart("webGui", "WebGui")
Runtime.createAndStart("htmlFilter", "HtmlFilter")
Runtime.createAndStart("Image", "ImageDisplay") 
wdf=Runtime.createAndStart("wdf", "WikiDataFetcher")
sleep(2)




if IsInmoov==0:
	Runtime.createAndStart("mouth", "AcapelaSpeech")
else:
	i01 = Runtime.createAndStart("i01", "InMoov")
	i01.startLeftHand(leftPort,"atmega2560")
	i01.startMouth()
	sleep(2)
	mouth = i01.mouth
	i01.startMouthControl(leftPort)
	i01.head.jaw.setMinMax(jawMin,jawMax)
	i01.mouthControl.setmouth(45,70)
	i01.head.jaw.setRest(40)
	i01.setHeadSpeed(0.5, 0.5)
	i01.moveHead(80,86,40,78,76)
	i01.head.jaw.rest()
	i01.head.eyeX.setMinMax(0,180)
	i01.head.eyeY.setMinMax(55,180)
	i01.head.eyeX.setRest(90)
	i01.head.eyeY.setRest(90)
	i01.head.eyeY.rest()
	i01.head.eyeX.rest()

if IhaveLights==1:
	i01.startLeftHand(rightPort,"atmega2560")
	right = Runtime.start("i01.right", "Arduino")
	right.setBoard("mega2560")
	right.connect(rightPort)
	sleep(2)
	right.pinMode(MASSE, Arduino.OUTPUT)
	right.pinMode(ROUGE, Arduino.OUTPUT)
	right.pinMode(VERT, Arduino.OUTPUT)
	right.pinMode(BLEU, Arduino.OUTPUT)
	
	right.publishState()
	right.digitalWrite(MASSE,1)
	right.digitalWrite(ROUGE,1)
	right.digitalWrite(VERT,0)
	right.digitalWrite(BLEU,1)	

if lang=="FR":
   NoNo="Je ne comprend pas"
   voiceType="Margaux"
   ear.setLanguage("fr-FR")
   wdf.setLanguage("fr")
   wdf.setWebSite("frwiki")
else:
   voiceType="Ryan"
   NoNo="I don't understand"
   wdf.setLanguage("en")
   wdf.setWebSite("enwiki")

# on cherche en français
 # On fait des recherches sur le site français de wikidata
sleep(2)
mouth.setVoice(voiceType)
mouth.setLanguage(lang)
ear.addTextListener(chatBot)
chatBot.startSession( "default", "rachel") 
chatBot.addTextListener(htmlFilter) 
htmlFilter.addListener("publishText", python.name, "talk") 

def Parse(utfdata):
	Light(1,1,0)
	utfdata = urllib2.urlopen(utfdata).read()
	utfdata = utfdata.replace("&#039;", "'").replace("http://fr.answers.yahoo.com/question/ind...", "")
	try:
		utfdata = utfdata.decode( "utf8" ).replace(" : ", random.choice(troat))
	except: 
		pass
	Light(1,1,1)
	return utfdata;

def MoveHead():
	if IsInmoov==1:
		i01.attach()
		i01.setHeadSpeed(0.5, 0.5)
		i01.moveHead(20,120,40,78,76)
		time.sleep(2)
		i01.moveHead(150,30,40,78,76)
		time.sleep(2)
		i01.moveHead(80,90,40,78,76)
		i01.detach()
		
def Light(ROUGE_V,VERT_V,BLEU_V):
	if IhaveLights==1:
		right.digitalWrite(ROUGE,ROUGE_V)
		right.digitalWrite(VERT,VERT_V)
		right.digitalWrite(BLEU,BLEU_V)

def talk(data):
	mouth.speak(data)
  	print "chatbot dit :", data
	
def askWiki(query): # retourne la description du sujet (query)
	Light(1,0,0)
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
	chatBot.getResponse("say " + answer)	
	Light(1,1,1)
	


def getProperty(query, what): # retourne la valeur contenue dans la propriété demandée (what)
	Light(1,0,0)
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
	# le fichier propriété.txt contient les conversions propriété -> ID . wikidata n'utilise pas des mots mais des codes (monnaie -> P38)	f = codecs.open(unicode('os.getcwd().replace("develop", "").replace("\", "/") + "/propriétés_ID.txt','r',"utf-8") #
	f = codecs.open(u'c:/mrl/proprietes_ID.txt','r','utf-8') #os.getcwd().replace("develop", "").replace("\\", "/") set you propertiesID.txt path
	
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
	Light(1,1,1)
	
def getDate(query, ID):# Cette fonction permet d'afficher une date personnalisée (mardi, le 10 juin, 1975, 12h38 .....)
	answer = ( wdf.getTime(query,ID,"day") +" " +wdf.getTime(query,ID,"month") + " " + wdf.getTime(query,ID,"year"))
	print " La date est : " + answer
	chatBot.getResponse("say Le " + answer)
	
def FindImage(image):
	try:
		image = image.decode( "utf8" )
	except: 
		pass
	mouth.speak(image)
	#PLEASE USE REAL LANGUAGE PARAMETER :
	#lang=XX ( FR/EN/RU/IT etc...)
	#A FAKE LANGUAGE WORKS BUT DATABASE WILL BROKE
	a = Parse(BotURL+"&type=pic&pic="+urllib2.quote(image).replace(" ", "%20"))
	Light(1,1,0)
	MoveHead()
	Image.displayFullScreen(a,1)
	Light(1,1,1)
	time.sleep(5)
	Image.exitFS()
		
def Joke():
	MoveHead()
	a = Parse(BotURL+"&type=joke&genre="+JokeType).replace(" : ", random.choice(troat))
	mouth.speakBlocking(a+' '+random.choice(laugh))
	
def No(data):
	if data=="#NO#":
		data=NoNo
	if IsInmoov==1:
		i01.attach()
		i01.setHeadSpeed(1, 1)
		i01.moveHead(80,90,0,80,40)
		sleep(2)
		i01.moveHead(80,90,180,80,40)
		sleep(1)
		i01.moveHead(80,90,90,80,40)
		sleep(0.5)
	Light(0,1,1)
	if IsInmoov==1:
		i01.moveHead(81,50,90,78,40)
		sleep(0.5)
		i01.moveHead(79,120,90,78,40)
	mouth.speakBlocking(data.decode( "utf8" ))
	if IsInmoov==1:
		i01.moveHead(80,50,90,78,40)
		sleep(0.5)
		i01.moveHead(83,120,90,78,40)
	sleep(0.5)
	Light(1,1,1)
	if IsInmoov==1:
		i01.moveHead(80,90,90,78,40)
	mouth.speakBlocking(random.choice(troat))
	if IsInmoov==1:
		i01.head.jaw.rest()
		i01.detach()
	
def Yes(data):
	i01.attach()
	i01.moveHead(80,90,90,180,40)
	sleep(1)
	Light(1,0,1)
	i01.setHeadSpeed(1, 1)
	i01.moveHead(120,88,90,78,40)
	sleep(0.4)
	i01.moveHead(40,92,90,78,40)
	sleep(0.4)
	mouth.speakBlocking(data.decode( "utf8" ))
	sleep(0.4)
	i01.moveHead(120,87,90,78,40)
	sleep(0.4)
	i01.moveHead(40,91,90,78,40)
	sleep(0.4)
	i01.moveHead(120,87,90,78,40)
	sleep(0.3)
	Light(1,1,1)
	i01.moveHead(80,90,90,78,40)
	mouth.speakBlocking(random.choice(troat))
	i01.head.jaw.rest()
	i01.detach()
	
def Meteo():
	a = Parse(BotURL+"&type=meteo&units="+units+"&city="+CITY.replace(" ", "%20"))
	mouth.speakBlocking(a)
	MoveHead()

def question(data):
	a = Parse(BotURL+"&type=question&question="+urllib2.quote(data).replace(" ", "%20"))
	if a[0:299]<>"":
		mouth.speakBlocking(a[0:299])
		mouth.speakBlocking(a[300:599])
	MoveHead()
i01.detach()
Light(1,1,1)
