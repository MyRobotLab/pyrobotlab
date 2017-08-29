#this is WIP
tts = Runtime.start("tts", "MicrosoftLocalTTS");

print tts.getVoices();
# get available system voices for information ( check id )
# exemple :
# 0 Microsoft Hortense Desktop - French
# 1 Microsoft Zira Desktop - English (United States)

tts.setVoice("0")
tts.speakBlocking(u"Bonjour ceci est une voix française")
tts.setVoice("1")
tts.speak(u"Hello this is an english voice")
