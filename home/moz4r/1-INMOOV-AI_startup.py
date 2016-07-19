
# ##############################################################################
# 							*** SETUP / INSTALLATION ***
# ##############################################################################
# STABLE FILES : https://github.com/MyRobotLab/pyrobotlab/tree/master/home/moz4r  [ RACHEL AIML + PYTHON ]
# UPDATED DEV FILES :  https://github.com/MyRobotLab/aiml/tree/master/bots/ [ RACHEL AIML + PYTHON ]
# -----------------------------------
# - Inmoov-AI Version 1.5 By Moz4r
# - Credit :
# - Rachel the humanoïde
# - Wikidatafetcher By Beetlejuice
# - Grog / Kwatters / and All MRL team
# - HairyGael
# - heisenberg333 for help to construct french AIML brain
# -----------------------------------
# !!! INSTALL : !!!
# !!! PLEASE copy all aiml files to : develop\ProgramAB\bots\rachel\aiml !!!
# !!! AND https://github.com/MyRobotLab/aiml/tree/master/bots/BOTS-FRENCH/INMOOV_AI/TXT to the root of MRL
# !!! + https://github.com/MyRobotLab/aiml/tree/master/bots/BOTS-ENGLISH/INMOOV_AI/TXT
#
# 
# I use realTime voice syncronisation but you can check mouthcontrol=1 in 2-INMOOV-AI_config.py 
# https://github.com/MyRobotLab/pyrobotlab/blob/master/home/moz4r/mouthcontrol_hardware.ino
# -
#  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#  !!!!!!!!!!!!!!!! CONFIG INSIDE THIS FILE !!! / ENTREZ VOS PARAMETRES DANS CE FICHIER  !!!!!!!!!!
#  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# 						2-INMOOV-AI_config.py


# ###
# 
# ##############################################################################
#  						*** END SETUP ***
# ##############################################################################




version=17
IcanStartToEar=0

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

global Ispeak
Ispeak=1


oridir=os.getcwd().replace("\\", "/")
#fix programab aimlif problems
try:
	shutil.rmtree(oridir+'/ProgramAB/bots/rachel/aimlif')
except: 
	pass

# check if a config file exist or create default one
if os.path.isfile(os.getcwd().replace("develop", "").replace("\\", "/")+'2-INMOOV-AI_config.py'):
	print("ok")
else:
	shutil.copyfile(os.getcwd().replace("develop", "").replace("\\", "/")+'2-INMOOV-AI_config.py.default',os.getcwd().replace("develop", "").replace("\\", "/")+'2-INMOOV-AI_config.py')
execfile('../2-INMOOV-AI_config.py')
	
gesturesPath = os.getcwd().replace("develop", "").replace("\\", "/")+"gestures"
BotURL=BotURL+"?lang="+lang+"&FixPhpCache="+str(time.time())


#some voice emotions
laugh = [" #LAUGH01# ", " #LAUGH02# ", " #LAUGH03# ", " ", " "]
troat = [" #THROAT01# ", " #THROAT02# ", " #THROAT03# ", " ", " ", " "]



image=Runtime.createAndStart("ImageDisplay", "ImageDisplay")


Runtime.createAndStart("chatBot", "ProgramAB")
wdf=Runtime.createAndStart("wdf", "WikiDataFetcher")

i01 = Runtime.createAndStart("i01", "InMoov")
i01.setMute(1)


i01.startMouth()

mouth = i01.mouth


webgui = Runtime.create("WebGui","WebGui")
webgui.autoStartBrowser(False)
webgui.startService()

#r=image.displayFullScreen("https://i.ytimg.com/vi/tIk1Mc170yg/maxresdefault.jpg",1)
sleep(0.5)
#r=image.displayFullScreen(os.getcwd().replace("develop", "")+'pictures\loading.jpg',1)
#r=image.displayFullScreen(os.getcwd().replace("develop", "")+'pictures\loading.jpg',1)
#webgui.start()

# inmoov init

