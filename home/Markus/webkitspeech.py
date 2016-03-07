
# i used this from Mats

def heard(data):
  print "Speech Recognition Data:", data
 
lloyd = Runtime.createAndStart("lloyd", "ProgramAB")
lloyd.startSession("kevin", "alice2")
webgui = Runtime.create("WebGui","WebGui")
webgui.autoStartBrowser(False)
webgui.startService()
wksr = Runtime.createAndStart("webkitspeechrecognition", "WebkitSpeechRecognition")
htmlfilter = Runtime.createAndStart("htmlfilter", "HtmlFilter")
i01.mouth.speak("Testing to speak")
wksr.addTextListener(lloyd)
lloyd.addTextListener(htmlfilter)
htmlfilter.addTextListener(i01.mouth)

i01.mouth.speak("okay i am ready for conversation")

# and i used this from Alessandro

wksr.addListener("publishText","python","onText")

def onText(data):
     print data
     if (data == " let me take a picture of you"):
         pose()
     elif (data == "drive the car"):
         drivecar()
