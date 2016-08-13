VieAleatoire = Runtime.start("VieAleatoire","Clock")
VieAleatoire.setInterval(60000)
chatBot.getResponse("SAVEPREDICATES")
global TimeNoSpeak
TimeNoSpeak="OFF"
TuTeTais=0
def OnBalanceUnePhare_Aleatoire(timedata):
	global TimeNoSpeak
	global TuTeTais
	
	VieAleatoire.setInterval(random.randint(60000,600000))
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
# start the clock
VieAleatoire.startClock()