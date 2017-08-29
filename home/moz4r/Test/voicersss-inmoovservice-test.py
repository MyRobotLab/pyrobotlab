i01 = Runtime.createAndStart("i01", "InMoov")
i01.mouth = Runtime.createAndStart("i01.mouth", "voiceRSS")

python.subscribe(i01.mouth.getName(),"publishStartSpeaking")
python.subscribe(i01.mouth.getName(),"publishEndSpeaking")

def onEndSpeaking(text):
	print "end speak"
def onStartSpeaking(text):
	print "start speak"

i01.mouth.setKey("!!! YOUR_KEY !!!")
i01.mouth.setVoice("fr-fr");
i01.mouth.speakBlocking(u"test accent utf8 : éléphant")
