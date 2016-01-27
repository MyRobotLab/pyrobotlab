#To set a specific voice using acapela speech:

acapelaSpeech = Runtime.createAndStart("speech", "AcapelaSpeech")
voices = acapelaSpeech.getVoices()
for voice in voices:
    acapelaSpeech.setVoice("Ryan") 

def CTG():
    for voice in voices:
        acapelaSpeech.setVoice("Klaus")

def CTE():
    for voice in voices:
        acapelaSpeech.setVoice("Graham")

def CTI():
    for voice in voices:
        acapelaSpeech.setVoice("Vittorio")

#in this case "Ryan" is the voice
#go to:
#http://www.acapela-group.com/voices/repertoire/
#here you find all voices available
################################################
# def CTG(): changes the voice to german
# def CTE(): to english
# def CTI(): to italian
