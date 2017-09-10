#########################################
# AcapelaSpeech.py
# description: speech
# categories: speech
# more info @: http://myrobotlab.org/service/AcapelaSpeech
#########################################

# Example of how to use the Acapela Speech service
acapelaSpeech = Runtime.start("speech", "AcapelaSpeech")
acapelaSpeech.speak("Hello world")
voices = acapelaSpeech.getVoices()
str = "we have {0} voices".format(voices.size())
print(str)
acapelaSpeech.speak(str)

voiceIndex = 0
for voice in voices:
    acapelaSpeech.setVoice(voice)
    print(voice)
    acapelaSpeech.speak("Hello world. I'm " + voice)
    voiceIndex = voiceIndex + 1
    if (voiceIndex > 3):
        break;
