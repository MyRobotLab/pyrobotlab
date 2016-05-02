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
jawMax = 70
# ###
# ##############################################################################
#  						*** END SETUP ***
# ##############################################################################






import urllib2
from java.lang import String
import random
import threading
import itertools
import random
import time


BotURL=BotURL+"?lang="+lang+"&FixPhpCache="+str(time.time())


#voice emotions
laugh = [" #LAUGH01# ", " #LAUGH02# ", " #LAUGH03# ", " ", " "]
troat = [" #THROAT01# ", " #THROAT02# ", " #THROAT03# ", " : ", " : ", " : "]

Runtime.createAndStart("chatBot", "ProgramAB")
Runtime.createAndStart("ear", "WebkitSpeechRecognition") 
Runtime.createAndStart("webGui", "WebGui")
Runtime.createAndStart("htmlFilter", "HtmlFilter")
Runtime.createAndStart("Image", "ImageDisplay") 



if IsInmoov==0:
	Runtime.createAndStart("mouth", "AcapelaSpeech")
else:
	i01 = Runtime.createAndStart("i01", "InMoov")
	i01.startMouth()
	mouth = i01.mouth
	i01.startMouthControl(leftPort)
	i01.head.jaw.setMinMax(jawMin,jawMax)
	i01.mouthControl.setmouth(45,70)
	i01.head.jaw.setRest(50)
	i01.setHeadSpeed(0.5, 0.5)
	i01.moveHead(80,86,82,78,76)


if lang=="FR":
   voiceType="Margaux"
   ear.setLanguage("fr-FR")
else:
   voiceType="Ryan"


mouth.setVoice(voiceType)
mouth.setLanguage(lang)
ear.addTextListener(chatBot)
chatBot.startSession( "default", "rachel") 
chatBot.addTextListener(htmlFilter) 
htmlFilter.addListener("publishText", python.name, "talk") 

def talk(data):
	mouth.speak(data)
  	print "chatbot dit :", data
	
def FindImage(image):
	mouth.speak(image)
	#PLEASE USE REAL LANGUAGE PARAMETER :
	#lang=XX ( FR/EN/RU/IT etc...)
	#A FAKE LANGUAGE WORKS BUT DATABASE WILL BROKE
	a = String(urllib2.urlopen(BotURL+"&type=pic&pic="+image.replace(" ", "%20")).read())
	time.sleep(2)
	if IsInmoov==1:
		i01.moveHead(39,70)
	print(a)
	Image.displayFullScreen(a)
	time.sleep(5)
	Image.exitFS()
	if IsInmoov==1:
		i01.moveHead(80,86,82,78,76)
		
def Joke():
	if IsInmoov==1:
		i01.moveHead(80,70)
	a = urllib2.urlopen(BotURL+"&type=joke&genre="+JokeType).read().replace(" : ", random.choice(troat))
	time.sleep(1)
	try:
		a = a.decode( "utf8" )
	except: 
		pass
	mouth.speakBlocking(a+' '+random.choice(laugh))
	if IsInmoov==1:
		i01.moveHead(80,86,82,78,76)

def Meteo():
	if IsInmoov==1:
		i01.moveHead(80,70)
	a = urllib2.urlopen(BotURL+"&type=meteo&units="+units+"&city="+CITY.replace(" ", "%20")).read().replace(" : ", random.choice(troat))
	time.sleep(1)
	try:
		a = a.decode( "utf8" )
	except: 
		pass
	mouth.speakBlocking(a)
	print(a)
	if IsInmoov==1:
		i01.moveHead(80,86,82,78,76)