if IsInmoovRight==1:

	right = Runtime.start("i01.right", "Arduino")
	right.publishState()
	right.connect(rightPort)
	sleep(1)
	if IhaveLights==1:

		right.pinMode(ROUGE, Arduino.OUTPUT)
		right.pinMode(VERT, Arduino.OUTPUT)
		right.pinMode(BLEU, Arduino.OUTPUT)
		

		right.digitalWrite(ROUGE,1)
		right.digitalWrite(VERT,0)
		right.digitalWrite(BLEU,1)
	
	
	i01.startRightArm(rightPort)
	i01.startRightHand(rightPort,BoardType)
	
	
if IsInmoovLeft==1:	
	
	left = Runtime.start("i01.left", "Arduino")
	left.publishState()
	left.connect(leftPort)
	sleep(1)
	i01.startLeftHand(leftPort,"")
	i01.startHead(leftPort,BoardType)
	if MRLmouthControl==1:
		i01.startMouthControl(leftPort)
		i01.head.jaw.setMinMax(JawMIN,JawMAX)
		i01.mouthControl.setmouth(JawMIN,JawMAX)
		i01.head.jaw.setRest(JawMIN)
	i01.startLeftArm(leftPort)
	torso = i01.startTorso(leftPort)
	i01.setHeadSpeed(0.5, 0.5)
	i01.head.neck.setMinMax(0,180)
	i01.head.neck.map(0,180,MinNeck,MaxNeck)
	i01.head.rothead.setMinMax(0,180)
	i01.head.rothead.map(0,180,MinRotHead,MaxRotHead)
	i01.moveHead(80,86,40,78,76)
	i01.setHeadSpeed(1, 1)
	i01.head.eyeX.setMinMax(0,180)
	i01.head.eyeY.setMinMax(0,180)
	i01.head.eyeX.setRest(90)
	i01.head.eyeY.setRest(90)
	i01.head.eyeY.rest()
	i01.head.eyeX.rest()
	i01.startEyesTracking(leftPort)
	i01.startHeadTracking(leftPort)
	i01.eyesTracking.pid.setPID("eyeX",20.0,5.0,0.1)
	i01.eyesTracking.pid.setPID("eyeY",20.0,5.0,0.1)
	i01.headTracking.pid.setPID("rothead",12.0,5.0,0.1)
	i01.headTracking.pid.setPID("neck",12.0,5.0,0.1)
		
	
	
if IsInmoovLeft==1 or IsInmoovRight==1:
	opencv = i01.opencv
else:
	opencv = Runtime.createAndStart("opencv","OpenCV")	
	


 




	

Runtime.createAndStart("htmlFilter", "HtmlFilter")


voiceType=Voice


if lang=="FR":
   WikiFile="prop.txt"
   wdf.setLanguage("fr")
   wdf.setWebSite("frwiki")
else:
   WikiFile="propEN.txt"
   wdf.setLanguage("en")
   wdf.setWebSite("enwiki")


sleep(1)
mouth.setVoice(voiceType)
mouth.setLanguage(lang)




chatBot.startSession("ProgramAB", "default", "rachel")
#ear.addTextListener(chatBot)
chatBot.addTextListener(htmlFilter)
htmlFilter.addListener("publishText", python.name, "talk") 

def SaveMemory(question,reponse,silent,justPredicates):
	sleep(0.5)
	chatBot.savePredicates()
	if justPredicates==0:
		ServerResponse="0"
		RetourServer=Parse("http://www.myai.cloud/shared_memory.php?action=update&question="+urllib2.quote(question)+"&reponse="+urllib2.quote(reponse.replace("'", " ")))
		print "http://www.myai.cloud/shared_memory.php?action=update&question="+urllib2.quote(question)+"&reponse="+urllib2.quote(reponse.replace("'", " "))
		if silent<>1:
			chatBot.getResponse("SAVEMEMORY")


chatBot.startSession("ProgramAB", "default", "rachel")
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

