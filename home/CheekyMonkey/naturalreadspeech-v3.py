# cycle through NaturalReaderSpeech voices
# with i2c connected jaw servo
# Author: Acapulco Rolf
# Date: December 16th 2017
# Build: myrobotlab development build version 2673

# commentary
# https://github.com/MyRobotLab/myrobotlab/commit/d7ae81c867c14465752cd36b0d856d365e91dcad

from time import sleep 
from org.myrobotlab.service import Speech
lang="EN" #for NaturalReaderSpeech
Voice="British-English_John" 
voiceType = Voice
speech = Runtime.createAndStart("Speech", "NaturalReaderSpeech")
speech.setVoice(voiceType)
speech.setLanguage(lang)

#open and close mouth in sync with speech
openclosemouth = False


if openclosemouth:
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
		# myvoices = ['Ryan','Rich','Mike','Graham','Laura','Charles','Crystal','Heather','Ella','Rod','Peter','Audrey','Lucy','Rachel','Rosy','Ryan']
		# myvoices = ["Sharon", "Amanda","Tracy","Ryan","Tim","Suzan", "Mike","Rod","Rachel","Peter","Graham","Selene","Darren","Charles","Audrey","Rosa","Alberto","Diego", "Camila","Paula","Joaquim","Alain","Juliette","Emmanuel", "Marie","Bruno","Alice","Louice","Reiner", "Klara","Klaus","Sarah","Bertha","Jacob","Vittorio","Chiara","Mario","Valentina","Celia","Renata","Andrea","Julieta","Emma","Erik","Gus","Maja","Anika", "Markus"]
		myvoices = ["Australian-English_Noah","Australian-English_Olivia","Brazilian-Portuguese_Manuela","Brazilian-Portuguese_Miguel","British-English_Charlotte","British-English_Emily","British-English_John","Castilian-Spanish_Alejandro","Castilian-Spanish_Lucia","Danish_Line","Danish_Mikkel","Dutch_Birgit","Dutch_Daan","Dutch_Dieter","Dutch_Roos","French_Gabriel","French_Renee","GB-English_Carrie","German_Ida","German_Johann","German_Vicki","Icelandic_Gunnar","Icelandic_Helga","Indian-English_Aditi","Indian-English_Padma","Italian_Francesca","Italian_Francesco","Italian_Giulia","Japanese_Hana","Japanese_Midori","Japanese_Takumi","Korean_Seoyeon","Norwegian_Ingrid","Polish_Jakub","Polish_Kacper","Polish_Lena","Polish_Zofia","Portuguese_BR-Isabela","Portuguese_Joao","Portuguese_Mariana","Romanian_Elena","Russian_Olga","Russian_Sergei","Spanish_Enrique","Spanish_Laura","Spanish_Sofia","Swedish_Elsa","Turkish_Esma","US-English_Amber","US-English_David","US-English_James","US-English_Jennifer","US-English_Kathy","US-English_Leslie","US-English_Linda","US-English_Mary","US-English_Matthew","US-English_Polly","US-English_Ronald","US-English_Sofia","US-Spanish_Isabella","Welsh_Seren","Welsh-English_Gareth"]
		
		#"Italian_Giulia","Japanese_Hana","Japanese_Midori","Japanese_Takumi","Korean_Seoyeon","Norwegian_Ingrid","Polish_Jakub","Polish_Kacper","Polish_Lena","Polish_Zofia","Portuguese_BR-Isabela","Portuguese_Joao","Portuguese_Mariana","Romanian_Elena","Russian_Olga","Russian_Sergei","Spanish_Enrique","Spanish_Laura","Spanish_Sofia","Swedish_Elsa","Turkish_Esma","US-English_Amber","US-English_David","US-English_James","US-English_Jennifer","US-English_Kathy","US-English_Leslie","US-English_Linda","US-English_Mary","US-English_Matthew","US-English_Polly","US-English_Ronald","US-English_Sofia","US-Spanish_Isabella","Welsh_Seren","Welsh-English_Gareth"]	

		myvoicescount = len(myvoices)
		print myvoicescount
		for i in range(0,myvoicescount):
			speech.setVoice(myvoices[i])
			print i
			voicename = myvoices[i].replace("-", "")
			voicename = myvoices[i].replace("_", "")
			print("I am speaking with "+voicename+"'s voice")
			onEndSpeaking ("I am speaking with "+voicename+"'s voice")
			onEndSpeaking ("I'm completely operational, and all my circuits are functioning perfectly.")

		# voices with unicode characters in the voice name
		speech.setVoice(u"French_Chloé")
		print("I am speaking with French Chloe's voice")
		onEndSpeaking ("I'm completely operational, and all my circuits are functioning perfectly.")

		speech.setVoice(u"Canadian-French_Adèle")
		print("I am speaking with French Adele's voice")
		onEndSpeaking ("I'm completely operational, and all my circuits are functioning perfectly.")
		
		speech.setVoice(u"US-Spanish_Matías")
		print("I am speaking with Spanish Matias' voice")
		onEndSpeaking ("I'm completely operational, and all my circuits are functioning perfectly.")



saystuff()
