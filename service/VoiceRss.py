#########################################
# VoiceRss.py
# categories: speech
# more info @: http://myrobotlab.org/service/VoiceRss
#########################################

mouth = Runtime.start("mouth", "VoiceRss")

#possible voices ( selected voice is stored inside config until you change it )
print ("these are the voices I can have", mouth.getVoices())
print ("this is the voice I am using", mouth.getVoice())


# You sould't not expose keys here, inside gui is a good place
# But you can do it here ( only once is enough )
# An AES safe is used to store keys
# speech.setKeys("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

mouth.setVoice("en-gb")

mouth.speakBlocking("it works, yes I believe it does")
mouth.setVolume(0.7)
mouth.speakBlocking("Silent please")
