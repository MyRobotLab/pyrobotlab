#########################################
# WebkitSpeechRecognition.py
# more info @: http://myrobotlab.org/service/WebkitSpeechRecognition
#########################################

# start the service
webkitspeechrecognition = Runtime.start("webkitspeechrecognition","WebkitSpeechRecognition")
# auto rearm microphone
# webkitspeechrecognition.setAutoListen(True)
# speedup recognition
# webkitspeechrecognition.setContinuous(False)
=======
webgui = Runtime.start("webgui","WebGui")
webkitspeechrecognition = Runtime.start("webkitspeechrecognition","WebkitSpeechRecognition")
arduino = Runtime.start("arduino","Arduino")
arduino.connect("COM3")

def lightOn():
  arduino.digitalWrite(13,1)

def lightOff():
  arduino.digitalWrite(13,0)

def onText(data):
     print data
     if (data == "light on"):
         lightOn()
     elif (data == "light off"):
         lightOff()

webkitspeechrecognition.addListener("publishText","python","onText")
