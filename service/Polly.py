#########################################
# Polly.py
# categories: speech
# more info @: http://myrobotlab.org/service/Polly
#########################################

# start the service
polly = Runtime.start('polly','Polly')
polly.setKey("YOUR_KEY_ID","YOUR_KEY_SECRET")
polly.setLanguage("en")
polly.setVoice(u"Brian")
polly.speakBlocking(u"Hello this is Brian speakin !")
polly.setLanguage("fr")
polly.setVoice(u"Céline")
polly.speakBlocking(u"Ceci est une voix française en U T F 8")
