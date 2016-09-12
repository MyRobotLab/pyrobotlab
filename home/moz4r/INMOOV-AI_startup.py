
# ##############################################################################
# 							*** SETUP / INSTALLATION ***
# ##############################################################################
# STABLE FILES : https://github.com/MyRobotLab/pyrobotlab/tree/master/home/moz4r  [ AIML + PYTHON ]
# UPDATED DEV FILES :  https://github.com/MyRobotLab/aiml/tree/master/bots/ [ AIML + PYTHON ]
# -----------------------------------
# - Inmoov-AI Version 1.8 By Moz4r
# - Credit :
# - Rachel the humanoïde
# - Wikidatafetcher By Beetlejuice
# - Azure translator by Papaoutai
# - Grog / Kwatters / and All MRL team
# - HairyGael
# - Heisenberg
# - Grattounet
# - Lecagnois
# -----------------------------------
# !!! INSTALL : !!!
# !!! PLEASE copy all aiml files to : develop\ProgramAB\bots\YOUR_BOT_NAME\aiml !!!
# !!! AND https://github.com/MyRobotLab/aiml/tree/master/bots/BOTS-FRENCH/INMOOV_AI/TXT to the root of MRL
# !!! + https://github.com/MyRobotLab/aiml/tree/master/bots/BOTS-ENGLISH/INMOOV_AI/TXT
#
# 
# I use realTime voice syncronisation but you can check mouthcontrol=1 in INMOOV-AI_config.py 
# https://github.com/MyRobotLab/pyrobotlab/blob/master/home/moz4r/mouthcontrol_hardware.ino
# -
#  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#  !!!!!!!!!!!!!!!! CONFIG INSIDE THIS FILE !!! / ENTREZ VOS PARAMETRES DANS CE FICHIER  !!!!!!!!!!
#  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# 						INMOOV-AI_config.py


# ###
# 
# ##############################################################################
#  						*** END SETUP ***
# ##############################################################################




version=19
global IcanStartToEar
IcanStartToEar=0

#Python libraries

import urllib2
from java.lang import String
import random
import threading
import io
import itertools
import random
import time
import textwrap
import codecs
import socket
import os
import shutil
import hashlib
import subprocess
import json
import time
import csv
from datetime import datetime
from subprocess import Popen, PIPE
from org.myrobotlab.service import Servo



#check runing folder
oridir=os.getcwd().replace("\\", "/")+"/"
#print oridir

# check if a config file exist or create default one
if os.path.isfile(oridir + '2-INMOOV-AI_config.py'):
	shutil.move(oridir + '2-INMOOV-AI_config.py', oridir + 'INMOOV-AI_config.py')

if os.path.isfile(oridir + 'INMOOV-AI_config.py'):
	print("ok")
else:
	shutil.copyfile(oridir + 'INMOOV-AI_config.py.default',oridir + 'INMOOV-AI_config.py')

execfile('INMOOV-AI_config.py')
	
gesturesPath = (oridir)+"gestures"
BotURL=BotURL+"?lang="+lang+"&FixPhpCache="+str(time.time())

#fix programab aimlif problems : remove all aimlif files
#print oridir+'ProgramAB/bots/'+myAimlFolder+'/aimlif'
try:
	shutil.rmtree(oridir+'ProgramAB/bots/'+myAimlFolder+'/aimlif')
except: 
	pass

#some voice emotions
laugh = [" #LAUGH01# ", " #LAUGH02# ", " #LAUGH03# ", " ", " "]
troat = [" #THROAT01# ", " #THROAT02# ", " #THROAT03# ", " ", " ", " "]

#service pictures
image=Runtime.createAndStart("ImageDisplay", "ImageDisplay")

#service aiml
Runtime.createAndStart("chatBot", "ProgramAB")

#service wikidata
Runtime.createAndStart("wdf", "WikiDataFetcher")

#service inmoov
i01 = Runtime.create("i01", "InMoov")

#disable autocheck
i01.setMute(1)

#start acapela and webkit ear
i01.startMouth()
i01.startEar()
ear = i01.ear
mouth = i01.mouth

#start webgui
webgui = Runtime.create("WebGui","WebGui")
webgui.autoStartBrowser(False)
webgui.startService()

#r=image.displayFullScreen("https://i.ytimg.com/vi/tIk1Mc170yg/maxresdefault.jpg",1)
sleep(0.1)
#r=image.displayFullScreen(os.getcwd().replace("develop", "")+'pictures\loading.jpg',1)
#r=image.displayFullScreen(os.getcwd().replace("develop", "")+'pictures\loading.jpg',1)
#webgui.start()

