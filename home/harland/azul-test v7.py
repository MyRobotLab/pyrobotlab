# file : Azul_Test v7.py
# April 23,2016 uses mrl 32 and myrobotlab ver 1280
# only problem is voice commands run twice most of time

import random
import threading
import itertools
webgui = Runtime.start("webgui","WebGui")

#Azul dell laptop mega on left, uno on right, mega on wheel platform
leftPort = "COM11"	
rightPort = "COM10"	

# mobile platform mega board with Fd firmware
serial = Runtime.start("serial","Serial")
serial.connect("COM14",57600, 8, 1, 0)
speed = 5
serdata = ""

i01 = Runtime.createAndStart("i01", "InMoov")

print("head & mouth")
i01.startMouth()
i01.startMouthControl(leftPort)
i01.mouth.setVoice("Will")
mouth = i01.mouth

# checked 10-28-2015 125 is close
i01.head.jaw.map(0,180,60,125)
i01.mouthControl.setmouth(125,60)
mouth.speakBlocking("My name is Azul")
mouth.speakBlocking("#LAUGH02#")

i01.startHead(leftPort, "mega")
# checked head 10-28-2015   new camera 4-10-2016
i01.head.eyeY.map(0,180,0,65)
i01.head.eyeY.setRest(30)
i01.head.eyeX.map(0,180,30,110)  #there is no x servo on azul
i01.head.eyeX.setRest(64)
i01.head.neck.map(0,180,50,170)
i01.head.neck.setRest(120)
i01.head.rothead.map(0,180,20,145)
i01.head.rothead.setRest(90)

print("arms and hands")
i01.startLeftHand(leftPort)
# checked 4-15-2016 Azul new dual stage pulleys, reversed open and closed
i01.leftHand.thumb.map(0,180,160,15)
i01.leftHand.index.map(0,180,165,10)
i01.leftHand.majeure.map(0,180,20,170)
i01.leftHand.ringFinger.map(0,180,170,25)
i01.leftHand.pinky.map(0,180,155,25)
i01.leftHand.wrist.map(0,180,10,150)
i01.leftHand.wrist.setRest(90)

#  checked 6-7-2015
i01.startRightHand(rightPort)
i01.rightHand.thumb.map(0,180,10,110)
i01.rightHand.thumb.setRest(25)
i01.rightHand.index.map(0,180,0,150)
i01.rightHand.majeure.map(0,180,0,140)
i01.rightHand.ringFinger.map(0,180,15,145)
i01.rightHand.pinky.map(0,180,10,135)
i01.rightHand.pinky.setRest(10)
i01.rightHand.wrist.map(0,180,5,90)
i01.rightHand.wrist.setRest(50)

i01.startLeftArm(leftPort)
# checked 4-17-2016
i01.leftArm.bicep.map(0,180,5,90)
i01.leftArm.bicep.setRest(10)
i01.leftArm.rotate.map(0,180,10,130)
i01.leftArm.rotate.setRest(60)
i01.leftArm.shoulder.map(0,180,5,125)
i01.leftArm.shoulder.setRest(30)
i01.leftArm.omoplate.map(0,180,10,35)
i01.leftArm.omoplate.setRest(15)

i01.startRightArm(rightPort)
# checked 6-7-2015
i01.rightArm.bicep.map(0,180,10,95)
i01.rightArm.bicep.setRest(20)
i01.rightArm.rotate.map(0,180,5,145)
i01.rightArm.rotate.setRest(94)
i01.rightArm.shoulder.map(0,180,20,155)
i01.rightArm.shoulder.setRest(35)
i01.rightArm.omoplate.map(0,180,10,50)
i01.rightArm.omoplate.setRest(20)

print("torso")
torso = i01.startTorso(leftPort)
# checked
torso.topStom.map(0,180,65,115)
torso.midStom.map(0,180,20,160)
torso.topStom.setRest(90)
torso.midStom.setRest(90)

print("opencv")
opencv = Runtime.start("opencv","OpenCV")
sleep(3)
opencv.capture()
sleep(5)
opencv.addFilter("Transpose")