def No(data):
	if IsInmoovLeft==1:
		#i01.attach()
		i01.setHeadSpeed(1, 1)
		i01.moveHead(80,90,0,80,40)
		sleep(2)
		i01.moveHead(80,90,180,80,40)
		sleep(1)
		i01.moveHead(80,90,90,80,40)
		sleep(0.5)
	#Light(0,1,1)
	if IsInmoovLeft==1:
		i01.moveHead(81,50,90,78,40)
		sleep(0.5)
		i01.moveHead(79,120,90,78,40)
	chatBot.getResponse("IDONTUNDERSTAND")
	if IsInmoovLeft==1:
		i01.moveHead(80,50,90,78,40)
		sleep(0.5)
		i01.moveHead(83,120,90,78,40)
	sleep(0.5)
	#Light(1,1,1)
	if IsInmoovLeft==1:
		i01.moveHead(80,90,90,78,40)
	if IsInmoovLeft==1:
		i01.head.jaw.rest()
		#i01.detach()
		
def talk(data):
	sleep(0.1)
	#VieAleatoire.stopClock()
	
	if data!="":
		try:
			ear.stopListening()
		except: 
			pass
		mouth.speak(unicode(data,'utf-8'))

def talkBlocking(data):
	sleep(0.1)
	#VieAleatoire.stopClock()
	
	if data!="":
		try:
			ear.stopListening()
		except: 
			pass
		mouth.speakBlocking(unicode(data,'utf-8'))



if IhaveEyelids==1:
	execfile('../INMOOV-AI_paupieres_eyeleads.py')
execfile('../INMOOV-AI_vie_aleatoire-standby_life.py')
if IsInmoovLeft==1:
	execfile('../INMOOV-AI_opencv.py')
execfile('../INMOOV-AI_move_head_random.py')
#on bloque le micro quand le robot parle

def onEndSpeaking(text):
	MoveHeadTimer.stopClock()
	global Ispeak
	Ispeak=0
	global TimeNoSpeak
	VieAleatoire.startClock()
	TimeNoSpeak="OFF"
	#Light(0,0,0)
	if IcanStartToEar==1:
		try:
			ear.startListening()
		except: 
			pass

def onStartSpeaking(text):
	MoveHeadTimer.startClock()
	global Ispeak
	Ispeak=1
	try:
		ear.stopListening()
	except: 
		pass
	global TimeNoSpeak
	TimeNoSpeak="OFF"
	VieAleatoire.stopClock()
	#Light(1,1,1)
	
	
#ear.addTextListener(chatBot)	
def onText(text):
	ear.stopListening()	
	print text.replace("'", " ")
	chatBot.getResponse(text.replace("'", " "))
	


	

	
#on bloque le micro quand le robot parle
		
python.subscribe(mouth.getName(),"publishStartSpeaking")
python.subscribe(mouth.getName(),"publishEndSpeaking")




WebkitSpeachReconitionFix = Runtime.start("WebkitSpeachReconitionFix","Clock")
WebkitSpeachReconitionFix.setInterval(10000)

def WebkitSpeachReconitionON(timedata):
	global Ispeak
	if Ispeak==0:
		ear.startListening()
	
WebkitSpeachReconitionFix.addListener("pulse", python.name, "WebkitSpeachReconitionON")
# start the clock




		
def Parse(utfdata):
	#Light(1,1,0)
	utfdata = urllib2.urlopen(utfdata).read()
	utfdata = utfdata.replace("&#039;", "'").replace("http://fr.answers.yahoo.com/question/ind...", "")
	try:
		utfdata = utfdata.decode( "utf8" ).replace(" : ", random.choice(troat))
	except: 
		pass
	print utfdata
	#Light(1,1,1)
	return utfdata;


		
def Light(ROUGE_V,VERT_V,BLEU_V):
	if IhaveLights==1 and IsInmoovRight==1:
		right.digitalWrite(ROUGE,ROUGE_V)
		right.digitalWrite(VERT,VERT_V)
		right.digitalWrite(BLEU,BLEU_V)


	
def askWiki(query,question,retour): # retourne la description du sujet (query)
	#Light(1,0,0)
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
		QueryMemory(question,retour)
	else:
		talk(answer)
	#Light(1,1,1)
	


def getProperty(query, what): # retourne la valeur contenue dans la propriété demandée (what)
	#Light(1,0,0)
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
	#Light(1,1,1)
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
	
	DisplayPic(a)
	print BotURL+"&type=pic&pic="+urllib2.quote(image).replace(" ", "%20")
	#Light(1,1,1)
			
