#EN : SHUTDOWN THE EAR ACTION AFTER 1mn INACTIVITY
#FR : ON COUPE VIRTUELEMENT LE MICRO APRES 1 MINUTE
StopListenTimer = Runtime.create("StopListenTimer","Clock")
StopListenTimer.setInterval(60000)
StopListenTimer = Runtime.start("StopListenTimer","Clock")

def StopListenTimerFunc(timedata):
	global IcanEarOnlyKnowsWords
	IcanEarOnlyKnowsWords+=1
	print "IcanEarOnlyKnowsWords=",IcanEarOnlyKnowsWords

StopListenTimer.addListener("pulse", python.name, "StopListenTimerFunc")
# start the clock
StopListenTimer.startClock()



#RANDOM TIME ACTIONS
VieAleatoire = Runtime.start("VieAleatoire","Clock")
VieAleatoire.setInterval(60000)
chatBot.getResponse("SAVEPREDICATES")
global TimeNoSpeak
TimeNoSpeak="OFF"
TuTeTais=0
def OnBalanceUnePhare_Aleatoire(timedata):
	global TimeNoSpeak
	global TuTeTais
	global IcanEarOnlyKnowsWords
	
	VieAleatoire.setInterval(random.randint(60000,600000))
	if TimeNoSpeak=="ON":
		if random.randint(0,1)==1:
			chatBot.getResponse("ALEATOIRE")
		else:
			chatBot.getResponse("ALEATOIRE2")
		IcanEarOnlyKnowsWords=1
	if TuTeTais==0:
		TimeNoSpeak="ON"
	

def TuTeTais_OuPas(value):
	global IcanEarOnlyKnowsWords
	IcanEarOnlyKnowsWords=1
	global TuTeTais
	TuTeTais=value
	
#create a message routes
VieAleatoire.addListener("pulse", python.name, "OnBalanceUnePhare_Aleatoire")
# start the clock
VieAleatoire.startClock()