i01.startEar()
ear =i01.ear
# harland removed 04-23 ear.addMouth(mouth)

# verbal commands
ear.addCommand("attach everything", "i01", "attach")
ear.addCommand("disconnect everything", "i01", "detach")
ear.addCommand("manual", ear.getName(), "lockOutAllGrammarExcept", "voice control")
ear.addCommand("voice control", ear.getName(), "clearLock")
ear.addCommand("camera on", i01.getName(), "cameraOn")
ear.addCommand("off camera", i01.getName(), "cameraOff")

ear.addCommand("relax", "python", "relax")
ear.addCommand("take a break", "python", "rest")
ear.addCommand("open your hands", "python", "handopen")
ear.addCommand("close your hands", "python", "handclose")
ear.addCommand("open your right hand", "python", "openrighthand")
ear.addCommand("open your left hand", "python", "openlefthand")
ear.addCommand("close your right hand", "python", "closerighthand")
ear.addCommand("close your left hand", "python", "closelefthand")
ear.addCommand("move hips", "python", "fistHips")
ear.addCommand("arms front", "python", "armsFront")
ear.addCommand("come here", "python", "comehere")
ear.addCommand("guess what", "python", "guesswhat")
ear.addCommand("perfect", "python", "perfect")
ear.addCommand("picture on the right side", "python", "picturerightside")
ear.addCommand("picture on the left side", "python", "pictureleftside")
ear.addCommand("look on your right side", "python", "lookrightside")
ear.addCommand("look on your left side", "python", "lookleftside")
ear.addCommand("look back", "python", "lookback")
ear.addCommand("how many fingers do you have", "python", "howmanyfingersdoihave")
ear.addCommand("show your muscles", "python", "muscle")
ear.addCommand("hello", "python", "hello")

# next commands for mobil platform
ear.addCommand("41", "python", "fforward1")
ear.addCommand("42", "python", "fforward2")
ear.addCommand("43", "python", "fforward3")
ear.addCommand("44", "python", "fforward4")
ear.addCommand("45", "python", "fforward5")
ear.addCommand("backup", "python", "backward")
ear.addCommand("left", "python", "turnleft")
ear.addCommand("right", "python", "turnright")
ear.addCommand("stop", "python", "allstop")
ear.addCommand("move forward", "python", "move")
ear.addCommand("up", "python", "speedup") 
ear.addCommand("down", "python", "speedown") 
ear.addCommand("distance", "python", "pings") 
ear.addCommand("range", "python", "analog") 
ear.addCommand("heading", "python", "compass") 

ear.addComfirmations("yes","correct","ya","yeah")
ear.addNegations("no","wrong","nope","nah")
ear.startListening()

mouth.speakBlocking("Azul is ready to rock")
print("ready")

def relax():           
# changed 4-28-2015
# head rotatehead, neck, eyeX, eyeY, jaw
# hand thumb, index,  majeure,  ring,  pinky, wrist
# arm bicep, rotate, rotate shoulder, omoplate
#  i01.mouth.speakBlocking("relaxing")
  i01.setHandSpeed("left", 0.85, 0.85, 0.85, 0.85, 0.85, 0.85)
  i01.setHandSpeed("right", 0.85, 0.85, 0.85, 0.85, 0.85, 0.85)
  i01.setArmSpeed("right", 0.75, 0.85, 0.65, 0.85)
  i01.setArmSpeed("left", 0.95, 0.65, 0.75, 0.75)
  i01.setHeadSpeed(0.85, 0.85)
  i01.setTorsoSpeed(0.75, 0.75, 1.0)
  i01.moveHead(79,100)
  sleep(.5)
  i01.moveArm("left",5,84,28,15)
  sleep(.5)
  i01.moveArm("right",5,82,28,20)
  sleep(.5)
  i01.moveHand("left",92,33,37,71,66,90)
  sleep(.5)
  i01.moveHand("right",81,66,82,60,105,90)
  sleep(.5)
  i01.moveTorso(90,90,90)
  sleep(1)
  
