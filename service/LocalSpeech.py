#########################################
# LocalSpeech.py
# description: used as a general template
# categories: speech
# more info @: http://myrobotlab.org/service/LocalSpeech
#########################################

# start the service
localSpeech = Runtime.start('localSpeech','LocalSpeech')

# ( windows )
# get available system voices for information ( check id )
# exemple : print localSpeech.getVoices();
# 0 Microsoft Zira Desktop - English (United States)
# 1 Microsoft Hortense Desktop - French
# override tts.exe temp output path : microsoftlocaltts.ttsExeOutputFilePath="c:\\tmp\\"

# ( macOs )
# set your voice from macos control panel
# you can test it using say command from terminal

localSpeech.setVoice("0")
localSpeech.speakBlocking(u"Hello this is an english voice")
localSpeech.setVoice("1")
localSpeech.speakBlocking(u"Bonjour ceci est une voix française, je teste les accents aussi avec le mot éléphant")
