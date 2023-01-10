# ##############################################################################
# 								TIMERS ACTION
# Timer donne l heure toutes les heures
# plus phrase aleatoire toutes les 10 minutes
###############################################################################
import time
from datetime import datetime
import random

#AudioPlayer = runtime.start('AudioPlayer', 'AudioFile')
#AudioPlayer = runtime.getService("i01.mouth.audiofile")
AudioPlayer = runtime.start('i01.mouth.audioFile', 'AudioFile')
HumerTime = Runtime.start("HumerTime","Clock")
HumerTime.setInterval(60000)

def HumerTime_def(timedata):
	minute = str(timedata)[14:16]
	heure = str(timedata)[11:13]
	# donne l heure avec humour 
	if minute =="00" :
		#talkBlocking("il est exactement "+heure+" heure")
		Mheure = (str(random.randint(1,5))+".mp3")
		AudioPlayer.playFile('data/sounds/heure/'+heure+'/'+Mheure)
		
	## lance une humeur au hasard	
	if minute=="08" or minute=="16" or minute=="24" or minute=="33" or minute=="41"or minute=="51":
		surprise = (str(random.randint(1,305))+".mp3")
		AudioPlayer.playFile('data/sounds/surprise/'+surprise)

HumerTime.addListener("pulse", python.name, "HumerTime_def")		
HumerTime.startClock()

