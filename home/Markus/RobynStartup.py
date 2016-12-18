# File : Robyn Inmoov uppstart

import random
from org.myrobotlab.framework import MRLListener

leftPort = "COM8"
rightPort = "COM6"

i01 = Runtime.createAndStart("i01", "InMoov")

i01.mouth = Runtime.createAndStart("i01.mouth","NaturalReaderSpeech")

i01.startAll(leftPort, rightPort)

torso = i01.startTorso("COM8")
i01.torso.topStom.detach("i01.left");
i01.torso.topStom.attach("i01.left", 49)  # topStom

left = Runtime.getService("i01.left")
right = Runtime.getService("i01.right")

left.pinMode(42,"OUTPUT")
left.pinMode(43,"OUTPUT")
left.pinMode(44,"OUTPUT")
left.pinMode(45,"OUTPUT")

right.setBoard("mega2560") # atmega168 | mega2560 | etc

thumbgripp = Runtime.create("thumbgripp","Servo")
thumbfine = Runtime.create("thumbfine","Servo")
indexfine = Runtime.create("indexfine","Servo")
majeurefine = Runtime.create("majeurefine","Servo")
#lefteye = Runtime.create("lefteye","Servo")

thumbgripp.startService()
thumbfine.startService()
indexfine.startService()
majeurefine.startService()
#lefteye.startService()

thumbgripp.attach("i01.left", 30)  # thumbgripp
thumbfine.attach("i01.left", 31)  # thumbfine
indexfine.attach("i01.left", 32)  # indexfine
majeurefine.attach("i01.left", 33)  # majeurefine
#lefteye.attach("i01.left", 23)

thumbfine.moveTo(0)
indexfine.moveTo(0)
majeurefine.moveTo(0)


i01.mouth.speak("okay you can do a system check now")
sleep(2)
#############################################################################################


i01.mouth.setVoice("Laura")

######################################################################

def heard(data):
  print "Speech Recognition Data:", data
 
lloyd = Runtime.createAndStart("lloyd", "ProgramAB")
lloyd.startSession("markus", "Robyn")
webgui = Runtime.create("WebGui","WebGui")
webgui.autoStartBrowser(False)
webgui.startService()
wksr = Runtime.createAndStart("webkitspeechrecognition", "WebkitSpeechRecognition")
htmlfilter = Runtime.createAndStart("htmlfilter", "HtmlFilter")
i01.mouth.speak("Testing to speak")
wksr.setLanguage("sv")
wksr.addTextListener(lloyd)
lloyd.addTextListener(htmlfilter)
htmlfilter.addTextListener(i01.mouth)
webgui.startBrowser("http://localhost:8888/#/service/webkitspeechrecognition")

def askPgmAB(text):
#	i01.mouth.speakBlocking(text)
	lloyd.onText(text)

i01.mouth.speak("okay i am ready for conversation")

######################################################################
# Markus Mod
  
i01.leftArm.omoplate.map(10,80,65,15)
i01.rightArm.omoplate.map(10,80,80,15)
i01.leftArm.shoulder.map(0,180,170,15)
i01.rightArm.shoulder.map(0,180,190,50)
i01.leftArm.rotate.map(40,180,155,20)
i01.rightArm.rotate.map(40,180,155,20)
i01.leftArm.bicep.map(5,90,90,20)
i01.rightArm.bicep.map(5,90,90,20)
i01.torso.topStom.map(60,120,83,118)
i01.leftHand.thumb.map(0,180,20,160)
i01.leftHand.index.map(0,180,30,160)
i01.leftHand.majeure.map(0,180,0,170)
i01.leftHand.ringFinger.map(0,180,0,120)
i01.leftHand.pinky.map(0,180,40,180)

i01.head.rothead.setInverted(True)
i01.head.neck.setInverted(True)
i01.head.eyeX.map(60,100,55,100)
i01.head.eyeY.setInverted(True)
i01.head.jaw.map(0,180,0,160)

i01.rightHand.thumb.map(0,180,160,20)
i01.rightHand.index.map(0,180,160,20)
i01.rightHand.majeure.map(0,180,180,20)
i01.rightHand.ringFinger.map(0,180,0,180)
i01.rightHand.pinky.map(0,180,0,140)

thumbfine.map(0,180,138,0)
indexfine.map(0,180,138,0)
majeurefine.map(0,180,138,0)

############################################################
#to tweak the default PID values

i01.eyesTracking.pid.setPID("eyeX",20.0,5.0,0.1)
i01.eyesTracking.pid.setPID("eyeY",20.0,5.0,0.1)
i01.headTracking.pid.setPID("rothead",12.0,5.0,0.1)
i01.headTracking.pid.setPID("neck",12.0,5.0,0.1)

############################################################

voice = 0

trackloopControl = 0

XboxZ = 122
XboxRY = 122
XboxRX = 122

dance1 = 1
dance2 = 1

arms = 0
leftarm = 0
rightarm = 0

arms3 = 0
leftarm3 = 0
rightarm3 = 0

mem = 1

test = 90

picture = 1

mic = 1

blind = 1

drive = 0

openclosehands = 3
opencloselefthand = 0
opencloserighthand = 0

##################################################################
# Hastighet vid start

i01.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
i01.setHeadSpeed(0.98, 0.98)
i01.head.jaw.setSpeed(1)
i01.setTorsoSpeed(1.0, 1.0, 1.0)
i01.moveArm("left",5,90,30,10)
i01.moveArm("right",5,90,30,15)
i01.moveTorso(90,90,90)
"""
thumbfine.moveTo(0)
indexfine.moveTo(0)
majeurefine.moveTo(0)
"""
i01.mouth.speak("startup script is finished")

##########################################################################################

def Changelanguage():    
    if voice == 0:
        ElinSv()
    elif voice == 1:
        LauraEn()

def ElinSv(): 
    global voice
    voice = 1
    i01.mouth.setVoice("Elin")  
    i01.mouth.speak(u"Nu använder jag en svensk röst")  

def LauraEn():                  
    global voice
    voice = 0
    i01.mouth.setVoice("Laura")
    i01.mouth.speak("Now I am using Lauras Voice to speak English") 
        
######################################################################################################################################################

def red():
    left.digitalWrite(42, 1) # ON
    left.digitalWrite(43, 1) # ON
    left.digitalWrite(44, 1) # ON
    left.digitalWrite(45, 0) # OFF


def green():
    left.digitalWrite(42, 1) # ON
    left.digitalWrite(43, 0) # OFF
    left.digitalWrite(44, 1) # ON
    left.digitalWrite(45, 1) # ON

def blue():
    left.digitalWrite(42, 1) # ON
    left.digitalWrite(43, 1) # ON
    left.digitalWrite(44, 0) # OFF
    left.digitalWrite(45, 1) # ON

def ledoff():
    left.digitalWrite(42, 0) # OFF
    left.digitalWrite(43, 0) # OFF
    left.digitalWrite(44, 0) # OFF
    left.digitalWrite(45, 0) # OFF
#########################################################################################

#while True:
#    if trackloopControl == 1:
#        if i01.head.rothead.getPos() >= 100:
#            serial.write("127,127,60\n") 
#        elif i01.head.rothead.getPos() <= 60:
#            serial.write("127,127,200\n")            
#        else : 
#            serial.write("127,127,127\n") 
#            print ("off")
#        print (i01.head.rothead.getPos())
#        sleep(1)  
