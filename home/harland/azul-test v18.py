# file : Azul_Test v17.py
# May 15,2016 uses mrl 32 and myrobotlab ver 13?? problem with serial interface
# dell laptop runing windows 7
# mrl 1300

import random
import threading
import itertools

#Azul dell laptop mega on left, uno on right, 2nd mega on wheel platform
leftPort = "COM11"	
rightPort = "COM10"	
# mobile platform mega board with Fd firmware
serial = Runtime.start('serial','Serial')
# serial.connect("COM8",57600, 8, 1, 0)	  # testing on desktop
serial.connect("COM14",57600, 8, 1, 0)    # Azul laptop

# tried next 2 lines from GroG but could not get working
#serial.addByteListener('python')
#serial.addListener("publishRX", "python", "onByte")

# next 2 lines from robyn-inmoov script
keyboard = Runtime.createAndStart("keyboard", "Keyboard")
keyboard.addListener("keyCommand", python.getName(), "input")

serdata = ''
method = ''
speed = 5
helvar = 1
offsetR = 0
offsetL = 0

webgui = Runtime.start("webgui","WebGui")
i01 = Runtime.createAndStart("i01", "InMoov")

print("head & mouth")
i01.startMouth()
i01.startMouthControl(leftPort)
# i01.mouth.setVoice("Josh")
# i01.mouth.setVoice("Rachel")
i01.mouth.setVoice("Will")
# i01.mouth.setVoice("Tracy")
mouth = i01.mouth

# checked 5-9-2016  110 is close
i01.head.jaw.map(0,180,50,110)
i01.mouthControl.setmouth(110,50)
mouth.speakBlocking("My name is Azul")
mouth.speakBlocking("#LAUGH02#")

i01.startHead(leftPort)
# checked head 5-9-2016 
i01.head.eyeY.map(0,180,10,65)    # up is 10 down in 65
i01.head.eyeY.setRest(30)
i01.head.eyeX.map(0,180,30,110)	  # no motor on x
i01.head.eyeX.setRest(64)
i01.head.neck.map(0,180,67,175)
i01.head.neck.setRest(144)
i01.head.rothead.map(0,180,0,170)
i01.head.rothead.setRest(95)

print("arms and hands")
i01.startLeftHand(leftPort)
# checked 5-15-2016 Azul new dual stage pulleys, reversed open and closed
i01.leftHand.thumb.map(0,180,110,10)
i01.leftHand.thumb.setRest(30)
i01.leftHand.index.map(0,180,150,25)
i01.leftHand.index.setRest(40)
i01.leftHand.majeure.map(0,180,25,170)
i01.leftHand.majeure.setRest(30)
i01.leftHand.ringFinger.map(0,180,145,20)
i01.leftHand.ringFinger.setRest(25)
i01.leftHand.pinky.map(0,180,120,0)
i01.leftHand.pinky.setRest(35)
i01.leftHand.wrist.map(0,180,25,125)
i01.leftHand.wrist.setRest(90)

#  checked 5-9-2016
i01.startLeftArm(leftPort)
i01.leftArm.bicep.map(0,180,5,95)
i01.leftArm.bicep.setRest(25)
i01.leftArm.rotate.map(0,180,10,130)
i01.leftArm.rotate.setRest(44)
i01.leftArm.shoulder.map(0,180,5,135)
i01.leftArm.shoulder.setRest(30)
i01.leftArm.omoplate.map(0,180,10,35)
i01.leftArm.omoplate.setRest(15)

#  checked 5-9-2016
i01.startRightHand(rightPort)
i01.rightHand.thumb.map(0,180,25,140)
i01.rightHand.thumb.setRest(25)
i01.rightHand.index.map(0,180,10,145)
i01.rightHand.index.setRest(35)
i01.rightHand.majeure.map(0,180,5,120)
i01.rightHand.majeure.setRest(35)
i01.rightHand.ringFinger.map(0,180,10,135)
i01.rightHand.ringFinger.setRest(35)
i01.rightHand.pinky.map(0,180,0,115)
i01.rightHand.pinky.setRest(10)
i01.rightHand.wrist.map(0,180,0,105)
i01.rightHand.wrist.setRest(60)

