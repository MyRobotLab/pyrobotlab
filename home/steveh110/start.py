

import random
import codecs
import socket
import sys
from java.lang import String
import urllib2
import random
import threading
import io
import itertools
import random
import time
from time import sleep
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
import feedparser
import re
import math
#pour connection avec automate Siemens
from Moka7 import S7Client
from Moka7 import S7
#import xml.dom.minidom
#from xml.dom.minidom import Node
#import xml.etree.ElementTree  #parser xml
from datetime import datetime
from subprocess import Popen, PIPE
from org.myrobotlab.service import Servo





#check runing folder
oridir=os.getcwd().replace("\\", "/")+"/"

#fix programab aimlif problems : remove all aimlif files
#print oridir+'ProgramAB/bots/'+myAimlFolder+'/aimlif'
try:
	shutil.rmtree(oridir+'ProgramAB/bots/steve/aimlif')
except: 
	pass


execfile(u'config.py')
execfile(u'opencv.py')
execfile(u'wikiDataFetcher.py')
execfile(u'traduction.py')
execfile(u'news.py')
execfile(u'domotique.py')




#demmarage des services


if (Arduino1 == 1) :
	ardu1 = Runtime.start("arduino1","Arduino")
	ardu1.connect(Arduino1Com)  #port de communication



opencv = Runtime.start("opencv","OpenCV")
python = Runtime.start("python","Python")

chatBot = Runtime.createAndStart("chatBot", "ProgramAB")
ear = Runtime.createAndStart("ear", "WebkitSpeechRecognition")
htmlFilter=Runtime.createAndStart("htmlFilter","HtmlFilter")
webgui = Runtime.create("WebGui","WebGui")
wdf=Runtime.createAndStart("wdf", "WikiDataFetcher") # WikiDataFetcher cherche des données sur les sites wiki



mouth=Runtime.createAndStart("mouth", "MarySpeech")

	

pid = Runtime.createAndStart("pid","Pid")
pid.setPID("x",0.1, 0, 0.1)
pid.setMode("x",1)
pid.setOutputRange("x",-2, 2)
pid.setControllerDirection("x",0)
pid.setSetpoint("x",70)




wdf.setLanguage("fr") # on cherche en français
wdf.setWebSite("frwiki") # On fait des recherches sur le site français de wikidata

sleep(0.5)

voiceType=Voice
ear.setLanguage("fr-FR")

sleep(5)
mouth.setLanguage("FR") #mouth.setLanguage(lang)
#print mouth.getVoices()
mouth.setVoice(voiceType)
#print mouth.getVoices()




chatBot.startSession("ProgramAB","Defaut","steve")

sleep(2)
 
ear.addTextListener(chatBot) # On creer une liaison de webKitSpeechRecognition vers Program AB
chatBot.addTextListener(htmlFilter) # On creer une liaison de Program AB vers html filter
htmlFilter.addTextListener(mouth) # On creer une liaison de htmlfilter vers mouth


 
def onStartSpeaking(text):
	ear.stopListening()
	print "Start Speaking"
 
def onEndSpeaking(text): 
	ear.startListening()
	print "Stop speaking"

webgui.autoStartBrowser(False)
webgui.startService()

sleep(1)
webgui.startBrowser("http://localhost:8888/#/service/ear")

 




if Arduino1 == 1 :
	#activation des servo
	RegardGD = Runtime.start("RegardGD","Servo")
	RotationTete = Runtime.start("RotationTete","Servo")
	Bouche = Runtime.start("Bouche","Servo")

	#start servo
	RegardGD.setMinMax(20,170)
	RegardGD.setRest(90)
	RegardGD.setSpeed(1)
	RegardGD.attach(ardu1.getName(),PinRegardGD)
	RegardGD.setRest(100)

	RotationTete.setMinMax(20,170)
	RotationTete.setRest(140)
	RotationTete.setSpeed(1)
	RotationTete.attach(ardu1.getName(),PinRotationTete)
	

	Bouche.setMinMax(20,170)
	Bouche.setRest(0)
	Bouche.setSpeed(1)
	Bouche.attach(ardu1.getName(),PinBouche)
	

	RegardGD.rest()
	RotationTete.rest()
	Bouche.rest()

	sleep(1)
















 
# add python as a listener to OpenCV data
# this tells the framework - whenever opencv.publishOpenCVData is invoked
# python.onOpenCVData will get called
python.subscribe("opencv", "publishOpenCVData")
python.subscribe("mouth", "publishEndSpeaking")
python.subscribe("mouth", "publishStartSpeaking") 

  




sleep(2)



mouth.speakBlocking(unicode("Fin de l'initialisation. merci de ta patience",'utf-8'))








def setModeVision(data) :
	global MODEVIDEO 
	if data==1 :
		MODEVIDEO = 1
		opencv.capture()
	if data==0 :
		MODEVIDEO = 10
		
Bouche.moveTo(50)
sleep(0.1)
Bouche.moveTo(0)
sleep(0.1)
Bouche.moveTo(40)
sleep(0.1)
Bouche.moveTo(10)
sleep(0.1)
Bouche.moveTo(50)
sleep(0.1)
Bouche.moveTo(0)
sleep(0.1)
Bouche.moveTo(20)
sleep(0.1)
Bouche.moveTo(10)
sleep(0.1)
