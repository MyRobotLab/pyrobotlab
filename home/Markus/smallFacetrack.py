# File : Robyn Inmoov

import random

keyboard = Runtime.createAndStart("keyboard", "Keyboard")
keyboard.addListener("keyCommand", python.getName(), "input")

leftPort = "COM3"
rightPort = "COM6"

i01 = Runtime.createAndStart("i01", "InMoov")

i01.startAll(leftPort, rightPort)

torso = i01.startTorso("COM3")

left = Runtime.getService("i01.left")
right = Runtime.getService("i01.right")

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
sleep(3)
#############################################################################################


i01.mouth.setVoice("Laura")

######################################################################

def heard(data):
  print "Speech Recognition Data:", data
 
lloyd = Runtime.createAndStart("lloyd", "ProgramAB")
lloyd.startSession("markus", "alice2")
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
i01.head.rothead.map(30,150,150,30)
i01.torso.topStom.map(60,120,83,118)
i01.head.eyeX.setMinMax(50,100)
i01.head.eyeX.map(60,100,55,100)
#lefteye.setMinMax(40,90)
#lefteye.map(60,100,40,90)
i01.head.eyeY.map(50,100,95,60)
i01.head.neck.map(20,160,160,20)
i01.leftHand.thumb.map(0,180,20,160)
i01.leftHand.index.map(0,180,30,160)
i01.leftHand.majeure.map(0,180,0,170)
i01.leftHand.ringFinger.map(0,180,0,120)
i01.leftHand.pinky.map(0,180,40,180)

i01.rightHand.majeure.map(0,180,20,180)

thumbfine.map(0,180,138,0)
indexfine.map(0,180,138,0)
majeurefine.map(0,180,138,0)

############################################################
i01.startEyesTracking(leftPort)
i01.startHeadTracking(leftPort)
##############
#to tweak the default PID values

i01.eyesTracking.pid.setPID("eyeX",20.0,5.0,0.1)
i01.eyesTracking.pid.setPID("eyeY",20.0,5.0,0.1)
i01.headTracking.pid.setPID("rothead",12.0,5.0,0.1)
i01.headTracking.pid.setPID("neck",12.0,5.0,0.1)

############################################################

blind = 1

############################################################
# Hastighet vid start

i01.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
i01.setHeadSpeed(0.9, 0.9)
i01.setTorsoSpeed(1.0, 1.0, 1.0)
i01.moveArm("left",5,90,30,10)
i01.moveArm("right",5,90,30,15)
i01.moveTorso(90,90,90)
thumbfine.moveTo(0)
indexfine.moveTo(0)
majeurefine.moveTo(0)

i01.mouth.speak("working on full speed")

##########################################################################################

wksr.addListener("publishText","python","onText")

def onText(data):
     print "User.  " + data
     if (data == "just use your head") or (data == " just use your head"):
         i01.detach()
         i01.head.attach()
         
##########################################################################################

def input(cmd):

    if (cmd == "B"):
        facetrack()
       
############################################################

def facetrack():
    if blind == 1:
        trackHumans()
        global blind
        blind = 0  
    elif blind == 0:
        stopTracking()
        global blind
        blind = 1

def trackHumans():
     i01.mouth.speak("facetrack on")
     i01.headTracking.faceDetect()
#     i01.eyesTracking.faceDetect()

def stopTracking():
     i01.mouth.speak("facetrack off")
     i01.headTracking.stopTracking()
#     i01.eyesTracking.stopTracking()

    
