#file : Small_Test-pi.py
# teting on Azul Dec 21 2016

import time

webgui = Runtime.start("webgui","WebGui")

#Azul pi ACM0 is uno, ACM1 is mega
leftPort = "/dev/ttyACM1"
rightPort = "/dev/ttyACM0"
headPort = leftPort

i01 = Runtime.create("i01", "InMoov")

print("head")
head = Runtime.create("i01.head","InMoovHead")
# checked 5-21-2016  120 is mouth closed
head.jaw.map(0,180,50,120)
head.jaw.setRest(100)
# checked head 5-9-2016 
head.eyeY.map(0,180,10,65)    # up is 10 down in 65
head.eyeY.setRest(60)
head.eyeX.map(0,180,10,65)    # no motor on x, burned up
head.eyeX.setRest(30)
head.neck.map(0,180,67,175)
head.neck.setRest(144)
head.rothead.map(0,180,0,170)
head.rothead.setRest(95)

print("arms and hands")
leftHand = Runtime.create("i01.leftHand","InMoovHand")
# checked 5-15-2016 Azul new dual stage pulleys, reversed open and closed
#leftHand.thumb.setMaxVelocity(250)
leftHand.thumb.map(0,180,110,10)
leftHand.thumb.setRest(35)
#leftHand.index.setMaxVelocity(250)
leftHand.index.map(0,180,150,25)
leftHand.index.setRest(50)
#leftHand.majeure.setMaxVelocity(250)
leftHand.majeure.map(0,180,25,170)
leftHand.majeure.setRest(35)
#leftHand.ringFinger.setMaxVelocity(250)
leftHand.ringFinger.map(0,180,145,20)
leftHand.ringFinger.setRest(35)
#leftHand.pinky.setMaxVelocity(250)
leftHand.pinky.map(0,180,120,0)
leftHand.pinky.setRest(44)
#leftHand.wrist.setMaxVelocity(250)
leftHand.wrist.map(0,180,25,125)
leftHand.wrist.setRest(90)

leftArm = Runtime.create("i01.leftArm","InMoovArm")
#  checked 5-9-2016
#leftArm.bicep.setMaxVelocity(26)
leftArm.bicep.map(0,180,5,95)
leftArm.bicep.setRest(25)
#leftArm.rotate.setMaxVelocity(18)
leftArm.rotate.map(0,180,10,130)
leftArm.rotate.setRest(90)
#leftArm.shoulder.setMaxVelocity(14)
leftArm.shoulder.map(0,180,5,135)
leftArm.shoulder.setRest(25)
#leftArm.omoplate.setMaxVelocity(15)
leftArm.omoplate.map(0,180,10,35)
leftArm.omoplate.setRest(25)

rightHand = Runtime.create("i01.rightHand","InMoovHand")
#  checked 5-19-2016
#rightHand.thumb.setMaxVelocity(250)
rightHand.thumb.map(0,180,15,150)
rightHand.thumb.setRest(35)
#rightHand.index.setMaxVelocity(250)
rightHand.index.map(0,180,25,180)
rightHand.index.setRest(35)
#rightHand.majeure.setMaxVelocity(250)
rightHand.majeure.map(0,180,5,180)
rightHand.majeure.setRest(35)
#rightHand.ringFinger.setMaxVelocity(250)
rightHand.ringFinger.map(0,180,20,180)
rightHand.ringFinger.setRest(35)
#rightHand.pinky.setMaxVelocity(250)
rightHand.pinky.map(0,180,0,180)
rightHand.pinky.setRest(35)
#rightHand.wrist.setMaxVelocity(250)
rightHand.wrist.map(0,180,0,105)
rightHand.wrist.setRest(60)

rightArm = Runtime.create("i01.rightArm","InMoovArm")
# checked 5-9-2016
#rightArm.bicep.setMaxVelocity(26)
rightArm.bicep.map(0,180,5,95)
rightArm.bicep.setRest(30)
#rightArm.rotate.setMaxVelocity(18)
rightArm.rotate.map(0,180,15,50)
rightArm.rotate.setRest(40)
#rightArm.shoulder.setMaxVelocity(14)
rightArm.shoulder.map(0,180,20,150)
rightArm.shoulder.setRest(34)
#rightArm.omoplate.setMaxVelocity(15)
rightArm.omoplate.map(0,180,10,60)
rightArm.omoplate.setRest(25)

print("torso")
torso = Runtime.create("i01.torso", "InMoovTorso")
# checked 5-9-2016
#torso.topStom.setMaxVelocity(13)
torso.topStom.map(0,180,65,115)		# hips up and down
#torso.midStom.setMaxVelocity(13)
torso.midStom.map(0,180,20,160)		# turns right and left
torso.topStom.setRest(105)
torso.midStom.setRest(95)
torso.lowStom.setRest(90)		# dont have yet

print("start mouth and ear")
i01.startEar()
i01.startMouth()
mouth = i01.mouth
mouth.speakBlocking("My name is Azul")

# trying to start up slowly
print("start servos")
mouth.speakBlocking("start servos")
i01 = Runtime.start("i01","InMoov")
sleep(2)
mouth.speakBlocking("right hand")
i01.startRightHand(rightPort,"uno")
sleep(3)
mouth.speakBlocking("right arm")
i01.startRightArm(rightPort)
sleep(3)
mouth.speakBlocking("head")
i01.startHead(leftPort,"atmega2560")
sleep(3)
mouth.speakBlocking("left hand")
i01.startLeftHand(leftPort)
sleep(3)
mouth.speakBlocking("left arm")
i01.startLeftArm(leftPort)
sleep(3)
mouth.speakBlocking("torso")
#i01.starttorso(leftPort)
sleep(3)

