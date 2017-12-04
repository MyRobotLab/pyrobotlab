#start Service
mouth = Runtime.start("MarySpeech", "MarySpeech")

#possible voices
print ("these are the voices I can have", mouth.getVoices())
print ("this is the voice I am using", mouth.getVoice())

#install a voice:
#an overview over all official voices is available @ http://myrobotlab.org/service/MarySpeech
#mouth.installComponentsAcceptLicense(voicename)
#e.g.
#mouth.installComponentsAcceptLicense("bits1")

#switch voice:
#mouth.setVoice("bits1")
#mouth.setVoice("cmu-slt-hsmm")
#etc...

# ru voice : download & extract at mrl root : http://www.myai.cloud/mrl/mary-mrl-ru.zip
#mouth.setVoice("ac-nsh")
#mouth.speakBlocking(u"привет")

#speakBlocking!
# this blocks until speaking is done
mouth.speakBlocking(u"Hello world")
mouth.speakBlocking(u"I speak English. More voices are available, but they need to be installed")
mouth.speakBlocking(u"Echo echo echo")
mouth.speakBlocking(u"What should I use")


#add voice effects:
#more effects and information @ http://myrobotlab.org/service/MarySpeech
mouth.setAudioEffects("FIRFilter+Robot(amount=50)")
mouth.speakBlocking(u"this is after a sound effect ")

#speak!
# this not blocks speaking and next line is executed immediatly
mouth.speak(u"Happy birthday Kyle")
