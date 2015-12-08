python = Runtime.start("python","Python")
webkitspeechrecognition = Runtime.start("webkitspeechrecognition","WebkitSpeechRecognition")
arduino = Runtime.start("arduino","Arduino")
arduino.connect("COM3")


def onText(data):
     print data
     if (data = "accendi luce"):
         arduino.digitalWrite(13,1)
     elif (data = "spegni luce"):
         arduino.digitalWrite(13,0)
    
webkitspeechrecognition.addListener("publishText","python","onText")