# inmoov servo configuration

left = Runtime.create("i01.left", "Arduino")
leftHand = Runtime.create("i01.leftHand", "InMoovHand")
leftArm = Runtime.create("i01.leftArm", "InMoovArm")
right=Runtime.create("i01.right", "Arduino")
rightHand = Runtime.create("i01.rightHand", "InMoovHand")
rightArm = Runtime.create("i01.rightArm", "InMoovArm")
head = Runtime.create("i01.head","InMoovHead")

leftHand.thumb.setMinMax(ThumbLeftMIN,ThumbLeftMAX) 
leftHand.index.setMinMax(IndexLeftMIN,IndexLeftMAX) 
leftHand.majeure.setMinMax(majeureLeftMIN,majeureLeftMAX) 
leftHand.ringFinger.setMinMax(ringFingerLeftMIN,ringFingerLeftMAX) 
leftHand.pinky.setMinMax(pinkyLeftMIN,pinkyLeftMAX) 
leftHand.thumb.map(0,180,ThumbLeftMIN,ThumbLeftMAX) 
leftHand.index.map(0,180,IndexLeftMIN,IndexLeftMAX) 
leftHand.majeure.map(0,180,majeureLeftMIN,majeureLeftMAX) 
leftHand.ringFinger.map(0,180,ringFingerLeftMIN,ringFingerLeftMAX) 
leftHand.pinky.map(0,180,majeureLeftMIN,majeureLeftMAX) 

rightHand.thumb.setMinMax(ThumbRightMIN,ThumbRightMAX) 
rightHand.index.setMinMax(IndexRightMIN,IndexRightMAX) 
rightHand.majeure.setMinMax(majeureRightMIN,majeureRightMAX) 
rightHand.ringFinger.setMinMax(ringFingerRightMIN,ringFingerRightMAX) 
rightHand.pinky.setMinMax(pinkyRightMIN,pinkyRightMAX) 
rightHand.thumb.map(0,180,ThumbRightMIN,ThumbRightMAX) 
rightHand.index.map(0,180,IndexRightMIN,IndexRightMAX) 
rightHand.majeure.map(0,180,majeureRightMIN,majeureRightMAX) 
rightHand.ringFinger.map(0,180,ringFingerRightMIN,ringFingerRightMAX) 
rightHand.pinky.map(0,180,majeureRightMIN,majeureRightMAX)

head.jaw.setMinMax(JawMIN,JawMAX)
if JawInverted==1:
	head.jaw.map(0,180,JawMAX,JawMIN)
else:
	head.jaw.map(0,180,JawMIN,JawMAX)
head.jaw.setMinMax(0,180)
head.jaw.setRest(0)

head.eyeX.setMinMax(EyeXMIN,EyeXMAX)
head.eyeX.map(0,180,EyeXMIN,EyeXMAX)
head.eyeX.setMinMax(0,180)
head.eyeY.setMinMax(EyeYMIN,EyeYMAX)
head.eyeY.map(0,180,EyeYMIN,EyeYMAX)
head.eyeY.setMinMax(0,180)
head.eyeX.setRest(90)
head.eyeY.setRest(90)
head.neck.setMinMax(MinNeck,MaxNeck)
head.neck.setRest(90)
head.rothead.setMinMax(MinRotHead,MinRotHead)

if RotHeadInverted==1: 
	head.rothead.map(0,180,MaxRotHead,MinRotHead)
else:
	head.rothead.map(0,180,MinRotHead,MaxRotHead)

if NeckInverted==1: 
	head.neck.map(0,180,MaxNeck,MinNeck)
else:
	head.neck.map(0,180,MinNeck,MaxNeck)
	
#start the arduino
	
if IsInmoovArduino==1:
	i01 = Runtime.start("i01","InMoov")
	i01.startAll(leftPort, rightPort)
	sleep(1)

	left = Runtime.start("i01.left", "Arduino")
	i01.startHead(leftPort)
	head.rothead.setSpeed(0.2)
	head.neck.setSpeed(0.2)
	head.neck.setMinMax(0,180)
	head.rothead.setMinMax(0,180)
	head.rothead.moveTo(1)
	head.neck.rest()
	head.rothead.setRest(90)
	i01.startLeftHand(leftPort,"")
	i01.startLeftArm(leftPort)
	
	if MRLmouthControl==1:
		i01.startMouthControl(leftPort)
		i01.mouthControl.setmouth(0,180)
		
	torso = i01.startTorso(leftPort)
	
	i01.head.eyeY.rest()
	i01.head.eyeX.rest()

	i01.startEyesTracking(leftPort,22,24)
	i01.startHeadTracking(leftPort)
	
	right = Runtime.start("i01.right", "Arduino")
	i01.startRightHand(rightPort,"")
	i01.startRightArm(rightPort)
	
