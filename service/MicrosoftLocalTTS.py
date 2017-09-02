#########################################
# MicrosoftLocalTTS.py
# description: used as a general template
# categories: speech
# more info @: http://myrobotlab.org/service/MicrosoftLocalTTS
#########################################

# start the service
microsoftlocaltts = Runtime.start('microsoftlocaltts','MicrosoftLocalTTS')

print microsoftlocaltts.getVoices();
# get available system voices for information ( check id )
# exemple :
# 0 Microsoft Zira Desktop - English (United States)
# 1 Microsoft Hortense Desktop - French

microsoftlocaltts.setVoice("0")
microsoftlocaltts.speak(u"Hello this is an english voice")
microsoftlocaltts.setVoice("1")
microsoftlocaltts.speakBlocking(u"Bonjour ceci est une voix française, je teste les accents aussi avec le mot éléphant")