def handopen():
# changed 4-28-2015
# hand thumb, index,  majeure,  ring,  pinky, wrist
  i01.setHandSpeed("left", 0.85, 0.85, 0.85, 0.85, 0.85, 0.85)
  i01.setHandSpeed("right", 0.85, 0.85, 0.85, 0.85, 0.85, 0.85)
  i01.moveHand("left",0,0,0,0,0)
  sleep(.5)
  i01.moveHand("right",0,0,0,0,0)

def handclose():
# changed 4-28-2015
# hand thumb, index,  majeure,  ring,  pinky, wrist
  i01.setHandSpeed("left", 0.85, 0.85, 0.85, 0.85, 0.85, 0.85)
  i01.setHandSpeed("right", 0.85, 0.85, 0.85, 0.85, 0.85, 0.85)
  i01.moveHand("left",180,180,180,180,180)
  sleep(.5)
  i01.moveHand("right",180,180,180,180,180)

def openlefthand():
# changed 4-28-2015
# hand thumb, index,  majeure,  ring,  pinky, wrist
  i01.setHandSpeed("left", 0.95, 0.95, 0.95, 0.95, 0.95, 0.95)
  i01.moveHand("left",0,0,0,0,0)

def openrighthand():
# changed 4-28-2015
# hand thumb, index,  majeure,  ring,  pinky, wrist
  i01.setHandSpeed("right", 0.95, 0.95, 0.95, 0.95, 0.95, 0.95)
  i01.moveHand("right",0,0,0,0,0)

def closelefthand():
# changed 4-28-2015
# hand thumb, index,  majeure,  ring,  pinky, wrist
  i01.setHandSpeed("left", 0.85, 0.85, 0.85, 0.85, 0.85, 0.85)
  i01.moveHand("left",180,180,180,180,180)

def closerighthand():
# changed 4-28-2015
# hand thumb, index,  majeure,  ring,  pinky, wrist
  i01.setHandSpeed("right", 0.85, 0.85, 0.85, 0.85, 0.85, 0.85)
  i01.moveHand("right",180,180,180,180,180)
  
def fistHips():
# changed 4-28-2015
# head rotatehead, neck, eyeX, eyeY, jaw
# hand thumb, index,  majeure,  ring,  pinky, wrist
# arm bicep, rotate, rotate shoulder, omoplate
  mouth.speakBlocking("#LAUGH02#")
  i01.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
  i01.setHeadSpeed(1.0, 1.0)
  i01.setTorsoSpeed(0.80, 0.80, 1.0)
  i01.moveHead(138,80)
  sleep(.5)
  i01.moveArm("left",79,42,23,41)
  sleep(.5)
  i01.moveArm("right",71,40,14,39)
  sleep(.5)
  i01.moveHand("left",180,180,180,180,180,47)
  i01.moveHand("right",99,130,152,154,145,180)
  sleep(.5)
  i01.moveTorso(50,30,90)
  sleep(2)
  i01.moveTorso(130,160,90)
  sleep(2)
  i01.moveTorso(90,90,90)
  sleep(1)

def armsFront():        # changed 11-1-2015
# arm bicep, rotate, rotate shoulder, omoplate
    i01.moveArm("left",90,90,90,20)
    sleep(4)
    i01.moveArm("right",90,90,90,20)
  
def comehere():
# rotatehead, neck, eyeX, eyeY, jaw
# hand right thumb, index, majeure, ring, pinky, wrist
# arm bicep, rotate, rotate shoulder, omoplate
#look around
      i01.setHeadSpeed(0.80, 0.80, 0.90, 0.90, 1.0)
      i01.moveHead(20,66,7,85,72)
      sleep(3)
      i01.moveHead(130,110,175,85,72)
      sleep(3)
#raise arm point finger
      i01.setHandSpeed("left", 0.85, 0.85, 0.85, 0.85, 0.85, 1.0)
      i01.setHandSpeed("right", 1.0, 0.85, 1.0, 1.0, 1.0, 1.0)
      i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
      i01.setArmSpeed("right", 0.90, 1.0, 1.0, 1.0)
      i01.setHeadSpeed(1.0, 0.90)
      i01.setTorsoSpeed(1.0, 1.0, 1.0)
      i01.moveHead(80,86,85,85,72)
      i01.moveArm("left",5,94,30,10)
      i01.moveArm("right",7,78,92,10)
      i01.moveHand("left",180,180,180,180,180,90)
      i01.moveHand("right",180,2,175,160,165,180)
      i01.moveTorso(90,90,90)
      sleep(4)
