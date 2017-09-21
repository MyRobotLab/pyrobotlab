#########################################
# WebkitSpeechRecognition.py
# more info @: http://myrobotlab.org/service/WebkitSpeechRecognition
# you need chrome browser as default
#########################################

# Start the webgui service without starting the browser
webgui = Runtime.create("WebGui","WebGui")
webgui.autoStartBrowser(False)
webgui.startService()

# Then start the browsers and show the WebkitSpeechRecognition service named webkitspeechrecognition
webgui.startBrowser("http://localhost:8888/#/service/webkitspeechrecognition")
webkitspeechrecognition = Runtime.start("webkitspeechrecognition","WebkitSpeechRecognition")
webkitspeechrecognition.setLanguage("en")
# start mouth
marySpeech = Runtime.start("marySpeech", "MarySpeech")

# auto rearm microphone
webkitspeechrecognition.setAutoListen(False)

# speedup recognition if False
webkitspeechrecognition.setContinuous(False)

def lightOn():
  marySpeech.speakBlocking("light is on")

def lightOff():
  marySpeech.speakBlocking("light is off")

def onText(data):
     print data
     if (data == "light on"):
         lightOn()
     elif (data == "light off"):
         lightOff()

webkitspeechrecognition.addListener("publishText","python","onText")