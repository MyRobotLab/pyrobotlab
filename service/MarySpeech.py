#start Service
mouth = Runtime.start("MarySpeech", "MarySpeech")

#possible voices
print ("these are the voices I can have", mouth.getVoices())
print ("this is the voice I am using", mouth.getVoice())

#set a different voice
#mouth.setVoice("cmu-slt-hsmm")
#mouth.speak("Hello world I have a different voice")

#speak!
# this blocks until speaking is done
mouth.speakBlocking("Hello world")
mouth.speakBlocking("I speak English. More voices are available, but they need to be installed")
mouth.speakBlocking("Echo echo echo")
mouth.speakBlocking("What should I use")
mouth.speakBlocking("Happy birthday Kyle")

#install a voice:
#an overview over all official voices is available @ http://myrobotlab.org/service/MarySpeech
#mouth.installComponentsAcceptLicense(voicename)
#e.g.
#mouth.installComponentsAcceptLicense("bits1")

#switch voice:
#mouth.setVoice(voicename)
#mouth.setVoice("bits1")

#add voice effects:
#more effects and information @ http://myrobotlab.org/service/MarySpeech
mouth.setAudioEffects("FIRFilter+Robot(amount=50)")
mouth.speakBlocking("this is after a sound effect ")