#move finger
      i01.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
      i01.setHandSpeed("right", 1.0, 0.95, 1.0, 1.0, 1.0, 1.0)
      i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
      i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
      i01.setHeadSpeed(1.0, 1.0)
      i01.setTorsoSpeed(1.0, 1.0, 1.0)
      i01.moveHead(80,86)
      i01.moveArm("left",5,94,30,10)
      i01.moveArm("right",48,78,92,10)
      i01.moveHand("left",180,180,180,180,180,90)
      i01.moveHand("right",180,2,175,160,165,26)
      i01.moveTorso(90,90,90)
      sleep(2)
      i01.setHeadSpeed(0.80, 0.80)
      i01.moveHead(80,80)
      i01.moveHand("right",180,164,175,160,165,26)
      sleep(2)
      i01.moveHead(80,80)
      i01.moveHand("right",180,2,175,160,165,26)
      sleep(2)
      i01.moveHead(118,80)
      i01.moveHand("right",180,164,175,160,165,26)
      sleep(2)
      mouth.speak("come closer")
      i01.moveHead(60,80)
      i01.moveHand("right",180,2,175,160,165,26)
      sleep(2)
      i01.moveHead(118,80)
      i01.moveHand("right",180,164,175,160,165,26)
      sleep(2)
      i01.moveHead(60,80)
      sleep(1)
      relax()

def guesswhat():
    mouth.speak("I'm not really a human man")
    mouth.speak("but I use Old spice body wash and deodorant together")
    mouth.speak("and now I'm really cool")
    sleep(1)

def rest():
# changed 4-28-2015
# head rotatehead, neck, eyeX, eyeY, jaw
# hand thumb, index,  majeure,  ring,  pinky, wrist
# arm bicep, rotate, rotate shoulder, omoplate
#  mouth.speak("resting")
#  i01.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
#  i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
#  i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
#  i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
#  i01.setHeadSpeed(0.9, 0.9)
#  i01.setTorsoSpeed(0.90, 0.90, 1.0)
  i01.moveHead(90,65,82,78,76)
  sleep(1)
  i01.moveArm("left",5,90,30,10)
  sleep(1)
  i01.moveArm("right",5,90,30,20)
  sleep(1)
  i01.moveHand("left",10,10,10,10,10)
  sleep(1)
  i01.moveHand("right",15,15,15,15,15)
  sleep(1)
  i01.moveTorso(90,90,90)
  sleep(1)

def perfect():
# changed 4-28-2015
# head rotatehead, neck, eyeX, eyeY, jaw
# hand thumb, index,  majeure,  ring,  pinky, wrist
# arm bicep, rotate, rotate shoulder, omoplate
  mouth.speakBlocking("azul is perfect")
  i01.setHandSpeed("left", 0.80, 0.80, 1.0, 1.0, 1.0, 1.0)
  i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("left", 0.85, 0.85, 0.85, 0.95)
  i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
  i01.setHeadSpeed(0.65, 0.75)
  i01.moveHead(88,79)
  sleep(.5)
  i01.moveArm("left",89,75,93,11)
  sleep(.5)
  i01.moveArm("right",0,91,28,17)
  sleep(.5)
  i01.moveHand("left",130,160,83,40,0,34)
  sleep(.5)
  i01.moveHand("right",86,51,133,162,153,180)
  sleep(1)

def pictureleftside():
# rotatehead, neck, eyeX, eyeY, jaw
# hand right thumb 110, index 100, majeure 120, ring 115, pinky 115, wrist 90
  i01.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setHandSpeed("right", 0.85, 0.85, 0.85, 0.85, 0.85, 0.85)
  i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("left", 0.75, 0.85, 0.95, 0.85)
  i01.setHeadSpeed(0.65, 0.65)
  i01.moveHead(180,90)
  i01.setTorsoSpeed(0.80, 0.80, 1.0)
  i01.moveTorso(90,120,90)
  sleep(1)
  i01.moveArm("left",90,105,24,75)
  sleep(.5)
  i01.moveArm("right",5,82,28,15)
  sleep(.5)
  i01.moveHand("left",50,86,97,74,106,119)
  i01.moveHand("right",81,65,82,60,105,113)
  sleep(.5)