i01.startRightArm(rightPort)
# checked 5-9-2016
i01.rightArm.bicep.map(0,180,5,95)
i01.rightArm.bicep.setRest(30)
i01.rightArm.rotate.map(0,180,15,50)
i01.rightArm.rotate.setRest(88)
i01.rightArm.shoulder.map(0,180,20,150)
i01.rightArm.shoulder.setRest(34)
i01.rightArm.omoplate.map(0,180,10,55)
i01.rightArm.omoplate.setRest(20)

torso = i01.startTorso(leftPort)
# tweaking the torso settings
torso.topStom.map(0,180,65,115)
torso.midStom.map(0,180,20,160)
torso.topStom.setRest(90)
torso.midStom.setRest(90)
#torso.lowStom.setRest(90)		#dont have yet

print("opencv below works May 2")
opencv = i01.startOpenCV()
sleep(3)
opencv.capture()
sleep(2)
opencv.addFilter("Transpose")

#ni = Runtime.createAndStart("ni", "OpenNI")
#ni.startUserTracking()

#i01.headTracking.faceDetect()
#i01.headTracking.pyramidDown()
#to tweak the default PID values
#i01.headTracking.xpid.setPID(10.0,5.0,0.1)
#i01.headTracking.ypid.setPID(10.0,5.0,0.1)

i01.startEar()
ear =i01.ear
ear.addMouth(mouth)

# verbal commands
ear.addCommand("attach everything", "i01", "attach")
ear.addCommand("disconnect everything", "i01", "detach")
ear.addCommand("manual", ear.getName(), "lockOutAllGrammarExcept", "voice control")
ear.addCommand("voice control", ear.getName(), "clearLock")
ear.addCommand("camera on", i01.getName(), "cameraOn")
ear.addCommand("off camera", i01.getName(), "cameraOff")
ear.addCommand("relax", "python", "relax")
ear.addCommand("just rest", "python", "rest")
ear.addCommand("open hand", "python", "handopen")
ear.addCommand("close hand", "python", "handclose")
ear.addCommand("open your right hand", "python", "openrighthand")
ear.addCommand("open your left hand", "python", "openlefthand")
ear.addCommand("close your right hand", "python", "closerighthand")
ear.addCommand("close your left hand", "python", "closelefthand")
ear.addCommand("right turn", "python", "turnRight")
ear.addCommand("left turn", "python", "turnLeft")
ear.addCommand("move hips", "python", "fistHips")
ear.addCommand("arms front", "python", "armsFront")
ear.addCommand("perfect", "python", "perfect")
ear.addCommand("picture on the right side", "python", "picturerightside")
ear.addCommand("picture on the left side", "python", "pictureleftside")
ear.addCommand("look on your right side", "python", "lookrightside")
ear.addCommand("look around you", "python", "lookaroundyou")
ear.addCommand("look on your left side", "python", "lookleftside")
ear.addCommand("look back", "python", "lookback")
ear.addCommand("how many fingers do you have", "python", "howmanyfingersdoihave")
ear.addCommand("come here", "python", "comehere")
ear.addCommand("hello", "python", "hello")
ear.addCommand("system check", "python", "systemcheck")
ear.addCommand("guess what", "python", "guesswhat")
ear.addCommand("made by", "python", "madeby")
ear.addCommand("show your muscles", "python", "muscle")

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
ear.addCommand("move forward", "python", "mforward")
ear.addCommand("move backward", "python", "mback")
#ear.addCommand("left up", "python", "leftup") 
#ear.addCommand("left down", "python", "leftdown") 
#ear.addCommand("right up", "python", "rightup") 
#ear.addCommand("right down", "python", "rightdown") 
ear.addCommand("distance", "python", "analog") 
ear.addCommand("range", "python", "pings") 
ear.addCommand("heading", "python", "compass") 
ear.addCommand("point north", "python", "north") 
ear.addCommand("square", "python", "square") 

ear.startListening()

mouth.speakBlocking("Azul is ready to rock")
print("ready")

def relax():           
# changed 4-28-2015
# head rotatehead, neck, eyeX, eyeY, jaw
# hand thumb, index,  majeure,  ring,  pinky, wrist
# arm bicep, rotate, rotate shoulder, omoplate
  mouth.speakBlocking("#SWALLOW02#")
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
  mouth.speakBlocking("#BREATH02#")
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
  mouth.speakBlocking("#BREATH03#")

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
  i01.moveTorso(45,20,90)
  sleep(4)
  i01.moveTorso(135,170,90)
  sleep(4)
  i01.moveTorso(90,90,90)
  mouth.speakBlocking("#LAUGH03#")