def Joke():
	MoveHead()
	a = Parse(BotURL+"&type=joke&genre="+JokeType).replace(" : ", random.choice(troat))
	mouth.speakBlocking(a+' '+random.choice(laugh))
	

	
def Yes(data):
	i01.attach()
	i01.moveHead(80,90,90,180,40)
	sleep(1)
	#Light(1,0,1)
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
	#Light(1,1,1)
	i01.moveHead(80,90,90,78,40)
	mouth.speakBlocking(random.choice(troat))
	i01.head.jaw.rest()
	i01.detach()
	

	
def ClearMemory():
	chatBot.setPredicate("default","topic","")
	chatBot.setPredicate("default","QUESTION_WhoOrWhat","")
	chatBot.setPredicate("default","QUESTION_sujet","")
	chatBot.setPredicate("default","QUESTION_action","")
	
def UpdateBotName(botname):
	if str(chatBot.getPredicate("default","bot_id"))=="unknown":
		bot_id=hashlib.md5(str(time.time()).encode('utf-8')).hexdigest()
	else:
		bot_id=str(chatBot.getPredicate("default","bot_id"))
	RetourServer=Parse("http://www.myai.cloud/shared_memory.php?action=UpdateBotName&bot_id="+urllib2.quote(bot_id)+"&botname="+urllib2.quote(botname.replace("'", " ")))
	print "http://www.myai.cloud/shared_memory.php?action=UpdateBotName&bot_id="+urllib2.quote(bot_id)+"&botname="+urllib2.quote(botname.replace("'", " "))
	chatBot.setPredicate("default","bot_id",bot_id)
	chatBot.setPredicate("default","botname",botname)
	chatBot.savePredicates()
	
def GetUnreadMessageNumbers():
	RetourServer=Parse("http://www.myai.cloud/shared_memory.php?action=GetUnreadMessageNumbers&bot_id="+str(chatBot.getPredicate("default","bot_id")))
	print "http://www.myai.cloud/shared_memory.php?action=GetUnreadMessageNumbers&bot_id="+str(chatBot.getPredicate("default","bot_id"))
	if RetourServer!="0":
		Light(0,1,1)
		r=image.displayFullScreen(os.getcwd().replace("develop", "")+'pictures\message.jpg',1)
		r=image.displayFullScreen(os.getcwd().replace("develop", "")+'pictures\message.jpg',1)
	else:
		Light(1,1,1)
		r=image.displayFullScreen(os.getcwd().replace("develop", "")+'pictures\logo.jpg',1)
		r=image.displayFullScreen(os.getcwd().replace("develop", "")+'pictures\logo.jpg',1)
	chatBot.getResponse("SYSTEM "+RetourServer+ " MESSAGE")
	
def GetMessage():
	RetourServer=Parse("http://www.myai.cloud/shared_memory.php?action=GetMessage&bot_id="+str(chatBot.getPredicate("default","bot_id")))
	print "http://www.myai.cloud/shared_memory.php?action=GetMessage&bot_id="+str(chatBot.getPredicate("default","bot_id"))
	chatBot.getResponse("SYSTEMREADMESSAGE "+RetourServer)
	
def NewMessage(botname,bot_id,question):
	RetourServer=Parse("http://www.myai.cloud/shared_memory.php?action=NewMessage&bot_id="+bot_id+"&botname="+urllib2.quote(botname.replace("'", " "))+"&question="+urllib2.quote(question.replace("'", " ")))
	print "http://www.myai.cloud/shared_memory.php?action=NewMessage&bot_id="+bot_id+"&botname="+urllib2.quote(botname.replace("'", " "))+"&question="+urllib2.quote(question.replace("'", " "))
	chatBot.getResponse(RetourServer)
	
def CheckRobot(botname):
	RetourServer=Parse("http://www.myai.cloud/shared_memory.php?action=CheckRobot&botname="+urllib2.quote(botname.replace("'", " ")))
	print "http://www.myai.cloud/shared_memory.php?action=CheckRobot&botname="+urllib2.quote(botname.replace("'", " "))
	chatBot.getResponse(RetourServer)	
	
	
	
