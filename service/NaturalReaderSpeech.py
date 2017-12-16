#########################################
# NaturalReaderSpeech.py
# description: Natural Reader based speech service.
# categories: speech
# more info @: http://myrobotlab.org/service/NaturalReaderSpeech
#########################################


# start the service
speech = Runtime.start("Speech", "NaturalReaderSpeech")
speech.setVoice(u"Korean_Seoyeon")
speech.speakBlocking(u"내 로봇 연구소는 너무 강력하다")
#setRate is -x/0/+x
speech.setRate(-50)
speech.setVoice(u"US-English_Ronald")
speech.speakBlocking(u"Hey, Watson was here!")
#unicode test
speech.setVoice(u"French_Chloé")
speech.speakBlocking(u"coucou les francophones")