def picturerightside():
  i01.setHandSpeed("left", 0.85, 0.85, 0.85, 0.85, 0.85, 0.85)
  i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("right", 0.85, 0.85, 0.85, 0.85)
  i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
  i01.setHeadSpeed(0.65, 0.65)
  i01.moveHead(5,40)
  sleep(.5)
  i01.setTorsoSpeed(0.80, 0.80, 1.0)
  i01.moveTorso(90,30,90)
  sleep(1)
  i01.moveArm("left",5,94,28,15)
  sleep(.5)
  i01.moveArm("right",90,115,23,68)
  sleep(.5)
  i01.moveHand("left",42,58,87,55,71,35)
  i01.moveHand("right",10,112,95,91,125,45)

def lookrightside():
  i01.setHeadSpeed(0.70, 0.70)
  i01.setTorsoSpeed(0.75, 0.85, 1.0)
  i01.moveHead(20,40)
  i01.moveTorso(120,30,90)

def lookleftside():
  i01.setHeadSpeed(0.70, 0.70)
  i01.setTorsoSpeed(0.75, 0.85, 1.0)
  i01.moveHead(170,140)
  i01.moveTorso(80,150,90)

def lookback():
  i01.setHeadSpeed(0.90, 0.90)
  i01.setTorsoSpeed(0.85, 0.85, 1.0)
# want to look left and down
  i01.moveHead(160,150)
  sleep(2)
  i01.moveTorso(80,180,90)
  sleep(2)
  mouth.speak("life is good")
  sleep(4)
  i01.moveTorso(90,90,90)
  sleep(1)
  i01.moveHead(110,90)
  
def muscle():
# changed 4-28-2015
# head rotatehead, neck, eyeX, eyeY, jaw
# hand thumb, index,  majeure,  ring,  pinky, wrist
# arm bicep, rotate, rotate shoulder, omoplate
  i01.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("right", 0.75, 0.85, 0.95, 0.85)
  i01.setArmSpeed("left", 0.75, 0.85, 0.95, 0.85)
  i01.setHeadSpeed(0.65, 0.65)
  i01.setTorsoSpeed(0.75, 0.75, 1.0)
  i01.moveHead(90,129)
  i01.moveArm("left",170,150,48,170)
  i01.moveArm("right",71,40,14,43)
  i01.moveHand("left",180,180,180,180,180,83)
  i01.moveHand("right",99,130,152,154,145,21)
  i01.moveTorso(120,130,90)
  sleep(4)
  mouth.speak("Looks good, doesn't it")
  sleep(2)
  i01.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
  i01.setHeadSpeed(0.85, 0.85)
  i01.setTorsoSpeed(0.75, 0.75, 1.0)
  i01.moveHead(90,45)
  i01.moveArm("left",44,46,20,39)
  i01.moveArm("right",170,165,58,160)
  i01.moveHand("left",180,180,180,180,180,83)
  i01.moveHand("right",99,130,152,154,145,21)
  i01.moveTorso(60,75,90)
  sleep(3)
  mouth.speak("not bad either, don't you think")
  sleep(2)
  relax()

