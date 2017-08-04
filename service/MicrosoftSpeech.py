#this is WIP
tts = Runtime.start("tts", "MicrosoftLocalTTS");

#get available system voices for information ( check id )
print tts.getVoices();

tts.setVoice("0")
tts.speakBlocking(u"Bonjour ceci est une voix française")
tts.setVoice("1")
tts.speak(u"Hello this is an english voice")
