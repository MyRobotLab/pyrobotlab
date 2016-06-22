# ##############################################################################
# 							*** SETUP ***
# ##############################################################################
# STABLE FILES : https://github.com/MyRobotLab/aiml/tree/master/bots/ [ RACHEL AIML + PYTHON ]
# UPDATED DEV FILES : https://github.com/MyRobotLab/pyrobotlab/tree/master/home/moz4r [ RACHEL AIML + PYTHON ]
# -----------------------------------
# Rachel bot Version 1.2 By Moz4r
# 
# Wikidatafetcher By Beetlejuice
#
# french AIML dictionay with the help of MAT
# -----------------------------------
# !!! INSTALL : !!!
# !!! PLEASE copy all aiml files to : develop\ProgramAB\bots\rachel\aiml !!!
# !!! AND https://github.com/MyRobotLab/aiml/tree/master/bots/BOTS-FRENCH/Rachel/TXT to the root of MRL
# !!! + https://github.com/MyRobotLab/aiml/tree/master/bots/BOTS-ENGLISH/Rachel/TXT
#
#Your language ( FR/EN )
lang="FR"
# To fetch weather etc [ adresse du serveur fetcher meteo etc ...]
BotURL="http://myai.cloud/bot1.php"
units="metric" # or : imperial
# ##
#
#IF YOU DIDNT HAVE MOTORS set inmoov=0 
IsInmoov=0
leftPort = "COM3"
rightPort = "COM4"

#Eyeleads / paupieres
IhaveEyelids=0
PaupiereServoPin = 27

#MRL mouthcontrol
jawMin = 55
jawMax = 60
# Ligh if you have
IhaveLights = 0

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


wdf=Runtime.createAndStart("wdf", "WikiDataFetcher")



i01 = Runtime.createAndStart("i01", "InMoov")
i01.startEar()
i01.startMouth()
mouth = i01.mouth
ear = i01.ear

webgui = Runtime.create("WebGui","WebGui")
webgui.autoStartBrowser(False)
webgui.startService()
# Then start the browsers and show the WebkitSpeechRecognition service named i01.ear
webgui.startBrowser("http://localhost:8888/#/service/i01.ear")


if IsInmoov==0:
	sleep(2)
else:
	
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
	#i01.startMouthControl(leftPort)
	i01.head.jaw.setMinMax(jawMin,jawMax)
	#i01.mouthControl.setmouth(jawMin,jawMax)
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

	right.pinMode(ROUGE, Arduino.OUTPUT)
	right.pinMode(VERT, Arduino.OUTPUT)
	right.pinMode(BLEU, Arduino.OUTPUT)
	

	right.digitalWrite(ROUGE,1)
	right.digitalWrite(VERT,0)
	right.digitalWrite(BLEU,1)	

if lang=="FR":
   voiceType="MargauxSad"
   WikiFile="prop.txt"
   ear.setLanguage("fr-FR")
   wdf.setLanguage("fr")
   wdf.setWebSite("frwiki")
else:
   voiceType="Ryan"
   WikiFile="propEN.txt"
   wdf.setLanguage("en")
   wdf.setWebSite("enwiki")

# on cherche en français
 # On fait des recherches sur le site français de wikidata
sleep(2)
mouth.setVoice(voiceType)
mouth.setLanguage(lang)





ear.startListening()

chatBot.startSession("ProgramAB", "default", "rachel")
ear.addTextListener(chatBot)
chatBot.addTextListener(htmlFilter)
htmlFilter.addListener("publishText", python.name, "talk") 


if IhaveEyelids==1:
	execfile('../RACHEL_INC_paupieres_eyeleads.py')
execfile('../RACHEL_INC_vie_aleatoire-standby_life.py')


#on bloque le micro quand le robot parle

def onEndSpeaking(text):
	ear.startListening()
	global TimeNoSpeak
	TimeNoSpeak=1
	VieAleatoire.startClock()
	sleep(1)
	ear.startListening()

def onStartSpeaking(text):
	ear.stopListening()
	TimeNoSpeak=1
	VieAleatoire.stopClock()
	
	
	
#on bloque le micro quand le robot parle
		
python.subscribe(mouth.getName(),"publishStartSpeaking")
python.subscribe(mouth.getName(),"publishEndSpeaking")

		
def talk(data):
	sleep(1)
	#VieAleatoire.stopClock()
	
	if data!="":
		mouth.speak(unicode(data,'utf-8'))


		
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
		answer=(question(query))
		sleep(1);
		chatBot.getResponse(answer)
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
		answer=(question(query+" "+what))
		sleep(1);
		chatBot.getResponse(answer)
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
	chatBot.getResponse("IDONTUNDERSTAND")
	if IsInmoov==1:
		i01.moveHead(80,50,90,78,40)
		sleep(0.5)
		i01.moveHead(83,120,90,78,40)
	sleep(0.5)
	Light(1,1,1)
	if IsInmoov==1:
		i01.moveHead(80,90,90,78,40)
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
	
def SaveMemory():
	chatBot.savePredicates()
	chatBot.writeAIMLIF()
	chatBot.getResponse("SAVEMEMORY")
		
def Meteo(data):
	a = Parse(BotURL+"&type=meteo&units="+units+"&city="+urllib2.quote(data).replace(" ", "%20"))
	print BotURL+"&type=meteo&units="+units+"&city="+urllib2.quote(data).replace(" ", "%20")
	mouth.speakBlocking(a)
	MoveHead()

def question(data):
	chatBot.getResponse("FINDTHEWEB")
	a = Parse(BotURL+"&type=question&question="+urllib2.quote(data).replace(" ", "%20"))
	print BotURL+"&type=question&question="+urllib2.quote(data).replace(" ", "%20")
	if a[0]=="0":
		return("IDONTUNDERSTAND")
	elif a[0:299]<>"":
		#return(a[0:299])
		return("IDONTUNDERSTAND")
	else:
		return("IDONTUNDERSTAND")
if IsInmoov==1:
	i01.detach()
Light(1,1,1)


def DisplayPic(pic):
	r=0
	try:
		r=image.displayFullScreen(pic,1)
	except: 
		chatBot.getResponse("PICTUREPROBLEM")
		pass
	time.sleep(0.1)
	try:
		r=image.displayFullScreen(pic,1)
	except:
		pass
	time.sleep(2)
	image.exitFS()
	image.closeAll()
chatBot.getResponse("ALEATOIRE")