#gestion des mouvement latéraux de la tete ( mod pistons de Bob )
	
	HeadSide = Runtime.start("HeadSide","Servo")
	HeadSide.setMinMax(MinHeadSide , MaxHeadSide)
	if HeadSideArduino=="left":
		HeadSide.attach(left, HeadSidePin)
	else:
		HeadSide.attach(right, HeadSidePin)
	HeadSide.map(0,180,MinHeadSide,MaxHeadSide)
	HeadSide.setMinMax(0,180)
	HeadSide.setRest(90)
	HeadSide.setSpeed(0.2)

	opencv = i01.opencv

Runtime.createAndStart("htmlFilter", "HtmlFilter")

voiceType=Voice

if lang=="FR":
   WikiFile="BDD/WIKI_prop.txt"
   wdf.setLanguage("fr")
   wdf.setWebSite("frwiki")
else:
   WikiFile="BDD/WIKI_propEN.txt"
   wdf.setLanguage("en")
   wdf.setWebSite("enwiki")


sleep(0.1)
mouth.setVoice(voiceType)
mouth.setLanguage(lang)

chatBot.startSession("ProgramAB", "default", myAimlFolder)
chatBot.addTextListener(htmlFilter)
htmlFilter.addListener("publishText", python.name, "talk") 

		

#var to set when robot is speaking
 
global Ispeak
Ispeak=1
global MoveHeadRandom
MoveHeadRandom=1

chatBot.startSession("ProgramAB", "default", myAimlFolder)
#ear.addTextListener(chatBot)
chatBot.addTextListener(htmlFilter)
htmlFilter.addListener("publishText", python.name, "talk") 

if Neopixel!="COMX":
	serial = Runtime.createAndStart("serial","Serial")
	serial.connect(Neopixel, 9600, 8, 1, 0)

def NeoPixelF(valNeo):
	if Neopixel!="COMX":
		serial.write(valNeo)
	else:
		print(valNeo)

NeoPixelF(3)


			
def talk(data):
	if data[0:2]=="l ":
		data=data.replace("l ", "l'")
	data=data.replace(" l ", " l'")
	
	ear.startListening() #fix onclick micro
	
	if data!="":
		mouth.speak(unicode(data,'utf-8'))
		
	if IsInmoovArduino==1:
		if random.randint(1,3)==1:
			i01.head.eyeX.moveTo(0)
			sleep(2)
			i01.head.eyeX.moveTo(180)
			sleep(1)
			i01.head.eyeX.moveTo(90)

def talkBlocking(data):
		
	if data!="":
		mouth.speakBlocking(unicode(data,'utf-8'))

#We include all InmoovAI mods
# -- coding: utf-8 --
execfile('INMOOV-AI_memory.py')
if IhaveEyelids==1:
	execfile('INMOOV-AI_paupieres_eyeleads.py')
execfile('INMOOV-AI_vie_aleatoire-standby_life.py')
if IsInmoovArduino==1:
	execfile('INMOOV-AI_opencv.py')
execfile('INMOOV-AI_move_head_random.py')
execfile('INMOOV-AI_azure_translator.py')
execfile('INMOOV-AI_messenger.py')
execfile('INMOOV-AI_KnowledgeFetchers.py')
execfile('INMOOV-AI_games.py')
execfile('INMOOV-AI_reminders.py')
execfile('INMOOV-AI_gestures.py')
execfile('INMOOV-AI_domotique.py')
execfile(u'INMOOV-AI_dictionaries.py')

# We listen when the robot is starting to speak to avoid ear listening
# If you click on the webkit mic icon, this trick is broken


def onEndSpeaking(text):
	global IcanStartToEar
	print "End speaking debug"
	global MoveHeadRandom
	MoveHeadTimer.stopClock()
	global Ispeak
	Ispeak=0
	global TimeNoSpeak
	VieAleatoire.startClock()
	TimeNoSpeak="OFF"
	#Light(0,0,0)
	if IsInmoovArduino==1:
		i01.moveHead(90,90,90,90,90)
	MoveHeadRandom=1
	
	if IcanStartToEar==1:
		try:
			ear.startListening()
		except: 
			pass
	WebkitSpeachReconitionFix.startClock()
	IcanStartToEar=1

	