def armsFront():        # changed 11-1-2015
# arm bicep, rotate, rotate shoulder, omoplate
    i01.moveArm("left",90,90,90,20)
    sleep(4)
    i01.moveArm("right",90,90,90,20)
    mouth.speakBlocking("#MMM02#")
  
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
      mouth.speakBlocking("come closer")
      i01.moveHead(60,80)
      i01.moveHand("right",180,2,175,160,165,26)
      sleep(2)
      i01.moveHead(118,80)
      i01.moveHand("right",180,164,175,160,165,26)
      sleep(2)
      i01.moveHead(60,80)
      sleep(1)
      mouth.speakBlocking("#SNEEZE01#")
      relax()
      
def madeby():
    i01.moveHead(80,86)
    i01.moveArm("left",5,90,30,10)
    i01.moveArm("right",5,90,30,10)
    i01.moveHand("left",45,40,30,25,35,90)
    i01.moveHand("right",55,2,50,48,30,90)
    i01.moveTorso(90,90,90)
    sleep(1)
    mouth.speakBlocking("hello")
    i01.moveHead(80,98)
    i01.moveArm("left",5,90,30,10)
    i01.moveArm("right",5,90,30,10)
    i01.moveHand("left",45,40,30,25,35,90)
    i01.moveHand("right",55,2,50,48,30,90)
    i01.moveTorso(90,90,90)
    sleep(0.5)
    i01.moveHead(90,89)
    i01.moveArm("left",42,104,30,10)
    i01.moveArm("right",33,116,30,10)
    i01.moveHand("left",45,40,30,25,35,120)
    i01.moveHand("right",55,2,50,48,30,40)
    i01.moveTorso(90,90,90)
    sleep(0.5)
    i01.moveHead(80,98)
    i01.moveArm("left",5,99,30,16)
    i01.moveArm("right",5,94,30,16)
    i01.moveHand("left",120,116,110,115,98,73)
    i01.moveHand("right",114,146,125,113,117,109)
    i01.moveTorso(90,90,90)
    mouth.speakBlocking("my name is Azul I am an Inmoov")
    i01.moveHead(68,90)
    i01.moveArm("left",5,99,30,16)
    i01.moveArm("right",85,102,38,16)
    i01.moveHand("left",120,116,110,115,98,73)
    i01.moveHand("right",114,146,161,132,168,19)
    i01.moveTorso(90,90,90)
    sleep(0.5) 
    i01.setHandSpeed("left", 0.85, 0.85, 0.85, 0.85, 0.85, 1.0)
    i01.setHandSpeed("right", 0.85, 0.85, 0.85, 0.85, 0.85, 1.0)
    i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
    i01.setArmSpeed("right", 0.90, 1.0, 1.0, 1.0)
    i01.moveArm("left",5,94,30,10)
    i01.moveArm("right",7,78,92,10)
    i01.moveHand("left",180,180,180,180,180,90)
    i01.moveHand("right",180,2,175,160,165,180)
    i01.setHeadSpeed(0.70, 0.70)
    i01.setTorsoSpeed(0.75, 0.85, 1.0)
    i01.moveHead(170,140)
    i01.moveTorso(80,150,90)
    sleep(1)
    mouth.speakBlocking("I am designed by gael langevin")
    sleep(2)   
    i01.setHandSpeed("left", 0.90, 0.90, 0.90, 0.90, 0.90, 0.95)
    i01.setHandSpeed("right", 0.90, 0.90, 0.90, 0.90, 0.90, 0.95)
    i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
    i01.setArmSpeed("right", 0.90, 1.0, 1.0, 1.0)
    i01.moveHead(105,94)
    i01.moveArm("left",5,99,36,16)
    i01.moveArm("right",81,105,42,16)
    i01.moveHand("left",120,116,110,115,98,50)
    i01.moveHand("right",114,118,131,132,168,19)
    i01.moveTorso(90,90,90)
    sleep(0.5)
    i01.moveHead(80,86)
    i01.moveArm("left",5,96,25,10)
    i01.moveArm("right",5,94,26,10)
    i01.moveHand("left",110,62,56,88,81,18)
    i01.moveHand("right",78,88,101,95,81,137)
    i01.moveTorso(90,90,90)
    sleep(0.5)
    i01.moveHead(75,97)
    i01.moveArm("left",85,106,25,18)
    i01.moveArm("right",87,107,32,18)
    i01.moveHand("left",110,62,56,88,81,145)
    i01.moveHand("right",78,88,101,95,81,27)
    i01.moveTorso(90,90,90)
    mouth.speakBlocking("who is a french sculptor")
    sleep(2)
    i01.moveHead(80,86)
    i01.moveArm("left",5,96,25,10)
    i01.moveArm("right",5,94,26,10)
    i01.moveHand("left",110,62,56,88,81,18)
    i01.moveHand("right",78,88,101,95,81,137)
    i01.moveTorso(90,90,90)
    sleep(1)
    i01.moveArm("left",6,91,22,14)
    i01.moveArm("right",87,107,32,18)
    i01.moveHand("left",110,62,56,88,81,0)
    i01.moveHand("right",78,88,101,95,81,27)
    i01.setHeadSpeed(0.70, 0.70)
    i01.setTorsoSpeed(0.75, 0.85, 1.0)
    i01.moveHead(20,40)
    i01.moveTorso(120,30,90)
    mouth.speakBlocking("my software is being developped by myrobtlab dot org")
    sleep(2)
    i01.moveHead(20,69)
    i01.moveArm("left",6,91,22,14)
    i01.moveArm("right",87,107,32,21)
    i01.moveHand("left",110,62,56,88,81,0)
    i01.moveHand("right",78,88,101,95,81,27)
    i01.moveTorso(90,90,90)
    i01.mouth.setVoice("Rachel")
    mouth.speakBlocking("I am totally build with 3 D printed parts")
    i01.moveHead(75,97)
    i01.moveArm("left",85,106,25,18)
    i01.moveArm("right",87,107,32,18)
    i01.moveHand("left",110,62,56,88,81,145)
    i01.moveHand("right",78,88,101,95,81,27)
    i01.moveTorso(90,90,90)
    sleep(0.5)
    i01.moveHead(33,110)
    i01.moveArm("left",85,104,25,18)
    i01.moveArm("right",87,41,47,18)
    i01.moveHand("left",110,62,56,88,81,145)
    i01.moveHand("right",111,75,117,125,111,143)
    i01.moveTorso(90,90,90)
    sleep(0.5)
    i01.moveHead(62,102)
    i01.moveArm("left",85,104,25,18)
    i01.moveArm("right",87,41,47,18)
    i01.moveHand("left",110,62,56,88,81,145)
    i01.moveHand("right",111,75,117,125,111,143)
    i01.moveTorso(90,90,90)
    mouth.speakBlocking("which means all my parts")
    i01.moveHead(79,88)
    i01.moveArm("left",85,104,25,18)
    i01.moveArm("right",87,59,46,18)
    i01.moveHand("left",110,62,56,88,81,145)
    i01.moveHand("right",59,75,117,125,111,113)
    i01.moveTorso(90,90,90)
    mouth.speakBlocking("are made on a home 3 D printer")
    sleep(0.5)
    i01.moveHead(40,84)
    i01.moveArm("left",85,72,38,18)
    i01.moveArm("right",87,64,47,18)
    i01.moveHand("left",124,97,66,120,130,35)
    i01.moveHand("right",59,75,117,125,111,113)
    i01.moveTorso(90,90,90)
    sleep(0.5)
    i01.moveHead(97,80)
    i01.moveArm("left",85,79,39,14)
    i01.moveArm("right",87,76,42,12)
    i01.moveHand("left",124,97,66,120,130,35)
    i01.moveHand("right",59,75,117,125,111,113)
    i01.moveTorso(90,90,90)
    sleep(0.5)
    i01.moveHead(75,97)
    i01.moveArm("left",85,106,25,18)
    i01.moveArm("right",87,107,32,18)
    i01.moveHand("left",110,62,56,88,81,145)
    i01.moveHand("right",78,88,101,95,81,27)
    i01.moveTorso(90,90,90)
    sleep(0.5)
    mouth.speakBlocking("so anyone can reproduce me")
    i01.moveHead(80,98)
    i01.moveArm("left",5,90,30,10)
    i01.moveArm("right",5,90,30,10)
    i01.moveHand("left",45,40,30,25,35,90)
    i01.moveHand("right",55,2,50,48,30,90)
    i01.moveTorso(90,90,90)
    sleep(0.5)
    mouth.setVoice("Will")
    mouth.speakBlocking("#WHISTLE02#")
    i01.moveHead(116,80)
    i01.moveArm("left",85,93,42,16)
    i01.moveArm("right",87,93,37,18)
    i01.moveHand("left",124,82,65,81,41,143)
    i01.moveHand("right",59,53,89,61,36,21)
    i01.moveTorso(90,90,90)
    relax()     

