# cycle through NaturalReaderSpeech voices
# with i2c connected jaw servo
# Author: Acapulco Rolf
# Date: December 4th 2017
# Build: myrobotlab development build version 2645

from time import sleep 
from org.myrobotlab.service import Speech
lang="EN" #for NaturalReaderSpeech
Voice="Ryan" 
voiceType = Voice
speech = Runtime.createAndStart("Speech", "NaturalReaderSpeech")
speech.setVoice(voiceType)
speech.setLanguage(lang)

#open and close mouth in sync with speech
openclosemoouth = False


if openclosemoouth:
	#set up Jaw with Raspberry Pi with Adafruit16C servo service
	# 50 Hz servo frequency
	frequency	=  50 

	adaFruit16c1 = Runtime.createAndStart("AdaFruit16C1","Adafruit16CServoDriver")
	raspi = Runtime.createAndStart("RasPi","RasPi")
	adaFruit16c1.setController("RasPi","1","0x40")
	adaFruit16c1.setPWMFreq(0,frequency)  

	jawPin = 8
	jawServo = Runtime.createAndStart("jaw","Servo")
	mouth = Runtime.createAndStart("Mouth","MouthControl")
	sleep(20) # fix for servo attach timing issue as at myrobotlab 236x development builds

	jawServo.attach(adaFruit16c1,jawPin,150,-1)
	jaw = mouth.getJaw()
	sleep(1)
	jaw.attach(adaFruit16c1,jawPin)

	jawServo.setMinMax(140,180) # set min and max jaw position accordingly for your own use-case
				    # these min/max settings work for me for this particular jaw: https://www.thingiverse.com/thing:992918
				    # @Mats, thanks :) 				
	jawServo.setRest(175)
	jawServo.moveTo(100)
	jawServo.rest()
	mouth.setmouth(140,175)
	mouth.autoAttach = False
	mouth.setMouth(speech)


def onEndSpeaking(text):
	sleep(.5)	
	#Start of main script
	sleep(1)
	speech.speakBlocking(text)	
	#mouth.jaw.moveTo(175)
	

def saystuff():
	#myvoices = ['Ryan','Rich','Mike','Graham','Laura','Charles','Crystal','Heather','Ella','Rod','Peter','Audrey','Lucy','Rachel','Rosy','Ryan']
	myvoices = ["Sharon", "Amanda","Tracy","Ryan","Tim","Suzan", "Mike","Rod","Rachel","Peter","Graham","Selene","Darren","Charles","Audrey","Rosa","Alberto","Diego", "Camila","Paula","Joaquim","Alain","Juliette","Emmanuel", "Marie","Bruno","Alice","Louice","Reiner", "Klara","Klaus","Sarah","Bertha","Jacob","Vittorio","Chiara","Mario","Valentina","Celia","Renata","Andrea","Julieta","Emma","Erik","Gus","Maja","Anika", "Markus"]

	myvoicescount = len(myvoices)
	for i in range(0,myvoicescount):
		speech.setVoice(myvoices[i])
		print("I am speaking with "+(myvoices[i])+"'s voice")
		onEndSpeaking ("I'm completely operational, and all my circuits are functioning perfectly.")
		

saystuff()
