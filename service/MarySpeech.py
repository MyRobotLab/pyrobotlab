#start Service
mouth = Runtime.createAndStart("MarySpeech", "MarySpeech")

#speak!
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
mouth.setAudioEffects("FIRFilter+Robot(amount=50)");