def howmanyfingersdoihave():
     i01.moveHead(49,74)
     i01.moveArm("left",75,83,79,24)
     i01.moveArm("right",65,82,71,24)
     i01.moveHand("left",74,140,150,157,168,92)
     i01.moveHand("right",89,80,98,120,114,0)
     sleep(1)
     i01.moveHand("right",0,80,98,120,114,0)
     mouth.speakBlocking("ten")
     sleep(1)
     i01.moveHand("right",0,0,98,120,114,0)
     mouth.speakBlocking("nine")
     sleep(1)
     i01.moveHand("right",0,0,0,120,114,0)
     mouth.speakBlocking("eight")
     sleep(1)
     i01.moveHand("right",0,0,0,0,114,0)
     mouth.speakBlocking("seven")
     sleep(1)
     i01.moveHand("right",0,0,0,0,0,0)
     mouth.speakBlocking("six")
     sleep(1)
     i01.setHeadSpeed(.70,.70)
     i01.moveHead(40,105)
     i01.moveArm("left",75,83,79,24)
     i01.moveArm("right",65,82,71,24)
     i01.moveHand("left",0,0,0,0,0,180)
     i01.moveHand("right",0,0,0,0,0,0)
     sleep(1)
     mouth.speakBlocking("and five makes eleven")
     sleep(1)
     i01.setHeadSpeed(0.7,0.7)
     i01.moveHead(40,50)
     sleep(1)
     i01.setHeadSpeed(0.7,0.7)
     i01.moveHead(49,105)
     sleep(1)
     i01.setHeadSpeed(0.7,0.8)
     i01.moveHead(40,50)
     sleep(1)
     i01.setHeadSpeed(0.7,0.8)
     i01.moveHead(49,105)
     sleep(1)
     i01.setHeadSpeed(0.7,0.7)
     i01.moveHead(90,85)
     sleep(1)
     mouth.speak("eleven")
     i01.moveArm("left",70,75,70,20)
     i01.moveArm("right",60,75,65,20)
     sleep(1)
     mouth.speak("that doesn't seem right")
     sleep(1)
     mouth.speak("I think I better try that again")
     i01.moveHead(40,105)
     i01.moveArm("left",75,83,79,24)
     i01.moveArm("right",65,82,71,24)
     i01.moveHand("left",140,168,168,168,158,90)
     i01.moveHand("right",87,138,109,168,158,25)
     sleep(1)
     i01.moveHand("left",10,140,168,168,158,90)
     mouth.speak("one")
     sleep(1)
     i01.moveHand("left",10,10,168,168,158,90)
     mouth.speak("two")
     sleep(1)
     i01.moveHand("left",10,10,10,168,158,90)
     mouth.speak("three")
     sleep(1)
     i01.moveHand("left",10,10,10,10,158,90)
     mouth.speak("four")
     sleep(1)
     i01.moveHand("left",10,10,10,10,10,90)
     mouth.speak("five")
     sleep(1)
     i01.setHeadSpeed(0.65,0.65)
     i01.moveHead(53,65)
     i01.moveArm("right",48,80,78,11)
     i01.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
     i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
     i01.moveHand("left",10,10,10,10,10,90)
     i01.moveHand("right",10,10,10,10,10,25)
     sleep(1)
     mouth.speak("and five makes ten")
     sleep(1)
     mouth.speak("there that's better")
     i01.moveHead(95,85)
     i01.moveArm("left",75,83,79,24)
     i01.moveArm("right",40,70,70,10)
     sleep(1)
     mouth.speak("azul has ten fingers")
     sleep(1)
     i01.moveHead(90,90)
     i01.setHandSpeed("left", 0.8, 0.8, 0.8, 0.8, 0.8, 0.8)
     i01.setHandSpeed("right", 0.8, 0.8, 0.8, 0.8, 0.8, 0.8)
     i01.moveHand("left",140,140,140,140,140,60)
     i01.moveHand("right",140,140,140,140,140,60)
     sleep(1)
     i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
     i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
     i01.moveArm("left",5,90,30,11)
     i01.moveArm("right",5,90,30,11)
     sleep(1)

