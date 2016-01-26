from java.lang import String
webgui = Runtime.createAndStart("webgui","WebGui")
arduino = Runtime.createAndStart("arduino","Arduino")
arduino.connect("/dev/tty.usbmodem1431")
sleep(1)
arduino.publishState()
arduino.pinMode(13, Arduino.OUTPUT)
acapelaSpeech = Runtime.createAndStart("speech", "AcapelaSpeech")
voices = acapelaSpeech.getVoices()
for voice in voices:
    acapelaSpeech.setVoice("Ryan") 
python.subscribe("speech", "publishStartSpeaking") 
def onStartSpeaking(text): 
    arduino.digitalWrite(13,1)

python.subscribe("speech", "publishStopSpeaking")
def onStopSpeaking(text): 
    arduino.digitalWrite(13,0)
