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
IsInmoov=0
leftPort = "COM3"
rightPort = "COM4"
jawMin = 55
jawMax = 60
# Ligh if you have
IhaveLights = 0
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
image=Runtime.createAndStart("ImageDisplay", "ImageDisplay")
sleep(1)
Runtime.createAndStart("chatBot", "ProgramAB")
Runtime.createAndStart("ear", "WebkitSpeechRecognition") 
Runtime.createAndStart("webGui", "WebGui")

wdf=Runtime.createAndStart("wdf", "WikiDataFetcher")





if IsInmoov==0:
	Runtime.createAndStart("mouth", "AcapelaSpeech")
	sleep(2)
else:
	i01 = Runtime.createAndStart("i01", "InMoov")
	right = Runtime.start("i01.right", "Arduino")
	right.setBoard("mega2560")
	right.publishState()
	right.connect(rightPort)
	left = Runtime.start("i01.left", "Arduino")
	left.setBoard("mega2560")
	left.publishState()
	left.connect(leftPort)
	sleep(1)
	i01.startRightHand(rightPort,"atmega2560")
	i01.startHead(leftPort,"atmega2560")
	i01.startMouth()
	mouth = i01.mouth
	i01.startMouthControl(leftPort)
	i01.head.jaw.setMinMax(jawMin,jawMax)
	i01.mouthControl.setmouth(jawMin,jawMax)
	i01.head.jaw.setRest(jawMin)
	i01.setHeadSpeed(0.5, 0.5)
	i01.moveHead(80,86,40,78,76)
	i01.head.jaw.rest()
	i01.head.eyeX.setMinMax(0,180)
	i01.head.eyeY.setMinMax(55,180)
	i01.head.eyeX.setRest(90)
	i01.head.eyeY.setRest(90)
	i01.head.eyeY.rest()
	i01.head.eyeX.rest()
	
Runtime.createAndStart("htmlFilter", "HtmlFilter")

if IhaveLights==1:
	right.pinMode(MASSE, Arduino.OUTPUT)
	right.pinMode(ROUGE, Arduino.OUTPUT)
	right.pinMode(VERT, Arduino.OUTPUT)
	right.pinMode(BLEU, Arduino.OUTPUT)
	
	right.digitalWrite(MASSE,1)
	right.digitalWrite(ROUGE,1)
	right.digitalWrite(VERT,0)
	right.digitalWrite(BLEU,1)	

if lang=="FR":
   NoNo="Je ne comprend pas"
   LANGfind="Je vais faire une recherche sur internet"
   LANGimage="Désolé, Je rencontre un problème pour te montrer cette image"
   voiceType="MargauxSad"
   WikiFile="prop.txt"
   ear.setLanguage("fr-FR")
   wdf.setLanguage("fr")
   wdf.setWebSite("frwiki")
else:
   voiceType="Ryan"
   LANGfind="I do a search on internet"
   LANGimage="There is a problem to show the picture I am so sorry"
   NoNo="I don't understand"
   WikiFile="propEN.txt"
   wdf.setLanguage("en")
   wdf.setWebSite("enwiki")

# on cherche en français
 # On fait des recherches sur le site français de wikidata
sleep(2)
mouth.setVoice(voiceType)
mouth.setLanguage(lang)

chatBot.startSession("default", "rachel")
ear.addTextListener(chatBot)
chatBot.addTextListener(htmlFilter)
htmlFilter.addListener("publishText", python.name, "talk") 

def talk(data):
	if IsInmoov==0:
		mouth.speak(unicode(data,'utf-8'))
	else:
		mouth.speakBlocking(unicode(data,'utf-8'))
  	print "chatbot dit :", data

def Parse(utfdata):
	Light(1,1,0)
	utfdata = urllib2.urlopen(utfdata).read()
	utfdata = utfdata.replace("&#039;", "'").replace("http://fr.answers.yahoo.com/question/ind...", "")
	try:
		utfdata = utfdata.decode( "utf8" ).replace(" : ", random.choice(troat))
	except: 
		pass
	print utfdata
	Light(1,1,1)
	return utfdata;

def MoveHead():
	if IsInmoov==1:
		#i01.attach()
		i01.setHeadSpeed(0.5, 0.5)
		i01.moveHead(20,120,40,78,76)
		time.sleep(2)
		i01.moveHead(150,30,40,78,76)
		time.sleep(2)
		i01.moveHead(80,90,40,78,76)
		#i01.detach()
		
def Light(ROUGE_V,VERT_V,BLEU_V):
	if IhaveLights==1:
		right.digitalWrite(ROUGE,ROUGE_V)
		right.digitalWrite(VERT,VERT_V)
		right.digitalWrite(BLEU,BLEU_V)


	
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
	if (wikiAnswer == "Not Found !") or (unicode(wikiAnswer[-9:],'utf-8') == u"Wikimédia") : # Si le document n'ai pas trouvé , on réponds "je ne sais pas"
		answer = LANGfind
		talk(LANGfind)	
		sleep(1);
		answer=(question(query))
		sleep(1);
		talk(answer)
	else:
		talk(answer)
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
	f = codecs.open(os.getcwd().replace("develop", "").replace("\\", "/")+WikiFile,'r','utf-8') #os.getcwd().replace("develop", "").replace("\\", "/") set you propertiesID.txt path
	
	for line in f:
    		line_textes=line.split(":")
    		if line_textes[0]== what:
	    		ID= line_textes[1]
	f.close()
	#print "query = " + query + " - what = " + what + " - ID = " + ID
	wikiAnswer= wdf.getData(query,ID) # récupère la valeur de la propriété si elle existe dans le document
	answer = ( what +" de " + query + " est " + wikiAnswer)
	
	if wikiAnswer == "Not Found !":
		answer = LANGfind
		talk(LANGfind)	
		sleep(1);
		answer=(question(query+" "+what))
		sleep(1);
		talk(answer)
	else:
		talk(answer)
	Light(1,1,1)
	return answer
	
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
	DisplayPic(a)
	print BotURL+"&type=pic&pic="+urllib2.quote(image).replace(" ", "%20")
	Light(1,1,1)
			
def Joke():
	MoveHead()
	a = Parse(BotURL+"&type=joke&genre="+JokeType).replace(" : ", random.choice(troat))
	mouth.speakBlocking(a+' '+random.choice(laugh))
	
def No(data):
	if data=="#NO#":
		data=NoNo
	if IsInmoov==999:
		#i01.attach()
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
	mouth.speakBlocking(random.choice(troat).decode( "utf8" ))
	if IsInmoov==1:
		i01.head.jaw.rest()
		#i01.detach()
	
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
	print BotURL+"&type=question&question="+urllib2.quote(data).replace(" ", "%20")
	if a[0]=="0":
		return(NoNo)
	elif a[0:299]<>"":
		return(a[0:299])
	else:
		return(NoNo)
if IsInmoov==1:
	i01.detach()
Light(1,1,1)


def DisplayPic(pic):
	r=0
	try:
		r=image.displayFullScreen(pic,1)
	except: 
		talk(LANGimage)
		pass
	time.sleep(0.1)
	try:
		r=image.displayFullScreen(pic,1)
	except:
		pass
	time.sleep(2)
	image.exitFS()
	image.closeAll()