def guesswhat():
    mouth.speak("I'm not really a human")
    mouth.speak("but I use Old spice body wash and deodorant together")

def rest():
# changed 4-28-2015
# head rotatehead, neck, eyeX, eyeY, jaw
# hand thumb, index,  majeure,  ring,  pinky, wrist
# arm bicep, rotate, rotate shoulder, omoplate
  mouth.speak("#YAWN01#")
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
  mouth.speak("#YAWN02#")
  
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
  mouth.speakBlocking("#CLICK02#")

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
  mouth.speakBlocking("cheeze")

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
  mouth.speakBlocking("#AARGH02#")

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
  mouth.speakBlocking("#COUGH02#")
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
     
def systemcheck():
     sleep(2)
     i01.setHeadSpeed(.75,.75)
     i01.moveHead(90,90)
     sleep(1)
     i01.moveHead(72,64)
     sleep(1)
     i01.moveHead(155,94)
     sleep(1)
     i01.moveHead(90,138)
     sleep(1)
     i01.moveHead(29,95)
     sleep(1)
     i01.moveHead(90,90)
     sleep(1)
     mouth.speakBlocking("Head, neck and mouth")
     mouth.speakBlocking("#BREATH01#")
     sleep(1)
     i01.setHeadSpeed(.9,.9)
     i01.moveHead(25,61)
     i01.moveArm("left",0,90,30,10)
     i01.setArmSpeed("right",.75,.75,.75,.75)
     i01.moveArm("right",24,62,52,45)
     i01.moveHand("left",0,0,0,0,0,90)
     i01.moveHand("right",0,0,0,0,0,90)
     sleep(2)
     i01.moveHead(90,90)
     i01.setHeadSpeed(.9,.9)
     sleep(1)
     mouth.speakBlocking("right arm and right shoulder")
     mouth.speakBlocking("#BREATH02#")
     sleep(1)
     i01.setHeadSpeed(.9,.9)
     i01.moveHead(20,122)
     i01.setArmSpeed("left",.75,.75,.75,.75)
     i01.moveArm("left",24,62,52,45)
     sleep(2)
     i01.moveHead(90,90)
     i01.setHeadSpeed(.9,.9)
     sleep(1)
     mouth.speakBlocking("left arm and left shoulder")
     mouth.speakBlocking("#BREATH03#")
     sleep(1)
     i01.setHeadSpeed(.9,.9)
     i01.moveHead(20,120)
     i01.moveArm("left",75,123,52,45)
     i01.moveArm("right",75,123,52,45)
     i01.moveHand("left",180,180,180,180,180,30)
     i01.moveHand("right",180,180,180,180,180,170)
     sleep(3)
     i01.setHeadSpeed(.9,.9)
     i01.moveHead(59,67)
     i01.moveHand("right",0,0,0,0,0,19)
     i01.moveHand("left",0,0,0,0,0,170)
     sleep(1)
     i01.moveHand("left",180,180,180,180,180,30)
     i01.moveHand("right",180,180,180,180,180,170)
     sleep(1.5)
     i01.moveHead(90,90)
     i01.setHeadSpeed(.9,.9)
     sleep(1)
     mouth.speakBlocking(" hands and Wrists")
     mouth.speakBlocking("#SNEEZE01#")
     sleep(1)
     i01.setTorsoSpeed(0.80, 0.80, 1.0)
     i01.moveTorso(30,30,90)
     sleep(5)
     i01.moveTorso(140,150,90)
     sleep(5)
     i01.moveTorso(80,90,90)
     sleep(3) 
     mouth.speakBlocking(" hips and waste")
     mouth.speakBlocking("#SNEEZE02#")
     i01.moveHead(90,90)
     i01.moveArm("left",0,90,30,10)
     i01.moveArm("right",0,90,30,10)
     i01.moveHand("left",0,0,0,0,0,90)
     i01.moveHand("right",0,0,0,0,0,90)
     mouth.speakBlocking("all servos are functioning properly")
     sleep(1.5)
     mouth.speakBlocking("awaiting your commands")
     mouth.speakBlocking("#YAWN01#")
     relax()    

