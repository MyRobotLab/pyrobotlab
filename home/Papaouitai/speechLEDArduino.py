from java.lang import String
webgui = Runtime.createAndStart("webgui","WebGui")
arduino = Runtime.createAndStart("arduino","Arduino")
arduino.connect("/dev/tty.usbmodem1431")
sleep(1)
arduino.publishState()
arduino.pinMode(13, Arduino.OUTPUT)
acapelaSpeech = Runtime.createAndStart("speech", "AcapelaSpeech")
voices = acapelaSpeech.getVoices()
acapelaSpeech.setVoice("Ryan")
python.subscribe("speech", "publishStartSpeaking") 
def onStartSpeaking(text):
    print "Start Speaking"
    arduino.digitalWrite(13,1)

python.subscribe("speech", "publishEndSpeaking")
def onEndSpeaking(text): 
    print "Stop speaking"
    arduino.digitalWrite(13,0)
