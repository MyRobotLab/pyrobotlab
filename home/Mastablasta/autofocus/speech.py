import random
rightPort = "COM6"

arduino = Runtime.createAndStart("arduino", "Arduino")
arduino.connect(rightPort) 
m1 = Runtime.createAndStart("m1","Motor")
arduino.motorAttach("m1", "TYPE_LPWM_RPWM", 5, 6)
m1.stop()
m1.move(-0.01)

keyboard = Runtime.start("keyboard", "Keyboard")
keyboard.addCommand("Links", "python", "Links", "Links")               ########### I have a German keyboard !!! ###########
keyboard.addCommand("Rechts", "python", "Rechts", "Rechts")
keyboard.addCommand("Oben", "python", "Oben", "Oben")
keyboard.addCommand("Unten", "python", "Unten", "Unten")

ms = 1

i01 = Runtime.createAndStart("i01", "InMoov")

i01.startMouth()

i01.mouth.setGoogleURI("http://thehackettfamily.org/Voice_api/api2.php?voice=Rhona&txt=")

i01.startEar()

ear = i01.ear

sleep(2)
i01.mouth.speak("my name is venus")
sleep(2)
i01.mouth.speak("I am your personal telescope focus assistant")
sleep(2)
i01.mouth.speak("just say help and I will guide you through my menus")

ear.addCommand("stop talking", "python", "stopTalking")

ear.addComfirmations("yes","correct","ya","yeah")
ear.addNegations("no","wrong","nope","nah")

ear.startListening("thank you | left one | left two | left three | left four | left five | left six | left seven | left eight | left nine | right one | right two | right three | right four | right five | right six | right seven | right eight | right nine | help | start listening")

ear.addListener("recognized", "python", "heard")

def heard(data):

    if (data == "left one"):
       m1.move(0.1)
       m1.sleep(100)
       m1.stop()
       i01.mouth.speak("left one")

    if (data == "left two"):
       m1.move(0.2)
       m1.sleep(100)
       m1.stop()
       i01.mouth.speak("left two")

    if (data == "left three"):
       m1.move(0.3)
       m1.sleep(100)
       m1.stop()
       i01.mouth.speak("left three")
       
    if (data == "left four"):
       m1.move(0.4)
       m1.sleep(100)
       m1.stop()
       i01.mouth.speak("left four")

    if (data == "left five"):
       m1.move(0.5)
       m1.sleep(100)
       m1.stop()
       i01.mouth.speak("left five")

    if (data == "left six"):
       m1.move(0.6)
       m1.sleep(100)
       m1.stop()
       i01.mouth.speak("left six")

    if (data == "left seven"):
       m1.move(0.7)
       m1.sleep(100)
       m1.stop()
       i01.mouth.speak("left seven")

    if (data == "left eight"):
       m1.move(0.8)
       m1.sleep(100)
       m1.stop()
       i01.mouth.speak("left eight")

    if (data == "left nine"):
       m1.move(0.9)
       m1.sleep(100)
       m1.stop()
       i01.mouth.speak("left nine")

    if (data == "right one"):
       m1.move(-0.1)
       m1.sleep(100)
       m1.stop()
       i01.mouth.speak("right one")

    if (data == "right two"):
       m1.move(-0.2)
       m1.sleep(100)
       m1.stop()
       i01.mouth.speak("right two")

    if (data == "right three"):
       m1.move(-0.3)
       m1.sleep(100)
       m1.stop()
       i01.mouth.speak("right three")

    if (data == "right four"):
       m1.move(-0.4)
       m1.sleep(100)
       m1.stop()
       i01.mouth.speak("right four")

    if (data == "right five"):
       m1.move(-0.5)
       m1.sleep(100)
       m1.stop()
       i01.mouth.speak("right five")

    if (data == "right six"):
       m1.move(-0.6)
       m1.sleep(100)
       m1.stop()
       i01.mouth.speak("right six")

    if (data == "right seven"):
       m1.move(-0.7)
       m1.sleep(100)
       m1.stop()
       i01.mouth.speak("right seven")

    if (data == "right eight"):
       m1.move(-0.8)
       m1.sleep(100)
       m1.stop()
       i01.mouth.speak("right eight")

    if (data == "right nine"):
       m1.move(-0.9)
       m1.sleep(100)
       m1.stop()
       i01.mouth.speak("right nine")

    if (data == "thank you"):
       i01.mouth.speak("it is a pleasure to be an assistant")

    if (data == "help"):
       i01.mouth.speak("the numbers will set the motor speed")
       sleep(1)
       i01.mouth.speak("one means slow and nine means fast")
       sleep(2)
       i01.mouth.speak("please use the following commands")
       sleep(1)
       i01.mouth.speak("for example")
       sleep(2)
       i01.mouth.speak("left one")
       sleep(1)
       i01.mouth.speak("or")
       sleep(1)
       i01.mouth.speak("right two")
       sleep(1)
       i01.mouth.speak("or")
       sleep(1)
       i01.mouth.speak("left eight")

    if (data == "start listening"):
        ear.pauseListening()
        ear.resumeListening()
        ear.clearLock()
        x = (random.randint(1, 2))
        if x == 1:
           i01.mouth.speakBlocking("I am listening again")
        if x == 2:
           i01.mouth.speakBlocking("I am ready to assist")