def lookaroundyou(): 
     i01.setHeadSpeed(0.8, 0.8, 0.6, 0.6, 1.0)
     mouth.speakBlocking("time just flies away")
     lookrightside()
     sleep(2)
     lookleftside()
     sleep(2)
     relax()

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
     
def fforward1():
     serial.write(b'F12\r')	# go forward at speed of 10
     serial.write(b'G2\r')	# leds center of head
#     print "forward 14"
#     clearbuffer()  

def fforward2():
     serial.write(b'F15\r')
     serial.write(b'G2\r')	# leds center of head
#     print "forward 15"
#     clearbuffer()   

def fforward3():
     serial.write(b'F17\r')
     serial.write(b'G2\r')	# leds center of head
#     print "forward 20"
#     clearbuffer()   

def fforward4():
     serial.write(b'F20\r')
     serial.write(b'G2\r')	# leds center of head
#     print "forward 25"
#     clearbuffer()   

def fforward5():
     serial.write(b'F25\r')
     serial.write(b'G2\r')	# leds center of head
#     print "forward 30"
#     clearbuffer()   

def backward():
     serial.write(unicode("B14\r"))
     serial.write(b'G5\r')	# green eye of head
#     print "backward"
#     clearbuffer()

def turnright():
     serial.write("R13\r")	# was 15 but to fast
     serial.write(b'G6\r')	# leds right side of head
