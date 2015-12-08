python = Runtime.start("python","Python")
speech = Runtime.start("speech","GoogleSpeech")
webkitspeechrecognition = Runtime.start("webkitspeechrecognition","WebkitSpeechRecognition")
arduino = Runtime.start("arduino","Arduino")
arduino.connect("COM3")

speech.setGoogleURI("http://thehackettfamily.org/Voice_api/api2.php?voice=Vittorio&txt=")


def onText(data):
     print data
     if (data == "accendi luce"):
         arduino.digitalWrite(13,1)
     elif (data == "spegni luce"):
         arduino.digitalWrite(13,0)
    
webkitspeechrecognition.addListener("publishText","python","onText")

speech.speak("ciao italia")
