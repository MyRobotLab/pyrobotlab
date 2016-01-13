#To set a specific voice using acapela speech:

acapelaSpeech = Runtime.createAndStart("speech", "AcapelaSpeech")
voices = acapelaSpeech.getVoices()
for voice in voices:
    acapelaSpeech.setVoice("Ryan") 

#in this case "Ryan" is the voice
#go to:
#http://www.acapela-group.com/voices/repertoire/
#here you find all voices available