#     print "right"
#     clearbuffer()

def turnleft():
     serial.write("L13\r")	# was 15 but to fast
     serial.write(b'G1\r')	# leds left side of head
#     print "left"
#     clearbuffer()

def allstop():
     serial.write("S90\r")
     serial.write(b'G0\r')	# leds all off
     print "stop"
#     clearbuffer()

def mforward():
     serial.write("M13\r")
#     print "fwd till obstical"
#     clearbuffer()

def mback():
     serial.write("W13\r")
#     print "back till obstical"
#     clearbuffer()

def north():
    serial.write(b'G2\r')	# leds center of head
    serial.write("N\r")
#     print "find north"
#     clearbuffer()
# raise arm point finger
# head rotatehead, neck, eyeX, eyeY, jaw
# hand thumb, index,  majeure,  ring,  pinky, wrist
# arm bicep, rotate, rotate shoulder, omoplate
    sleep(3)
    i01.setHandSpeed("left", 0.85, 0.85, 0.85, 0.85, 0.85, 1.0)
    i01.setHandSpeed("right", 1.0, 0.85, 1.0, 1.0, 1.0, 1.0)
    i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
    i01.setArmSpeed("right", 0.90, 0.90, 0.90, 0.90)
    i01.setHeadSpeed(1.0, 0.90)
    i01.setTorsoSpeed(0.85, 0.85, 1.0)
    i01.moveHead(80,86,85,85,52)
    i01.moveArm("left",5,94,30,10)
    i01.moveArm("right",7,74,140,10)
    i01.moveHand("left",180,180,180,180,180,90)
    i01.moveHand("right",180,2,175,160,165,180)
    i01.moveTorso(90,90,90)

def square():
     serial.write("Q5\r")
#     print "run pattern"
#     clearbuffer()

#would like to clean out serial buffer
def clearbuffer():
  global serdata
  serdata = ''
  crap = 0
  crap = serial.available()
#  print("crap serial buffer count = " + str(crap))  # how many characters of crap
  if crap > 0:
    for i in range(1,crap): 
      junk = serial.read()		# out with the crap
#      print("junk=" + chr(junk) + " " + str(junk))   # show me
      serdata += chr(junk)
#  print( str(serdata))			# show string
   
def analog():
  global method
  global serdata
  method = 'analog'
  clearbuffer()
  serial.write("A\r")
  print("distance")
  onByte()
  cnt0 = serdata.find("A0=")		# find begin of data wanted
  cnt1 = serdata.find("A1=")
  cnt2 = serdata.find("A2=")
  cnt3 = serdata.find("A3=")
  cnt4 = serdata.find("v")
  if( cnt0 >0 ):
    print( serdata[(cnt0+3):(cnt1-1)] )	# want to print data starting with A3= or range of data
  if( cnt1 >0 ):
    print( serdata[(cnt1+3):(cnt2-1)] )	# want to print data starting with A3= or range of data
  if( cnt2 >0 ):
    print( serdata[(cnt2+3):(cnt3-1)] )	# want to print data starting with A3= or range of data
  if( cnt3 >0 ):
    print( serdata[(cnt3+3):(cnt4-1)] )	# want to print data starting with A3= or range of data
    mouth.speakBlocking("battery" + str(serdata[(cnt3+3):(cnt4-1)]))

