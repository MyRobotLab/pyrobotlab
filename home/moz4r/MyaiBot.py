# ##############################################################################
# 							*** SETUP ***
# ##############################################################################
#Your language ( FR/EN )
lang="EN"
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
jawMin = 45
jawMax = 60
# Ligh if you have
IhaveLights = 0
MASSE=27
ROUGE=29
VERT=28
BLEU=30
# ###
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


BotURL=BotURL+"?lang="+lang+"&FixPhpCache="+str(time.time())


#voice emotions
laugh = [" #LAUGH01# ", " #LAUGH02# ", " #LAUGH03# ", " ", " "]
troat = [" #THROAT01# ", " #THROAT02# ", " #THROAT03# ", " ", " ", " "]

Runtime.createAndStart("chatBot", "ProgramAB")
Runtime.createAndStart("ear", "WebkitSpeechRecognition") 
Runtime.createAndStart("webGui", "WebGui")
Runtime.createAndStart("htmlFilter", "HtmlFilter")
Runtime.createAndStart("Image", "ImageDisplay") 


if IhaveLights==1:
	right = Runtime.start("i01.right", "Arduino")
	right.setBoard("mega2560")
	right.connect(rightPort)
	right.pinMode(MASSE, Arduino.OUTPUT)
	right.pinMode(ROUGE, Arduino.OUTPUT)
	right.pinMode(VERT, Arduino.OUTPUT)
	right.pinMode(BLEU, Arduino.OUTPUT)
	right.digitalWrite(MASSE,1)
	right.digitalWrite(ROUGE,1)
	right.digitalWrite(VERT,1)
	right.digitalWrite(BLEU,1)


if IsInmoov==0:
	Runtime.createAndStart("mouth", "AcapelaSpeech")
else:
	i01 = Runtime.createAndStart("i01", "InMoov")
	i01.startMouth()
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

if lang=="FR":
   NoNo="Je ne comprend pas"
   voiceType="Margaux"
   ear.setLanguage("fr-FR")
else:
   voiceType="Ryan"
   NoNo="I don't understand"


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
	mouth.speakBlocking(a[0:299])
	mouth.speakBlocking(a[300:599])
	MoveHead()
i01.detach()