def hello():
     i01.setHandSpeed("left", 0.60, 0.60, 1.0, 1.0, 1.0, 1.0)
     i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
     i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
     i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
     i01.setHeadSpeed(0.65, 0.75)
     i01.moveHead(105,78)
     i01.moveArm("left",78,48,37,11)
     i01.moveArm("right",90,144,60,75)
     i01.moveHand("left",112,111,105,102,81,10)
     i01.moveHand("right",0,0,0,50,82,180)
     i01.setHandSpeed("left", 0.60, 0.60, 1.0, 1.0, 1.0, 1.0)
     i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 0.60)
     i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
     i01.setArmSpeed("right", 0.65, 1.0, 1.0, 1.0)
     i01.setHeadSpeed(0.65, 0.75)
     i01.moveHead(83,70)
     mouth.speak("hi, my name is azul")
     i01.moveArm("left",78,48,37,11)
     i01.moveArm("right",57,145,50,68)
     i01.moveHand("left",100,90,85,80,71,15)
     i01.moveHand("right",3,0,31,12,26,45)
     sleep(1)
     i01.moveHead(83,98)
     i01.moveArm("left",78,48,37,11)
     i01.moveArm("right",90,157,47,75)
     i01.moveHand("left",112,111,105,102,81,10)
     i01.moveHand("right",3,0,62,41,117,94)
     sleep(1)
     i01.setHandSpeed("left", 0.85, 0.85, 0.85, 0.85, 0.85, 0.85)
     i01.setHandSpeed("right", 0.85, 0.85, 0.85, 0.85, 0.85, 0.85)
     i01.setArmSpeed("right", 0.75, 0.85, 0.95, 0.85)
     i01.setArmSpeed("left", 0.95, 0.65, 0.75, 0.75)
     i01.setHeadSpeed(0.75, 0.75)
     i01.moveHead(79,100)
     i01.moveArm("left",5,94,28,15)
     i01.moveArm("right",5,82,28,15)
     i01.moveHand("left",42,58,42,55,71,35)
     i01.moveHand("right",81,50,82,60,105,113)
     sleep(1)
     
def fforward1():
     serial.write(b'F10\r')
#     print "forward 10"
     clearbuffer()  

def fforward2():
     serial.write(b'F15\r')
#     print "forward 15"
     clearbuffer()   

def fforward3():
     serial.write(b'F20\r')
#     print "forward 20"
     clearbuffer()   

def fforward4():
     serial.write(b'F25\r')
#     print "forward 25"
     clearbuffer()   

def fforward5():
     serial.write(b'F30\r')
#     print "forward 30"
     clearbuffer()   

def backward():
     serial.write(unicode("B15\r"))
#     print "backward"
     clearbuffer()

def turnright():
     serial.write("R15\r")
#     print "right"
     clearbuffer()

def turnleft():
     serial.write("L15\r")
#     print "left"
     clearbuffer()

def allstop():
     serial.write("S90\r")
     print "stop"
     clearbuffer()

def move():
     serial.write("M20\r")
     print "fwd till obstical"
     clearbuffer()

#would like to clean out serial buffer
def clearbuffer():
  crap = 0
  crap = serial.available()
#  print("cbuf " + str(crap))
  if crap > 0:
    for i in range(1,crap): 
      junk = serial.read()		# out with the crap
#      print("junk=" + str(junk))
    
def speedup():
  global speed
  speed = speed + 5
  print ("speed=" + str(speed))
  
def speedown():
  global speed
  speed = speed - 5
  print ("speed=" + str(speed))

def pings():
  global serdata
  clearbuffer()
  sleep(1)
  serial.write("P\r")
  getmessage()
  print("ping sensors = " + str(serdata))
  clearbuffer()

def analog():
  global serdata
  clearbuffer()
  sleep(1)
  serial.write("A\r")
  getmessage()
  print("3 ir sensors & batt volts=" + str(serdata))
  print str(serdata).find('A3=')
  start = str(serdata).find('A3=')
  print( start )
  print serdata[start:6]
  clearbuffer()

def compass():
  global serdata
  clearbuffer()
  sleep(1)
  serial.write("C\r")
  getmessage()
# message looks like 215.64
#  print("heading=" + (str(serdata)))
  print str(serdata)[:4]	# only need whole number
  clearbuffer()
  
def getmessage():
  global serdata
  serdata = ""
  crap = serial.available()
  if crap > 0:
    for i in range(1,crap): 
      code = serial.read()
#      print("junk=" + chr(code) + " " + str(code))
      if(code == 0x0D):
#         print("found end")
         break
      serdata += chr(code)
#    print("raw data=" + (str(serdata)))
