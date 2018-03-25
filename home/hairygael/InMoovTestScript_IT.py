#file : InMoov.minimalFingerStarter.py
# MRL version above 1.0.2620
# this script is provided as a basic guide
# most parts can be run by uncommenting them
# InMoov now can be started in modular pieces through the skeleton.config
# although this script is very short you can still
# do voice control of a FingerStarter or hand
# It uses WebkitSpeechRecognition, so you need to use Chrome as your default browser for this script to work

# Change to the port that you use
rightPort = "COM9"
##############
# start optional virtual arduino service, used for internal test and virtual inmoov
# virtual=True
if ('virtual' in globals() and virtual):
    # virtualArduinoLeft = Runtime.start("virtualArduinoLeft", "VirtualArduino")
    # virtualArduinoLeft.connect(leftPort)
    virtualArduinoRight = Runtime.start("virtualArduinoRight", "VirtualArduino")
    virtualArduinoRight.connect(rightPort)
# end used for internal test
##############
#to tweak the default voice
Voice="Italian_Francesco" 
#Voice="cmu-slt-hsmm" #Default female for MarySpeech
mouth = Runtime.createAndStart("i01.mouth", "NaturalReaderSpeech")
#mouth.installComponentsAcceptLicense(Voice)
mouth.setVoice(Voice)
##############
# starting InMoov service
i01 = Runtime.create("i01", "InMoov")
#Force Arduino to connect (fix Todo)
right = Runtime.createAndStart("i01.right", "Arduino")
right.connect(rightPort)
##############
# Starting parts
i01.startEar()
ear = i01.ear
ear.setLanguage("it-IT")
# Start the webgui service without starting the browser
webgui = Runtime.create("WebGui","WebGui")
webgui.autoStartBrowser(False)
webgui.startService()
# Then start the browsers and show the WebkitSpeechRecognition service named i01.ear
webgui.startBrowser("http://localhost:8888/#/service/i01.ear")
# As an alternative you can use the line below to show all services in the browser. In that case you should comment out all lines above that starts with webgui. 
# webgui = Runtime.createAndStart("webgui","WebGui")
##############
i01.startMouth()
##############
rightHand = Runtime.create("i01.rightHand","InMoovHand")
# Tweaking defaults settings of right hand

# Mapping by setting your servo limits
rightHand.index.map(0,180,42,160)
# Rest position
rightHand.index.setRest(0)
##############
i01 = Runtime.start("i01","InMoov")
##############
i01.startRightHand(rightPort)
i01.rightHand.setAutoDisable(True)
##############
# Verbal commands
#always listen
ear.setAutoListen(True)

ear.addCommand("gigi", "python", "saygigi")
ear.addCommand("silenzio", "python", "stopMp3")
ear.addCommand("pollo", "python", "pollo")


# Confirmations and Negations are not supported yet in WebkitSpeechRecognition
# So commands will execute immediatley
# ear.addComfirmations("si")
# ear.addNegations("no")

ear.startListening()

def saygigi():
    i01.mouth.speak(u"il mio nome è Gigi")

def stopMp3():
    i01.mouth.speak(u"stop")

def pollo():
    print(u"pollo de roma")