print("ear")
ear =i01.ear
ear.addMouth(mouth)

# verbal commands
ear.addCommand("relax", "python", "relax")
ear.addCommand("open your hands", "python", "handopen")
ear.addCommand("close your hands", "python", "handclose")
ear.addCommand("open your right hand", "python", "openrighthand")
ear.addCommand("open your left hand", "python", "openlefthand")
ear.addCommand("close your right hand", "python", "closerighthand")
ear.addCommand("close your left hand", "python", "closelefthand")
ear.addCommand("move hips", "python", "fistHips")
 
ear.addComfirmations("yes","correct","ya","yeah")
ear.addNegations("no","wrong","nope","nah")

ear.startListening()
mouth.speakBlocking("Azul is ready on PI")
 
def relax():           
# changed 7-6-2015
# head rotatehead, neck, eyeX, eyeY, jaw
# hand thumb, index,  majeure,  ring,  pinky, wrist
# arm bicep, rotate, rotate shoulder, omoplate
  mouth.speakBlocking("relaxing")
  i01.setHandSpeed("left", 0.85, 0.85, 0.85, 0.85, 0.85, 0.85)
  i01.setHandSpeed("right", 0.85, 0.85, 0.85, 0.85, 0.85, 0.85)
  i01.setArmSpeed("right", 0.85, 0.85, 0.85, 0.75)
  i01.setArmSpeed("left", 0.85, 0.85, 0.85, 0.75)
  i01.setHeadSpeed(0.85, 0.85)
  i01.setTorsoSpeed(0.75, 0.75, 1.0)
# head rotatehead, neck, eyeX, eyeY, jaw
  i01.moveHead(79,110,90,110,140)
  sleep(1)
# close fingers  
# hand thumb, index,  majeure,  ring,  pinky, wrist
  i01.moveHand("right",130,130,130,130,130,90)
  sleep(1)
  i01.moveHand("left",130,130,130,130,130,90)
# arm bicep, rotate, rotate shoulder up-down, omoplate
  i01.moveArm("left",70,90,30,40)
  sleep(2)
  i01.moveArm("right",70,90,30,40)
  sleep(2)
  i01.moveTorso(95,90,90)	# was 90,90,90

def handopen():
# changed 4-28-2015
# hand thumb, index,  majeure,  ring,  pinky, wrist
  i01.setHandSpeed("left", 0.85, 0.85, 0.85, 0.85, 0.85, 0.85)
  i01.setHandSpeed("right", 0.85, 0.85, 0.85, 0.85, 0.85, 0.85)
  i01.moveHand("left",0,0,0,0,0)
  sleep(1)
  i01.moveHand("right",0,0,0,0,0)
  i01.mouth.speak("fingers open")


def handclose():
# changed 4-28-2015
# hand thumb, index,  majeure,  ring,  pinky, wrist
  i01.setHandSpeed("left", 0.85, 0.85, 0.85, 0.85, 0.85, 0.85)
  i01.setHandSpeed("right", 0.85, 0.85, 0.85, 0.85, 0.85, 0.85)
  i01.moveHand("left",180,180,180,180,180)
  sleep(1)
  i01.moveHand("right",180,180,180,180,180)
  i01.mouth.speak("fingers closed")

def openlefthand():
# changed 4-28-2015
# hand thumb, index,  majeure,  ring,  pinky, wrist
  i01.setHandSpeed("left", 0.95, 0.95, 0.95, 0.95, 0.95, 0.95)
  i01.moveHand("left",0,0,0,0,0)
  i01.mouth.speak("left fingers open")

def openrighthand():
# changed 4-28-2015
# hand thumb, index,  majeure,  ring,  pinky, wrist
  i01.setHandSpeed("right", 0.95, 0.95, 0.95, 0.95, 0.95, 0.95)
  i01.moveHand("right",0,0,0,0,0)
  i01.mouth.speak("right fingers open")

def closelefthand():
# changed 4-28-2015
# hand thumb, index,  majeure,  ring,  pinky, wrist
  i01.setHandSpeed("left", 0.85, 0.85, 0.85, 0.85, 0.85, 0.85)
  i01.moveHand("left",180,180,180,180,180)
  i01.mouth.speak("left fingers closed")

def closerighthand():
# changed 4-28-2015
# hand thumb, index,  majeure,  ring,  pinky, wrist
  i01.setHandSpeed("right", 0.85, 0.85, 0.85, 0.85, 0.85, 0.85)
  i01.moveHand("right",180,180,180,180,180)
  i01.mouth.speak("right fingers closed")
  
def fistHips():
# changed 4-28-2015
# head rotatehead, neck, eyeX, eyeY, jaw
# hand thumb, index,  majeure,  ring,  pinky, wrist
# arm bicep, rotate, rotate shoulder, omoplate
# stomach hips, rotate, not used yet
  i01.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
  i01.setHeadSpeed(1.0, 1.0)
  i01.setTorsoSpeed(0.80, 0.80, 1.0)
  i01.moveHead(138,80)
  sleep(1)
  i01.moveArm("left",79,42,23,41)
  sleep(1)
  i01.moveArm("right",71,40,14,39)
  sleep(1)
  i01.moveHand("left",180,180,180,180,180,47)
  i01.moveHand("right",99,130,152,154,145,180)
  sleep(1)
# turn first
  i01.moveTorso(90,20,90)
  sleep(3)
# now move hips
  i01.moveTorso(45,20,90)
  sleep(4)
# turn first
  i01.moveTorso(90,170,90)
  sleep(4)
# now move hips
  i01.moveTorso(135,170,90)
  sleep(4)
  i01.moveTorso(90,90,90)


