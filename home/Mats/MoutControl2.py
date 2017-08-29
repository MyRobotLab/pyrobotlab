# Testing MouthControl using a virtual Arduino
# Saved here to be able to test with real hardware later ( 2017-03-02 )
leftPort = "COM1"
virtual = Runtime.start("virtual","VirtualArduino")
virtual.connect(leftPort)
# Start the TTS ( Text-To-Speech ) service MarySpeech and name it mouth
Voice="cmu-slt-hsmm" # Default female for MarySpeech
voiceType = Voice
mouth = Runtime.createAndStart("i01.mouth", "MarySpeech")
mouth.setVoice(voiceType)
# Start the STT ( Speech-To-Text ) service WebkitSpeechRecognition and name it ear 
ear = Runtime.createAndStart("i01.ear", "WebkitSpeechRecognition")
ear.addListener("publishText", python.name, "heard");
ear.addMouth(mouth)
# Html filter to clean the output from programab.  (just in case)
htmlfilter = Runtime.createAndStart("htmlfilter", "HtmlFilter")
htmlfilter.addTextListener(mouth)
# insert here ?
i01 = Runtime.start("i01","InMoov")
#
i01.startMouthControl(leftPort)
i01.mouthControl.setmouth(0,180) #105close, 160open
i01.startMouth()
i01.mouth = mouth
#
mouth.speakBlocking("Testing to say something")