def CheckVersion():
	RetourServer=Parse("http://www.myai.cloud/version.html")
	print str(RetourServer)+' '+str(version)
	if str(RetourServer)==str(version):
		print "software is OK"
		#chatBot.getResponse("IAMUPDATED")
	else:
		chatBot.getResponse("INEEDUPDATE")
	
		
def QueryMemory(question,retour):
	RetourServer=Parse("http://www.myai.cloud/shared_memory.php?action=select&question="+urllib2.quote(question))
	
	if RetourServer!="" and RetourServer!="0":
		chatBot.getResponse("SAY " + RetourServer)
	else:
		chatBot.getResponse(retour)
	
		
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
#if IsInmoov==1:
	#i01.detach()
#Light(1,1,1)



def loto(phrase,the,lucky):
	talkBlocking(phrase)
	talkBlocking(the+str(random.randint(1,49)))
	talkBlocking(the+str(random.randint(1,49)))
	talkBlocking(the+str(random.randint(1,49)))
	talkBlocking(the+str(random.randint(1,49)))
	talkBlocking(the+str(random.randint(1,49)))
	talkBlocking(lucky+str(random.randint(1,10)))

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


def rest():
	if IsInmoovLeft==1:
		i01.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
		i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
		i01.setHeadSpeed(1.0, 1.0)
		i01.setTorsoSpeed(1.0, 1.0, 1.0)
		i01.moveHead(80,86,82,78,76)
		i01.moveArm("left",5,90,0,10)
		i01.moveHand("left",2,2,2,2,2,90)
		i01.moveTorso(80,90,80)
		
	if IsInmoovRight==1:
		i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
		i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
		i01.moveArm("right",5,90,0,12)
		i01.moveHand("right",2,2,2,2,2,90)
	
	if IsInmoovLeft==1 or IsInmoovRight==1:
		i01.detach()
  
def trackHumans():
	i01.headTracking.findFace()
	#i01.opencv.SetDisplayFilter
	#i01.headTracking.faceDetect()
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
	print "name file is" , os.getcwd()+'\\'+str(photoFileName)
	Light(1,1,1)
	NeoPixelF(1)
	DisplayPic(os.getcwd()+'\\'+str(photoFileName))
	opencv.removeFilters()
	opencv.stopCapture()
	i01.startEyesTracking(leftPort)
	i01.startHeadTracking(leftPort)
	i01.eyesTracking.faceDetect()
	
	
	
# ##########################################################	
# program start :

Light(1,1,0)
ClearMemory()
if myBotname!="":
	UpdateBotName(myBotname)
#print gesturesPath
CheckVersion()
chatBot.getResponse("WAKE_UP")


rest()
if IsInmoovLeft==1:
	i01.head.attach()
if IsInmoovLeft==1 and tracking==1:
	trackHumans()

sleep(5)

i01.startEar()
ear = i01.ear
webgui.startBrowser("http://localhost:8888/#/service/i01.ear")
Light(1,1,1)
if lang=="FR":
   ear.setLanguage("fr-FR")
python.subscribe(ear.getName(),"publishText")
IcanStartToEar=1
WebkitSpeachReconitionFix.startClock()
#r=image.displayFullScreen("http://vignette2.wikia.nocookie.net/worldsofsdn/images/7/7a/Tyrell-corp.jpg",1)

if str(chatBot.getPredicate("default","botname"))!="unknown" and str(chatBot.getPredicate("default","botname"))!="default" and str(chatBot.getPredicate("default","botname"))!="":
	UpdateBotName(str(chatBot.getPredicate("default","botname")))
#if str(chatBot.getPredicate("default","bot_id"))!="unknown":
	#chatBot.getResponse("MESSAGESCHECK")
sleep(0.5)
r=image.displayFullScreen(os.getcwd().replace("develop", "")+'pictures\logo.jpg',1)
r=image.displayFullScreen(os.getcwd().replace("develop", "")+'pictures\logo.jpg',1)
Light(1,1,1)
NeoPixelF(1)