def Links(cmd):
    global keyboardInput
    keyboardInput = "Links"
    print "Focus left"
    i01.mouth.audioFile.playFile("F:/mrlneu/scripts/sounds/k1.mp3", False)
    if ms == 1:
       m1.move(0.1)
       m1.sleep(100)
       m1.stop()
    if ms == 2:
       m1.move(0.2)
       m1.sleep(100)
       m1.stop()
    if ms == 3:
       m1.move(0.3)
       m1.sleep(100)
       m1.stop()
    if ms == 4:
       m1.move(0.4)
       m1.sleep(100)
       m1.stop()
    if ms == 5:
       m1.move(0.5)
       m1.sleep(100)
       m1.stop()
    if ms == 6:
       m1.move(0.6)
       m1.sleep(100)
       m1.stop()
    if ms == 7:
       m1.move(0.7)
       m1.sleep(100)
       m1.stop()
    if ms == 8:
       m1.move(0.8)
       m1.sleep(100)
       m1.stop()
    if ms == 9:
       m1.move(0.9)
       m1.sleep(100)
       m1.stop()
    if ms >= 9:
       m1.move(0.9)
       m1.sleep(100)
       m1.stop()

def Rechts(cmd):
    global keyboardInput
    keyboardInput = "Rechts"
    if ms == 1:
       m1.move(-0.1)
       m1.sleep(100)
       m1.stop()
    if ms == 2:
       m1.move(-0.2)
       m1.sleep(100)
       m1.stop()
    if ms == 3:
       m1.move(-0.3)
       m1.sleep(100)
       m1.stop()
    if ms == 4:
       m1.move(-0.4)
       m1.sleep(100)
       m1.stop()
    if ms == 5:
       m1.move(-0.5)
       m1.sleep(100)
       m1.stop()
    if ms == 6:
       m1.move(-0.6)
       m1.sleep(100)
       m1.stop()
    if ms == 7:
       m1.move(-0.7)
       m1.sleep(100)
       m1.stop()
    if ms == 8:
       m1.move(-0.8)
       m1.sleep(100)
       m1.stop()
    if ms == 9:
       m1.move(-0.9)
       m1.sleep(100)
       m1.stop()
    if ms >= 9:
       m1.move(-0.9)
       m1.sleep(100)
       m1.stop()

def Oben(cmd):
    global keyboardInput
    keyboardInput = "Oben"
    global ms
    ms += 1
    if ms == 1:
       print "Speed set to 1"
       i01.mouth.audioFile.playFile("F:/mrlneu/scripts/sounds/1.mp3", False)
    if ms == 2:
       print "Speed set to 2"
       i01.mouth.audioFile.playFile("F:/mrlneu/scripts/sounds/2.mp3", False)
    if ms == 3:
       print "Speed set to 3"
       i01.mouth.audioFile.playFile("F:/mrlneu/scripts/sounds/3.mp3", False)
    if ms == 4:
       print "Speed set to 4"
       i01.mouth.audioFile.playFile("F:/mrlneu/scripts/sounds/4.mp3", False)
    if ms == 5:
       print "Speed set to 5"
       i01.mouth.audioFile.playFile("F:/mrlneu/scripts/sounds/5.mp3", False)
    if ms == 6:
       print "Speed set to 6"
       i01.mouth.audioFile.playFile("F:/mrlneu/scripts/sounds/6.mp3", False)
    if ms == 7:
       print "Speed set to 7"
       i01.mouth.audioFile.playFile("F:/mrlneu/scripts/sounds/7.mp3", False)
    if ms == 8:
       print "Speed set to 8"
       i01.mouth.audioFile.playFile("F:/mrlneu/scripts/sounds/8.mp3", False)
    if ms == 9:
       print "Speed set to 9"
       i01.mouth.audioFile.playFile("F:/mrlneu/scripts/sounds/9.mp3", False)
    if ms <= 0:
       print "Limit slow"
       i01.mouth.speak("limit reached")
       ms = 1
    if ms >= 10:
       print "Limit fast"
       i01.mouth.speak("limit reached")
       ms = 9

def Unten(cmd):
    global keyboardInput
    keyboardInput = "Unten"
    global ms
    ms -= 1
    if ms == 1:
       print "Speed set to 1"
       i01.mouth.audioFile.playFile("F:/mrlneu/scripts/sounds/1.mp3", False)
    if ms == 2:
       print "Speed set to 2"
       i01.mouth.audioFile.playFile("F:/mrlneu/scripts/sounds/2.mp3", False)
    if ms == 3:
       print "Speed set to 3"
       i01.mouth.audioFile.playFile("F:/mrlneu/scripts/sounds/3.mp3", False)
    if ms == 4:
       print "Speed set to 4"
       i01.mouth.audioFile.playFile("F:/mrlneu/scripts/sounds/4.mp3", False)
    if ms == 5:
       print "Speed set to 5"
       i01.mouth.audioFile.playFile("F:/mrlneu/scripts/sounds/5.mp3", False)
    if ms == 6:
       print "Speed set to 6"
       i01.mouth.audioFile.playFile("F:/mrlneu/scripts/sounds/6.mp3", False)
    if ms == 7:
       print "Speed set to 7"
       i01.mouth.audioFile.playFile("F:/mrlneu/scripts/sounds/7.mp3", False)
    if ms == 8:
       print "Speed set to 8"
       i01.mouth.audioFile.playFile("F:/mrlneu/scripts/sounds/8.mp3", False)
    if ms == 9:
       print "Speed set to 9"
       i01.mouth.audioFile.playFile("F:/mrlneu/scripts/sounds/9.mp3", False)
    if ms <= 0:
       print "Limit slow"
       i01.mouth.speak("limit reached")
       ms = 1
    if ms >= 10:
       print "Limit fast"
       i01.mouth.speak("limit reached")
       ms = 9

def stopTalking():
   sleep(2)
   ear.pauseListening()
   i01.mouth.speakBlocking("I will stop talking now")
   ear.pauseListening()
   ear.lockOutAllGrammarExcept("start listening")
   ear.resumeListening()