def onStartSpeaking(text):
	
	print "Start speaking debug"
	global Ispeak
	Ispeak=1
	WebkitSpeachReconitionFix.stopClock()
	global MoveHeadRandom
	if 'non' in text or 'no' in text:
		No('no')
		MoveHeadRandom=0
		#print("no detected")
	if 'oui' in text or 'yes' in text:
		Yes('yes')
		#print("yes detected")
		MoveHeadRandom=0
	if MoveHeadRandom==1:
		MoveHeadTimer.startClock()
	try:
		ear.stopListening()
	except: 
		pass
	global TimeNoSpeak
	TimeNoSpeak="OFF"
	VieAleatoire.stopClock()
	
	#Light(1,1,1)
	
	
#We intercept what the robot is listen to change some values
#here we replace ' by space because AIML doesn't like '
def onText(text):
	#print text.replace("'", " ")
	global Ispeak
	if Ispeak==0:
		chatBot.getResponse(text.replace("'", " "))
	

	
python.subscribe(mouth.getName(),"publishStartSpeaking")
python.subscribe(mouth.getName(),"publishEndSpeaking")


#Timer function to autostart webkit microphone every 10seconds
WebkitSpeachReconitionFix = Runtime.start("WebkitSpeachReconitionFix","Clock")
WebkitSpeachReconitionFix.setInterval(15000)

def WebkitSpeachReconitionON(timedata):
	sleep(0.2)
	global Ispeak
	if Ispeak==0:
		try:
			ear.startListening()
		except: 
			pass
			
WebkitSpeachReconitionFix.addListener("pulse", python.name, "WebkitSpeachReconitionON")




		
def Parse(utfdata):
	#Light(1,1,0)
	utfdata = urllib2.urlopen(utfdata).read()
	utfdata = utfdata.replace("&#039;", "'").replace("http://fr.answers.yahoo.com/question/ind...", "")
	try:
		utfdata = utfdata.decode( "utf8" ).replace(" : ", random.choice(troat))
	except: 
		pass
	#print utfdata
	#Light(1,1,1)
	return utfdata;


		
def Light(ROUGE_V,VERT_V,BLEU_V):
	if IhaveLights==1 and IsInmoovArduino==1:
		print 0



	
def getDate(query, ID):# Cette fonction permet d'afficher une date personnalisée (mardi, le 10 juin, 1975, 12h38 .....)
	answer = ( wdf.getTime(query,ID,"day") +" " +wdf.getTime(query,ID,"month") + " " + wdf.getTime(query,ID,"year"))
	#print " La date est : " + answer
	chatBot.getResponse("say Le " + answer)
	

	
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
	time.sleep(10)
	image.exitFS()
	image.closeAll()			
	



	
def UpdateBotName(botname):
	if str(chatBot.getPredicate("default","bot_id"))=="unknown":
		bot_id=hashlib.md5(str(time.time()).encode('utf-8')).hexdigest()
	else:
		bot_id=str(chatBot.getPredicate("default","bot_id"))
	RetourServer=Parse("http://www.myai.cloud/shared_memory.php?action=UpdateBotName&bot_id="+urllib2.quote(bot_id)+"&botname="+urllib2.quote(botname.replace("'", " ")))
	#print "http://www.myai.cloud/shared_memory.php?action=UpdateBotName&bot_id="+urllib2.quote(bot_id)+"&botname="+urllib2.quote(botname.replace("'", " "))
	chatBot.setPredicate("default","bot_id",bot_id)
	chatBot.setPredicate("default","botname",botname)
	chatBot.savePredicates()
	


	
def CheckVersion():
	RetourServer=Parse("http://www.myai.cloud/version.html")
	#print str(RetourServer)+' '+str(version)
	if str(RetourServer)==str(version):
		print "software is OK"
		#chatBot.getResponse("IAMUPDATED")
	else:
		chatBot.getResponse("INEEDUPDATE")
		sleep(3)
		
def Meteo(data):
	a = Parse(BotURL+"&type=meteo&units="+units+"&city="+urllib2.quote(data).replace(" ", "%20"))
	#print BotURL+"&type=meteo&units="+units+"&city="+urllib2.quote(data).replace(" ", "%20")
	mouth.speakBlocking(a)
	



def trackHumans():
	#i01.headTracking.findFace()
	#i01.opencv.SetDisplayFilter
	i01.headTracking.faceDetect()
	i01.eyesTracking.faceDetect()
	print "test"

def TakePhoto(messagePhoto):
	talkBlocking(messagePhoto)
	global FaceDetected
	global FaceDetectedCounter
	global startTimerFunction
	FaceDetectedCounter=0
	FaceDetected=0
	Light(0,0,0)
	startTimerFunction=0
	NoFaceDetectedTimer.startClock()
	#opencv.setInputSource("camera")
	#opencv.setCameraIndex(0)
	#opencv.addFilter("pdown","PyramidDown")
	#opencv.setDisplayFilter("pdown")
	#opencv.capture()
	#sleep(1)
	#photoFileName = opencv.recordSingleFrame()
	#print "name file is" , photoFileName

