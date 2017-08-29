import random

i01 = Runtime.createAndStart("i01", "InMoov")

i01.startMouth()

i01.mouth.setGoogleURI("http://thehackettfamily.org/Voice_api/api2.php?voice=Rhona&txt=")

i01.startEar()

ear = i01.ear

ear.addCommand("stop talking", "python", "stopTalking")

ear.addComfirmations("yes","correct","ya","yeah")
ear.addNegations("no","wrong","nope","nah")

ear.startListening("thank you | left one | left two | left three | left four | left five | left six | left seven | left eight | left nine | right one | right two | right three | right four | right five | right six | right seven | right eight | right nine | help | start listening")

ear.addListener("recognized", "python", "heard")

def heard(data):

    if (data == "left one"):
       i01.mouth.speak("left one")

    if (data == "left two"):
       i01.mouth.speak("left two")

    if (data == "left three"):
       i01.mouth.speak("left three")
       
    if (data == "left four"):
       i01.mouth.speak("left four")

    if (data == "left five"):
       i01.mouth.speak("left five")

    if (data == "left six"):
       i01.mouth.speak("left six")

    if (data == "left seven"):
       i01.mouth.speak("left seven")

    if (data == "left eight"):
       i01.mouth.speak("left eight")

    if (data == "left nine"):
       i01.mouth.speak("left nine")

    if (data == "right one"):
       i01.mouth.speak("right one")

    if (data == "right two"):
       i01.mouth.speak("right two")

    if (data == "right three"):
       i01.mouth.speak("right three")

    if (data == "right four"):
       i01.mouth.speak("right four")

    if (data == "right five"):
       i01.mouth.speak("right five")

    if (data == "right six"):
       i01.mouth.speak("right six")

    if (data == "right seven"):
       m1.move(-0.7)
       m1.sleep(100)
       m1.stop()
       i01.mouth.speak("right seven")

    if (data == "right eight"):
       i01.mouth.speak("right eight")

    if (data == "right nine"):
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

def stopTalking():
   sleep(2)
   ear.pauseListening()
   i01.mouth.speakBlocking("I will stop talking now")
   ear.pauseListening()
   ear.lockOutAllGrammarExcept("start listening")
   ear.resumeListening()