def compass():
  global serdata
  global method
  method = 'compass'
  clearbuffer()
  serial.write("C\r")
  print("compass")
  onByte()
  cnt = serdata.find("C0=")
  cnt1 = serdata.find(".")
  if( cnt >0 ):
    print( serdata[(cnt+3):(cnt1+2)] )	# want to print data starting with A3= or range of data
    mouth.speakBlocking("heading" + str(serdata[(cnt+3):(cnt1)]))

def pings():
  global method
  global serdata
  method = 'ping'
  clearbuffer()
  serial.write("P\r")
  sleep(3.5)				# added because it takes longer to read pings
  print("range")			# time of 3 gets most of it
  onByte()
  cnt0 = serdata.find("P0=")		# find begin of data wanted
  cnt1 = serdata.find("P1=")
  cnt2 = serdata.find("P2=")
  cnt3 = serdata.find("P3=")
  cnt4 = serdata.find("P4=")
  if( cnt0 >0 ):
    print( serdata[(cnt0+3):(cnt1-1)] )	# want to print data starting with A0= or range of data
    mouth.speakBlocking("ping one" + str(serdata[(cnt0+3):(cnt1-1)]))
  if( cnt1 >0 ):
    print( serdata[(cnt1+3):(cnt2-1)] )	# want to print data starting with A1= or range of data
    mouth.speakBlocking("ping two" + str(serdata[(cnt1+3):(cnt2-1)]))
  if( cnt2 >0 ):
    print( serdata[(cnt2+3):(cnt3-1)] )	# want to print data starting with A2= or range of data
    mouth.speakBlocking("ping three" + str(serdata[(cnt2+3):(cnt3-1)]))
  if( cnt3 >0 ):
    print( serdata[(cnt3+3):(cnt4-1)] )	# want to print data starting with A3= or range of data
    mouth.speakBlocking("ping four" + str(serdata[(cnt3+3):(cnt4-1)]))
  if( cnt4 >0 ):
    print( serdata[(cnt4+3):(cnt4+6)] )	# want to print data starting with A4= or range of data
 
def onByte():
  global serdata, method
  sleep(.5)
  data = serial.available()			# amount of possible characters
#  print("serial buffer data count=" + str(data)) # show me how many
  if data > 0:					# is there data
      for i in range(1,data): 			# get data
        c = chr( serial.read() )
        serdata += c				# make into string
      print("data ", method, str(serdata)) 	# show completed string

def input(cmd):
    if (cmd == "NumPad-2"):
        backward()
    if (cmd == "NumPad-4"):
        turnleft()
    if (cmd == "NumPad-5"):
        allstop()
    if (cmd == "NumPad-6"):
        turnright()    
    if (cmd == "NumPad-7"):
        fforward1() 
    if (cmd == "NumPad-8"):
        fforward2() 
    if (cmd == "NumPad-9"):
        fforward3() 
    if (cmd == "NumPad-0"):
        pings()
    if (cmd == "NumPad-3"):
        compass()
    if (cmd == "NumPad-1"):
        analog()
# next 4 are just trying to get Azul to go straight
    if (cmd == "A"):
      global offsetL
      offsetL = offsetL + 1
      serial.write("X\r")
      print ("offset left =" + str(offsetL))
    if (cmd == "S"):
     global offsetL
     offsetL = offsetL - 1
     serial.write("Y\r")
     print ("offset left =" + str(offsetL))
    if (cmd == "D"):
     global offsetR
     offsetR = offsetR + 1
     serial.write("T\r")
     print ("offset left =" + str(offsetR))
    if (cmd == "F"):
     global offsetR
     offsetR = offsetR - 1
     serial.write("U\r")
     print ("offset left =" + str(offsetR))
  
def onConnect(portName):
  print('connected', portName)
 
def onDisconnect(portName):
  print('disconnected', portName)
        
