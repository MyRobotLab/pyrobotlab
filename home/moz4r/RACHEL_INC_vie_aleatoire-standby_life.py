VieAleatoire = Runtime.start("VieAleatoire","Clock")
VieAleatoire.setInterval(20000)

TimeNoSpeak=1
TuTeTais=0
def OnBalanceUnePhare_Aleatoire(timedata):
	global TimeNoSpeak
	global TuTeTais
	VieAleatoire.setInterval(random.randint(20000,30000))
	if TimeNoSpeak==0:
		if random.randint(0,1)==1:
			chatBot.getResponse("ALEATOIRE")
		else:
			chatBot.getResponse("ALEATOIRE2")
	if TuTeTais==0:
		TimeNoSpeak=0

def TuTeTais_OuPas(value):
	global TuTeTais
	TuTeTais=value
	
#create a message routes
VieAleatoire.addListener("pulse", python.name, "OnBalanceUnePhare_Aleatoire")
# start the clock
VieAleatoire.startClock()