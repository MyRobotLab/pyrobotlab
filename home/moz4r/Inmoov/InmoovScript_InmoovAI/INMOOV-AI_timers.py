# -*- coding: utf-8 -*- 

###############################################################################
# timers.py : version 0.0.1
###############################################################################

###############################################################################
#  EN : SHUTDOWN THE EAR ACTION AFTER 1mn INACTIVITY
#  FR : ON COUPE VIRTUELEMENT LE MICRO APRES 1 MINUTE ( mode pause )
###############################################################################

def StopListenTimerFunc(timedata):
	global PleaseRobotDontSleep
	if PleaseRobotDontSleep==0:
		global IcanEarOnlyKnowsWords
		global RobotIsSleepingSoft
		IcanEarOnlyKnowsWords=IcanEarOnlyKnowsWords+1
		if DEBUG==1:
			print "dbg : IcanEarOnlyKnowsWords=",IcanEarOnlyKnowsWords
		if IcanEarOnlyKnowsWords==1:
			print "Sleeping mode ON"
			RobotIsSleepingSoft=1
			try:
				clockPaupiere.stopClock()
			except: 
				pass
			PositionPaupiere(90,90,0.4)
			sleep(3)
			PaupiereAttach(0)
			rest()
			#head.detach()
		
StopListenTimer = Runtime.create("StopListenTimer","Clock")
StopListenTimer.setInterval(60000)
StopListenTimer = Runtime.start("StopListenTimer","Clock")	
StopListenTimer.addListener("pulse", python.name, "StopListenTimerFunc")


###############################################################################
# Timer function to autostart webkit microphone every 10seconds
###############################################################################
WebkitSpeachReconitionFix = Runtime.start("WebkitSpeachReconitionFix","Clock")
WebkitSpeachReconitionFix.setInterval(15000)

def WebkitSpeachReconitionON(timedata):
	global LedWebkitListenFuncFix
	global Ispeak
	if Ispeak==0:
		ear.resumeListening()
	
		
		Light(1,1,0)

WebkitSpeachReconitionFix.addListener("pulse", python.name, "WebkitSpeachReconitionON")			

##################################################################################
# RANDOM TIME ACTIONS
##################################################################################

VieAleatoire = Runtime.start("VieAleatoire","Clock")
VieAleatoire.setInterval(120000)
chatBot.getResponse("SAVEPREDICATES")
global TimeNoSpeak
TimeNoSpeak="OFF"
TuTeTais=0

def OnBalanceUnePhare_Aleatoire(timedata):
	global TimeNoSpeak
	global TuTeTais
	global RamdomSpeak
	global RobotIsStarted
	if RobotIsStarted==1:
		RamdomSpeak=1
	
	VieAleatoire.setInterval(random.randint(220000,700000))
	if TimeNoSpeak=="ON":
		if random.randint(0,1)==1:
			chatBot.getResponse("ALEATOIRE")
		else:
			chatBot.getResponse("ALEATOIRE2")
		
	if TuTeTais==0:
		TimeNoSpeak="ON"
	

def TuTeTais_OuPas(value):
	global TuTeTais
	TuTeTais=value
	
#create a message routes
VieAleatoire.addListener("pulse", python.name, "OnBalanceUnePhare_Aleatoire")

##################################################################################
# Timer pour le watchdog tous les 5 secondes
##################################################################################

def sendRefresh(timedata):
	global WatchDog
	if WatchDog==1:
		watchdogRefresh()
  
watchdogTimer = Runtime.start("watchdogTimer","Clock")
watchdogTimer.setInterval(5000)
watchdogTimer.addListener("pulse", python.name, "sendRefresh")

##################################################################################
# Déclaration du timer de mise à jour des données Activator  
##################################################################################

def sendRefreshData(timedata):
  updateDataRequest()

updateDataTimer = Runtime.start("updateDataTimer","Clock")
updateDataTimer.setInterval(30000)
updateDataTimer.addListener("pulse", python.name, "sendRefreshData")

##################################################################################
# Fonction qui démarre tout les timers
# doit être mis aprés démarrage du système
##################################################################################

def startAllTimer():
	watchdogTimer.startClock()
	VieAleatoire.startClock()
	StopListenTimer.startClock()
	updateDataTimer.startClock()
	WebkitSpeachReconitionFix.startClock()

##################################################################################
# generic timeout function used in some loops to prevent infinite :)
##################################################################################

def TimoutTimerFunc(timedata):
	global TimoutVar
	TimoutVar+=1
	if TimoutVar==1:
		TimoutTimer.stopClock()
	
TimoutTimer = Runtime.start("TimoutTimer","Clock")
TimoutTimer.setInterval(60000)
TimoutTimer.addListener("pulse", python.name, "TimoutTimerFunc")

##################################################################################
# makerfaire matt move head random twice a minute
##################################################################################

MoveHeadRandomEveryMinute= Runtime.start("MoveHeadRandomEveryMinute","Clock")
MoveHeadRandomEveryMinute.setInterval(11000)

global MoveHeadRandomEveryMinuteVar
MoveHeadRandomEveryMinuteVar=1
def MoveHeadRandomEveryMinuteFunc(timedata):
	global MoveHeadRandomEveryMinuteVar
	global Ispeak
	
	if  Ispeak==0 and MoveHeadRandomEveryMinuteVar==0:
		MoveHeadRandomEveryMinuteVar=1
		MoveHeadTimer.stopClock()
		
	if Ispeak==0 and MoveHeadRandomEveryMinuteVar==1 and random.randint(1,3)==3:
		MoveHeadRandomEveryMinuteVar=0
		MoveHeadTimer.startClock()
		
	MoveHeadRandomEveryMinute.setInterval(random.randint(8000,11000))
		
MoveHeadRandomEveryMinute.addListener("pulse", python.name, "MoveHeadRandomEveryMinuteFunc")