def PhotoProcess(messagePhoto):
	global FaceDetected
	Light(1,1,1)
	FaceDetectedCounter=0
	FaceDetected=1
	NoFaceDetectedTimer.stopClock()
	NeoPixelF(3)
	talkBlocking(messagePhoto)
	Light(1,1,1)
	talkBlocking("chi i i i i i i i i ize")
	sleep(0.5)
	Light(0,0,0)
	sleep(0.1)
	Light(1,1,1)
	sleep(0.1)
	Light(0,0,0)
	sleep(0.1)
	Light(1,1,1)
	sleep(0.1)
	i01.stopTracking()
	opencv.removeFilters()
	opencv.stopCapture()
	sleep(1)
	opencv.setInputSource("camera")
	opencv.setCameraIndex(0)
	opencv.capture()
	sleep(0.5)
	Light(0,0,0)
	photoFileName = opencv.recordSingleFrame()
	#print "name file is" , os.getcwd()+'\\'+str(photoFileName)
	Light(1,1,1)
	NeoPixelF(1)
	DisplayPic(os.getcwd()+'\\'+str(photoFileName))
	opencv.removeFilters()
	opencv.stopCapture()
	i01.startEyesTracking(leftPort)
	i01.startHeadTracking(leftPort)
	i01.eyesTracking.faceDetect()
	

def PlayUtub(q,num):
	if q=="stop" and num==0:
		subprocess.Popen("taskkill /F /T /PID %i"%proc1.pid , shell=True)
		sleep(2)
		webgui.startBrowser("http://localhost:8888/#/service/i01.ear")
	else:
		webgui.startBrowser("http://www.myai.cloud/utub/?num="+str(num)+"&q="+str(q).encode('utf-8'))
		#print "http://www.myai.cloud/utub/?num="+str(num)+"&q="+str(q).encode('utf-8')
		


	

def ShutDown():
	talkBlocking("Extinction")
	MoveHeadRandom=0
	sleep(1)
	if IsInmoovArduino==1:
		i01.setHeadSpeed(0.3, 0.3)
		i01.moveHead(0,180)
		HeadSide.moveTo(90)
	sleep(4)
	
	HeadSide.detach()
	i01.detach()
	sleep(1)
	#runtime.shutdown()


	
# ##########################################################	


# program start :

Light(1,1,0)

#on remet à zero certaines variables de l'aiml ( sujets de discussion... )
ClearMemory()
if myBotname!="":
	UpdateBotName(myBotname)


rest()
if IsInmoovArduino==1:
	i01.head.attach()
	#head.rothead.setSpeed(0.2)
if IsInmoovArduino==1 and tracking==1:
	trackHumans()

proc1 = subprocess.Popen("%programfiles(x86)%\Google\Chrome\Application\chrome.exe", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

Light(1,1,1)

#r=image.displayFullScreen("http://vignette2.wikia.nocookie.net/worldsofsdn/images/7/7a/Tyrell-corp.jpg",1)

if str(chatBot.getPredicate("default","botname"))!="unknown" and str(chatBot.getPredicate("default","botname"))!="default" and str(chatBot.getPredicate("default","botname"))!="":
	UpdateBotName(str(chatBot.getPredicate("default","botname")))

#if str(chatBot.getPredicate("default","bot_id"))!="unknown":
	#chatBot.getResponse("MESSAGESCHECK")

#r=image.displayFullScreen(os.getcwd().replace("develop", "")+'pictures\logo.jpg',1)
#r=image.displayFullScreen(os.getcwd().replace("develop", "")+'pictures\logo.jpg',1)
Light(1,1,1)
NeoPixelF(1)

webgui.startBrowser("http://localhost:8888/#/service/i01.ear")
sleep(4)

GetUnreadMessageNumbers("0")
anniversaire("0")
CheckVersion()
sleep(2)
chatBot.getResponse("WAKE_UP")
#petit fix pour dire au robot qu'il eut commencer à écouter


if lang=="FR":
   ear.setLanguage("fr-FR")
python.subscribe(ear.getName(),"publishText")

WebkitSpeachReconitionFix.startClock()
#test de dictionaire
#print(Singularize("travaux"),Singularize("nez"),Singularize("vitraux"),Singularize("bocaux"),Singularize("poux"),Singularize("époux"),Singularize("fraises"))