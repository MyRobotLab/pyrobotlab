#file : azul.v11.py
# may 3 2015 updated commands and added pir to wake up
# may 31 added middle stomach
# jun 1 changing routines to add stomach

import random
import time
from java.lang import String

#laptop uno=right 8  mega=left 9 (pir sensor on 30) and head  eddie 10
leftPort = "COM9"
rightPort = "COM8"

i01 = Runtime.createAndStart("i01", "InMoov")

# starting parts
i01.startMouth()
#to tweak the default voice
i01.mouth.setGoogleURI("http://thehackettfamily.org/Voice_api/api2.php?voice=Ryan&txt=")

i01.startHead(leftPort)
# checked head 3-7-2015 no eye motors
#i01.head.eyeY.setMinMax(20,80)
i01.head.eyeY.map(0,180,20,80)
i01.head.eyeY.setRest(60)
#i01.head.eyeX.setMinMax(20,80)
i01.head.eyeX.map(0,180,20,80)
i01.head.eyeX.setRest(60)
#i01.head.neck.setMinMax(10,150)
i01.head.neck.map(0,180,10,150)
i01.head.neck.setRest(90)
#i01.head.rothead.setMinMax(15,165)
i01.head.rothead.map(0,180,15,165)
i01.head.rothead.setRest(100)

i01.startMouthControl(leftPort)
# checked 3-7-2015
#i01.head.jaw.setMinMax(10,65)
i01.head.jaw.map(0,180,65,10)
i01.mouthControl.setmouth(10,65)

helvar = 1
# added so i can limit scotter from waking up to soon as in any movement
timespir = 0

# added for pir sesor
mega = Runtime.createAndStart("i01.left", "mega")
mega.connect(leftPort)
print "pir is setup"
readDigitalPin = 30
mega.addListener("publishPin", "python", "input")
mega.setSampleRate(4000)

i01.startEar()

i01.startLeftHand(leftPort)
# checked 3-7-2015
#i01.leftHand.thumb.setMinMax(30,140)
i01.leftHand.thumb.map(0,180,30,140)
#i01.leftHand.index.setMinMax(0,135)
i01.leftHand.index.map(0,180,0,135)
#i01.leftHand.majeure.setMinMax(20,170)
i01.leftHand.majeure.map(0,180,20,170)
#i01.leftHand.ringFinger.setMinMax(20,145)
i01.leftHand.ringFinger.map(0,180,20,145)
#i01.leftHand.pinky.setMinMax(0,110)
i01.leftHand.pinky.map(0,180,0,110)

#i01.leftHand.wrist.setMinMax(10,150)
i01.leftHand.wrist.map(0,180,10,150)
i01.leftHand.wrist.setRest(90)

i01.startLeftArm(leftPort)
#i01.leftArm.bicep.setMinMax(0,90)
i01.leftArm.bicep.map(0,180,0,90)
i01.leftArm.bicep.setRest(10)
#i01.leftArm.rotate.setMinMax(0,130)
i01.leftArm.rotate.map(0,180,0,130)
i01.leftArm.rotate.setRest(60)
#i01.leftArm.shoulder.setMinMax(10,125)
i01.leftArm.shoulder.map(0,180,10,125)
i01.leftArm.shoulder.setRest(20)
#i01.leftArm.omoplate.setMinMax(0,60)
i01.leftArm.omoplate.map(0,180,0,60)
i01.leftArm.omoplate.setRest(15)

#  checked 3-7-2015
i01.startRightHand(rightPort)
#i01.rightHand.thumb.setMinMax(10,110)
i01.rightHand.thumb.map(0,180,10,110)
i01.rightHand.thumb.setRest(10)
#i01.rightHand.index.setMinMax(0,110)
i01.rightHand.index.map(0,180,0,110)
#i01.rightHand.majeure.setMinMax(0,140)
i01.rightHand.majeure.map(0,180,0,140)
#i01.rightHand.ringFinger.setMinMax(0,115)
i01.rightHand.ringFinger.map(0,180,0,115)
#i01.rightHand.pinky.setMinMax(0,100)
i01.rightHand.pinky.map(0,180,0,100)
i01.rightHand.pinky.setRest(10)
#i01.rightHand.wrist.setMinMax(10,90)
i01.rightHand.wrist.map(0,180,10,90)
i01.rightHand.wrist.setRest(90)

i01.startRightArm(rightPort)
# checked 3-7-2015
#i01.rightArm.bicep.setMinMax(10,95)
i01.rightArm.bicep.map(0,180,10,95)
i01.rightArm.bicep.setRest(20)
#i01.rightArm.rotate.setMinMax(20,150)
i01.rightArm.rotate.map(0,180,20,150)
i01.rightArm.rotate.setRest(90)
#i01.rightArm.shoulder.setMinMax(20,150)
i01.rightArm.shoulder.map(0,180,20,150)
i01.rightArm.shoulder.setRest(30)
#i01.rightArm.omoplate.setMinMax(10,60)
i01.rightArm.omoplate.map(0,180,10,60)
i01.rightArm.omoplate.setRest(20)

torso = i01.startTorso(leftPort)
# tweaking the torso settings only top stomach works BECAREFUL OF BODY IN THE WAY
#torso.topStom.setMinMax(65,115)
torso.topStom.map(0,180,65,115)
torso.midStom.setMinMax(0,180)
#torso.lowStom.setMinMax(0,180)
torso.topStom.setRest(90)
torso.midStom.setRest(90)
#torso.lowStom.setRest(90)

print("opencv")
opencv = Runtime.start("opencv","OpenCV")
sleep(2)
opencv.capture()
#ni = Runtime.createAndStart("ni", "OpenNI")
#ni.startUserTracking()

#i01.headTracking.faceDetect()
#i01.headTracking.pyramidDown()
#to tweak the default Pid values
#i01.headTracking.xpid.setPID(10.0,5.0,0.1)
#i01.headTracking.ypid.setPID(10.0,5.0,0.1)

# note parallax pir is active high, small radio shack pir is active low
# scooter has radio shack pir sensor and azul has parallax sensor
def input(pin):
  global timespir
#  print( pin.pin, pin.value, pin.type, pin.source )   
  if (pin.value == 1):
     timespir = timespir + 1			#added because it was going off too munch
     if (timespir > 5):
       mega.digitalReadPollingStop(readDigitalPin)     #turn off pir sensor
       timespir = 0				#reset counter for pir
       print pin.pin, pin.value, pin.type, pin.source,    
       print("***    some one is here    ***")		#show me in code working
       i01.mouth.speak("howdy partner, i was resting")
       rightSerialPort.digitalWrite(53, Arduino.HIGH)
       leftSerialPort.digitalWrite(53, Arduino.HIGH)
       sleep(2)
       for pos in range(0,2):			#move head like waking up
         i01.setHeadSpeed(0.80, 0.80)
         i01.moveHead(100,60)
         sleep(2)
         i01.moveHead(60,110)
         sleep(2)
       i01.moveHead(90,90)

# auto detaches any attached servos after 120 seconds of inactivity
# does not work may 2015 gives error no attribute
#i01.autoPowerDownOnInactivity(120)

#i01.speakErrors(false)
# purges any "auto" methods
#i01.purgeAllTasks()

# remote control services
# WebGUI - for more information see
# http://myrobotlab.org/service/WebGUI

# Xmpp - for more information see
# http://myrobotlab.org/service/Xmpp

# system check - called at anytime
#i01.systemCheck()

# take the current position of all attached servos <- FIXME
# and create a new method named "newGesture"
#i01.captureGesture("newGesture")

# all ear associations are done python startEar() only starts
# the peer service
# After ear.startListening(), the ear will listen for commands

# verbal commands
ear = i01.ear
ear.addCommand("rest", "python", "rest")
ear.addCommand("attach head", "i01.head", "attach")
ear.addCommand("disconnect head", "i01.head", "detach")
ear.addCommand("attach eyes", "i01.head.eyeY", "attach")
ear.addCommand("disconnect eyes", "i01.head.eyeY", "detach")
ear.addCommand("attach right hand", "i01.rightHand", "attach")
ear.addCommand("disconnect right hand", "i01.rightHand", "detach")
ear.addCommand("attach left hand", "i01.leftHand", "attach")
ear.addCommand("disconnect left hand", "i01.leftHand", "detach")
ear.addCommand("attach everything", "i01", "attach")
ear.addCommand("disconnect everything", "i01", "detach")
ear.addCommand("attach left arm", "i01.leftArm", "attach")
ear.addCommand("disconnect left arm", "i01.leftArm", "detach")
ear.addCommand("attach right arm", "i01.rightArm", "attach")
ear.addCommand("disconnect right arm", "i01.rightArm", "detach")
ear.addCommand("search humans", "python", "trackHumans")
ear.addCommand("quit search", "python", "stopTracking")
ear.addCommand("track", "python", "trackPoint")
ear.addCommand("freeze track", "python", "stopTracking")
ear.addCommand("open hand", "python", "handopen")
ear.addCommand("close hand", "python", "handclose")
ear.addCommand("camera on", "i01", "cameraOn")
ear.addCommand("off camera", "i01", "cameraOff")
ear.addCommand("capture gesture", "i01", "captureGesture")
ear.addCommand("giving", "i01", "giving")
ear.addCommand("fighter", "i01", "fighter")
ear.addCommand("fist hips", "python", "fistHips")
ear.addCommand("look at this", "i01", "lookAtThis")
ear.addCommand("victory", "i01", "victory")
ear.addCommand("arms up", "i01", "armsUp")
ear.addCommand("arms front", "i01", "armsFront")
ear.addCommand("da vinci", "i01", "daVinci")
ear.addCommand("manual", ear.getName(), "lockOutAllGrammarExcept", "voice control")
ear.addCommand("voice control", ear.getName(), "clearLock")
ear.addCommand("stop listening", ear.getName(), "stopListening")
ear.addCommand("full speed", "python", "fullspeed")
ear.addCommand("grab the bottle", "python", "grabthebottle")
ear.addCommand("take the glass", "python", "grabtheglass")
ear.addCommand("poor bottle", "python", "poorbottle")
ear.addCommand("give the glass", "python", "givetheglass")
ear.addCommand("take the ball", "python", "takeball")
ear.addCommand("keep the ball", "python", "keepball")
ear.addCommand("approach the left hand", "python", "approachlefthand")
ear.addCommand("use the left hand", "python", "uselefthand")
ear.addCommand("more", "python", "more")
ear.addCommand("hand down", "python", "handdown")
ear.addCommand("is it a ball", "python", "isitaball")
ear.addCommand("put it down", "python", "putitdown")
ear.addCommand("drop it", "python", "dropit")
ear.addCommand("remove your left arm", "python", "removeleftarm")
ear.addCommand("relax", "python", "relax")
ear.addCommand("what is it", "python", "studyball")
ear.addCommand("perfect", "python", "perfect")
ear.addCommand("delicate grab", "python", "delicategrab")
ear.addCommand("release delicate", "python", "releasedelicate")
ear.addCommand("open your right hand", "python", "openrighthand")
ear.addCommand("open your left hand", "python", "openlefthand")
ear.addCommand("close your right hand", "python", "closerighthand")
ear.addCommand("close your left hand", "python", "closelefthand")
ear.addCommand("right turn", "python", "turnRight")
ear.addCommand("left turn", "python", "turnLeft")
ear.addCommand("surrender", "python", "surrender")
ear.addCommand("picture on the right side", "python", "picturerightside")
ear.addCommand("picture on the left side", "python", "pictureleftside")
ear.addCommand("picture on both sides", "python", "picturebothside")
ear.addCommand("look on your right side", "python", "lookrightside")
ear.addCommand("look on your left side", "python", "lookleftside")
ear.addCommand("look back", "python", "lookback")
ear.addCommand("look in the middle", "python", "lookinmiddle")
ear.addCommand("before happy", "python", "beforehappy")
ear.addCommand("happy birthday", "python", "happy")
ear.addCommand("photo", "python", "photo")
ear.addCommand("about", "python", "about")
ear.addCommand("power down", "python", "powerdown")
ear.addCommand("power up", "python", "powerup")
ear.addCommand("servo", "python", "servos")
ear.addCommand("how many fingers do you have", "python", "howmanyfingersdoihave")
ear.addCommand("show your muscles", "python", "muscle")
ear.addCommand("shake hand", "python", "shakehand")
ear.addCommand("unhappy", "python", "unhappy")
ear.addCommand("take this", "python", "takethis")
ear.addCommand("rock paper scissors", "python", "rockpaperscissors")
ear.addCommand("ready", "python", "ready")
ear.addCommand("rock", "python", "rock")
ear.addCommand("paper", "python", "paper")
ear.addCommand("scissors", "python", "scissors")
ear.addCommand("that was fun", "python", "thatwasfun")
ear.addCommand("guess what", "python", "guesswhat")
ear.addCommand("finger", "python", "finger")
ear.addCommand("come here", "python", "comehere")
ear.addCommand("phone home", "python", "phonehome")
ear.addCommand("made by", "python", "madeby")
ear.addCommand("look around you", "python", "lookaroundyou")
ear.addCommand("system check", "python", "systemcheck")
ear.addComfirmations("yes","correct","ya","yeah")
ear.addNegations("no","wrong","nope","nah")
ear.startListening("sorry | how do you do | hello | bye bye | thanks | thank you | shake hand | nice")
i01.startPIR("leftPort",30)   #now start up pir sensor
i01.mouth.speak("azuul is ready")

# set up a message route from the ear --to--> python method "heard"

ear.addListener("publishText", python.name, "heard", String().getClass());
# ear.addListener("recognized", "python", "heard")

def finger():
    i01.setHandSpeed("left", 0.85, 0.85, 0.85, 0.85, 0.85, 1.0)
    i01.setHandSpeed("right", 1.0, 0.85, 1.0, 1.0, 1.0, 1.0)
    i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
    i01.setArmSpeed("right", 0.90, 1.0, 1.0, 1.0)
    i01.setHeadSpeed(1.0, 0.90)
    # i01.setTorsoSpeed(1.0, 1.0, 1.0)
    i01.moveHead(80,86,85,85,72)
    i01.moveArm("left",5,94,30,10)
    i01.moveArm("right",7,78,92,10)
    i01.moveHand("left",180,180,180,180,180,90)
    i01.moveHand("right",180,2,175,160,165,180)
    # i01.moveTorso(90,90,90)

# rotatehead, neck, eyeX, eyeY, jaw
# hand right thumb, index, majeure, ring, pinky, wrist
def comehere():
    fullspeed()
    relax()
##look around
# rotatehead 15-150, neck 15-150, eyeX 20-80, eyeY, jaw 10-70
    i01.setHeadSpeed(0.80, 0.80, 0.90, 0.90, 1.0)
    i01.moveHead(20,66,7,85,72)
    sleep(3)
    i01.setHeadSpeed(0.50, 0.80, 0.90, 0.90, 1.0)
    i01.moveHead(130,110,175,85,72)
    sleep(3)
##raise arm point finger
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
    sleep(4.5)
##move finger
# hand thumb 110, index 100, majeure 120, ring 115, pinky 115, wrist 90
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
    i01.mouth.speak("come closer")
    i01.moveHead(60,80)
    i01.moveHand("right",180,2,175,160,165,26)
    sleep(2)
    i01.moveHead(118,80)
    i01.moveHand("right",180,164,175,160,165,26)
    sleep(2)
    i01.moveHead(60,80)
    sleep(1)
    relax()
    sleep(6)
    fullspeed()

def guesswhat():
    i01.mouth.speak("I'm not really a human man")
    i01.mouth.speak("but I use Old spice body wash and deodorant together")
    i01.mouth.speak("and now I'm really cool")

def rockpaperscissors():
    fullspeed()
    for y in range(0, 5):
        x = (random.randint(1, 3))
        if x == 1:
            ready()
            sleep(2)
            rock()
            sleep(2)
        if x == 2:
            ready()
            sleep(2)
            paper()
            sleep(2)
        if x == 3:
            ready()
            sleep(2)
            scissors()
            sleep(2)
    thatwasfun()

def ready():
    i01.mouth.speak("ready")
    i01.mouth.speak("go")
# changed 4-28-2015
# head rotatehead, neck, eyeX, eyeY, jaw
# hand thumb, index,  majeure,  ring,  pinky, wrist
# arm bicep, rotate, rotate shoulder, omoplate
    i01.moveHead(90,90)
    i01.moveArm("left",65,90,75,10)
    sleep(.5)
    i01.moveArm("right",20,80,25,20)
    sleep(.5)
    i01.moveHand("left",130,180,180,180,180,90)
    sleep(.5)
    i01.moveHand("right",50,90,90,90,100,90)

def rock():
    i01.moveHead(90,90,80,90,75)
    i01.moveArm("left",70,90,75,10)
    i01.moveArm("right",5,90,30,10)
    i01.moveHand("left",40,171,180,180,180,90)
    i01.moveHand("right",2,2,2,2,2,90)
    sleep(.3)
    i01.setHeadSpeed(.8,.8)
    i01.moveHead(60,107,80,90,75)
    i01.moveArm("left",49,90,75,10)
    i01.moveArm("right",5,90,30,10)
    i01.moveHand("left",40,171,180,180,180,90)
    i01.moveHand("right",2,2,2,2,2,90)
    sleep(.3)
    i01.moveHead(60,107,80,90,75)
    i01.moveArm("left",70,90,75,10)
    i01.moveArm("right",5,90,30,10)
    i01.moveHand("left",40,171,180,180,180,90)
    i01.moveHand("right",2,2,2,2,2,90)
    sleep(.3)
    i01.moveHead(60,107,80,90,75)
    i01.moveArm("left",49,90,75,10)
    i01.moveArm("right",5,90,30,10)
    i01.moveHand("left",40,171,180,180,180,90)
    i01.moveHand("right",2,2,2,2,2,90)
    sleep(.3)
    i01.moveHead(60,107,80,90,75)
    i01.moveArm("left",70,90,75,10)
    i01.moveArm("right",5,90,30,10)
    i01.moveHand("left",40,171,180,180,180,90)
    i01.moveHand("right",2,2,2,2,2,90)
    sleep(.3)
    i01.moveHead(90,90,80,90,75)
    i01.moveArm("left",49,90,75,10)
    i01.moveArm("right",5,90,30,10)
    i01.moveHand("left",40,171,180,180,180,140)
    i01.moveHand("right",2,2,2,2,2,90)
    sleep(.3)
    i01.mouth.speakBlocking("rock")

def paper():
    i01.moveHead(90,90,80,90,75)
    i01.moveArm("left",70,90,75,10)
    i01.moveArm("right",5,90,30,10)
    i01.moveHand("left",40,171,180,180,180,90)
    i01.moveHand("right",2,2,2,2,2,90)
    sleep(.3)
    i01.setHeadSpeed(.8,.8)
    i01.moveHead(60,107,80,90,75)
    i01.moveArm("left",49,90,75,10)
    i01.moveArm("right",5,90,30,10)
    i01.moveHand("left",40,171,180,180,180,90)
    i01.moveHand("right",2,2,2,2,2,90)
    sleep(.3)
    i01.moveHead(60,107,80,90,75)
    i01.moveArm("left",70,90,75,10)
    i01.moveArm("right",5,90,30,10)
    i01.moveHand("left",40,171,180,180,180,90)
    i01.moveHand("right",2,2,2,2,2,90)
    sleep(.3)
    i01.moveHead(60,107,80,90,75)
    i01.moveArm("left",49,90,75,10)
    i01.moveArm("right",5,90,30,10)
    i01.moveHand("left",40,171,180,180,180,90)
    i01.moveHand("right",2,2,2,2,2,90)
    sleep(.3)
    i01.moveHead(60,107,80,90,75)
    i01.moveArm("left",70,90,75,10)
    i01.moveArm("right",5,90,30,10)
    i01.moveHand("left",40,171,180,180,180,90)
    i01.moveHand("right",2,2,2,2,2,90)
    sleep(.3)
    i01.moveHead(90,90,80,90,75)
    i01.moveArm("left",49,90,75,10)
    i01.moveArm("right",5,90,30,10)
    i01.moveHand("left",0,0,0,0,0,165)
    i01.moveHand("right",2,2,2,2,2,90)
    sleep(.3)
    i01.mouth.speakBlocking("paper")

def scissors():
    i01.moveHead(90,90,80,90,75)
    i01.moveArm("left",70,90,75,10)
    i01.moveArm("right",5,90,30,10)
    i01.moveHand("left",40,171,180,180,180,90)
    i01.moveHand("right",2,2,2,2,2,90)
    sleep(.3)
    i01.setHeadSpeed(.8,.8)
    i01.moveHead(60,107,80,90,75)
    i01.moveArm("left",49,90,75,10)
    i01.moveArm("right",5,90,30,10)
    i01.moveHand("left",40,171,180,180,180,90)
    i01.moveHand("right",2,2,2,2,2,90)
    sleep(.3)
    i01.moveHead(60,107,80,90,75)
    i01.moveArm("left",70,90,75,10)
    i01.moveArm("right",5,90,30,10)
    i01.moveHand("left",40,171,180,180,180,90)
    i01.moveHand("right",2,2,2,2,2,90)
    sleep(.3)
    i01.moveHead(60,107,80,90,75)
    i01.moveArm("left",49,90,75,10)
    i01.moveArm("right",5,90,30,10)
    i01.moveHand("left",40,171,180,180,180,90)
    i01.moveHand("right",2,2,2,2,2,90)
    sleep(.3)
    i01.moveHead(60,107,80,90,75)
    i01.moveArm("left",70,90,75,10)
    i01.moveArm("right",5,90,30,10)
    i01.moveHand("left",40,171,180,180,180,90)
    i01.moveHand("right",2,2,2,2,2,90)
    sleep(.3)
    i01.moveHead(90,90,80,90,75)
    i01.moveArm("left",49,90,75,10)
    i01.moveArm("right",5,90,30,10)
    i01.moveHand("left",50,0,0,180,180,90)
    i01.moveHand("right",2,2,2,2,2,90)
    sleep(.3)
    i01.mouth.speakBlocking("scissors")

def thatwasfun():
  i01.mouth.speak("that was fun")
  i01.moveHead(90,90,80,90,75)
  i01.moveArm("left",5,90,30,10)
  i01.moveArm("right",5,90,30,10)
  i01.moveHand("left",2,2,2,2,2,90)
  i01.moveHand("right",2,2,2,2,2,90)

def heard(data):
    
    if (data == "sorry"):
        x = (random.randint(1, 3))
        if x == 1:
            i01.mouth.speak("no problems")
        if x == 2:
            i01.mouth.speak("it doesn't matter")
        if x == 3:
            i01.mouth.speak("it's okay")

    if (data == "nice"):
        x = (random.randint(1, 3))
        if x == 1:
            i01.mouth.speak("I know")
        if x == 2:
            i01.mouth.speak("yes, indeed")
        if x == 3:
            i01.mouth.speak("you are damn right")

    if (data == "hello"):
        hello()
        relax()

    if (data == "bye bye"):
        i01.mouth.speak("see you soon")
        global helvar
        helvar = 1
        x = (random.randint(1, 2))
        if x == 1:
            i01.mouth.speak("i'm looking forward to see you again")
        if x == 2:
            i01.mouth.speak("goodbye")

    if (data == "thank you"):
        x = (random.randint(1, 3))
        if x == 1:
            i01.mouth.speak("you are welcome")
        if x == 2:
            i01.mouth.speak("my pleasure")
        if x == 3:
            i01.mouth.speak("it's okay")

    if (data == "thanks"):
        x = (random.randint(1, 2))
        if x == 1:
            i01.mouth.speak("it's okay")
        if x == 2:
            i01.mouth.speak("sure")

    if (data == "how do you do"):
        if helvar <= 2:
            i01.mouth.speak("I'm fine thank you")
            global helvar
            helvar += 1
        elif helvar == 3:
            i01.mouth.speak("you have already said that at least twice")
            i01.moveArm("left",43,88,22,10)
            i01.moveArm("right",20,90,30,10)
            i01.moveHand("left",0,0,0,0,0,119)
            i01.moveHand("right",0,0,0,0,0,119)
            sleep(2)
            relax()
            global helvar
            helvar += 1
        elif helvar == 4:
            i01.mouth.speak("what is your problem stop saying how do you do all the time")
            i01.moveArm("left",30,83,22,10)
            i01.moveArm("right",40,85,30,10)
            i01.moveHand("left",130,180,180,180,180,119)
            i01.moveHand("right",130,180,180,180,180,119)
            sleep(2)
            relax()
            global helvar
            helvar += 1
        elif helvar == 5:
            i01.mouth.speak("i will ignore you if you say how do you do one more time")
            unhappy()
            sleep(4)
            relax()
            global helvar
            helvar += 1

    if (data == "i love you"):
        i01.mouth.speak("i love you too")
        surrender()
        sleep(1)
        relax()

def startkinect():
    i01.leftArm.shoulder.map(0,180,-25,105)
    i01.rightArm.shoulder.map(0,180,-30,100)
    i01.copyGesture(True)

def offkinect():
    i01.leftArm.shoulder.map(0,180,0,180)
    i01.rightArm.shoulder.map(0,180,0,180)
    i01.copyGesture(False)
    rest()

def trackHumans():
     i01.headTracking.faceDetect()
     i01.eyesTracking.faceDetect()
     fullspeed()

def trackPoint():
     i01.headTracking.startLKTracking()
     i01.eyesTracking.startLKTracking()
     fullspeed()

def stopTracking():
     i01.headTracking.stopTracking()
     i01.eyesTracking.stopTracking()

def takethis():
  fullspeed()
  i01.moveHead(58,96,82,78,72)
  i01.moveArm("left",13,45,95,10)
  sleep(.5)
  i01.moveArm("right",5,90,30,10)
  sleep(.5)
  i01.moveHand("left",2,2,2,2,2,15)
  i01.moveHand("right",81,66,82,60,105,113)
  sleep(.5)
  i01.moveTorso(79,90,90)
  sleep(3)
  closelefthand()
  sleep(2)
  isitaball()

def fistHips():
# changed 4-28-2015
# head rotatehead, neck, eyeX, eyeY, jaw
# hand thumb, index,  majeure,  ring,  pinky, wrist
# arm bicep, rotate, rotate shoulder, omoplate
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
  i01.moveTorso(50,50,90)
  sleep(4)
  i01.moveTorso(130,140,90)
  sleep(4)
  i01.moveTorso(90,90,90)
  
def turnLeft():
# changed 5-31-2015
# head rotatehead, neck, eyeX, eyeY, jaw
# hand thumb, index,  majeure,  ring,  pinky, wrist
# arm bicep, rotate, rotate shoulder, omoplate
  i01.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
  i01.setHeadSpeed(1.0, 1.0)
  i01.setTorsoSpeed(0.80, 0.80, 1.0)
  i01.moveTorso(90,170,90)
  
def turnRight():
# changed 5-31-2015
# head rotatehead, neck, eyeX, eyeY, jaw
# hand thumb, index,  majeure,  ring,  pinky, wrist
# arm bicep, rotate, rotate shoulder, omoplate
  i01.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
  i01.setHeadSpeed(1.0, 1.0)
  i01.setTorsoSpeed(0.80, 0.80, 1.0)
  i01.moveTorso(90,10,90)
  
def unhappy():
  i01.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
  i01.setHeadSpeed(1.0, 1.0)
  i01.setTorsoSpeed(1.0, 1.0, 1.0)
  i01.moveHead(85,40,80,90,78)
  i01.moveArm("left",79,42,23,41)
  sleep(.5)
  i01.moveArm("right",71,40,14,39)
  sleep(.5)
  i01.moveHand("left",180,180,180,180,180,47)
  i01.moveHand("right",99,130,152,154,145,180)
  sleeep(.5)
  i01.moveTorso(90,90,90)

def rest():
# changed 4-28-2015
# head rotatehead, neck, eyeX, eyeY, jaw
# hand thumb, index,  majeure,  ring,  pinky, wrist
# arm bicep, rotate, rotate shoulder, omoplate
  i01.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
  i01.setHeadSpeed(0.9, 0.9)
  i01.setTorsoSpeed(0.90, 0.90, 1.0)
  i01.moveHead(90,65,82,78,76)
  sleep(.5)
  i01.moveArm("left",5,90,30,10)
  sleep(.5)
  i01.moveArm("right",5,90,30,20)
  sleep(.5)
  i01.moveHand("left",1,1,1,1,1,90)
  sleep(.5)
  i01.moveHand("right",1,1,1,1,1,90)
  sleep(.5)
  i01.moveTorso(90,90,90)
  i01.mouth.speak("resting")

def fullspeed():
  i01.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
  i01.setHeadSpeed(1.0, 1.0)
  i01.setTorsoSpeed(1.0, 1.0, 1.0)

def delicategrab():
  i01.setHandSpeed("left", 0.70, 0.60, 1.0, 1.0, 1.0, 1.0)
  i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
  i01.setHeadSpeed(0.65, 0.75)
  i01.moveHead(21,98)
  sleep(.5)
  i01.moveArm("left",30,72,77,10)
  sleep(.5)
  i01.moveArm("right",0,91,28,17)
  sleep(.5)
  i01.moveHand("left",180,130,4,0,0,180)
  i01.moveHand("right",86,51,133,162,153,180)

def perfect():
# changed 4-28-2015
# head rotatehead, neck, eyeX, eyeY, jaw
# hand thumb, index,  majeure,  ring,  pinky, wrist
# arm bicep, rotate, rotate shoulder, omoplate
  i01.setHandSpeed("left", 0.80, 0.80, 1.0, 1.0, 1.0, 1.0)
  i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("left", 0.85, 0.85, 0.85, 0.95)
  i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
  i01.setHeadSpeed(0.65, 0.75)
  i01.moveHead(88,79)
  i01.moveArm("left",89,75,93,11)
  sleep(.5)
  i01.moveArm("right",0,91,28,17)
  sleep(.5)
  i01.moveHand("left",130,160,83,40,0,34)
  i01.moveHand("right",86,51,133,162,153,180)

def releasedelicate():
  i01.setHandSpeed("left", 0.60, 0.60, 1.0, 1.0, 1.0, 1.0)
  i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("left", 0.75, 0.75, 0.75, 0.95)
  i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
  i01.setHeadSpeed(0.65, 0.75)
  i01.moveHead(20,98)
  sleep(.5)
  i01.moveArm("left",30,72,64,10)
  sleep(.5)
  i01.moveArm("right",0,91,28,17)
  sleep(.5)
  i01.moveHand("left",101,74,66,58,44,180)
  sleep(.5)
  i01.moveHand("right",86,51,133,162,153,180)

def grabthebottle():
  i01.setHandSpeed("left", 1.0, 0.80, 0.80, 0.80, 1.0, 0.80)
  i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
  i01.setHeadSpeed(0.90, 0.80)
  i01.moveHead(20,88)
  i01.moveArm("left",77,85,45,15)
  i01.moveArm("right",5,90,30,10)
  i01.moveHand("left",180,138,140,164,180,60)
  i01.moveHand("right",0,0,0,0,0,90)

def grabtheglass():
  i01.setHandSpeed("left", 0.60, 0.60, 1.0, 1.0, 1.0, 1.0)
  i01.setHandSpeed("right", 1.0, 0.60, 0.60, 1.0, 1.0, 0.70)
  i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
  i01.setHeadSpeed(0.65, 0.65)
  i01.moveHead(20,68)
  i01.moveArm("left",77,85,45,15)
  i01.moveArm("right",48,91,72,10)
  i01.moveHand("left",180,138,140,164,180,60)
  i01.moveHand("right",140,112,127,105,143,133)

def poorbottle():
  i01.setHandSpeed("left", 0.60, 0.60, 0.60, 0.60, 0.60, 0.60)
  i01.setHandSpeed("right", 0.60, 0.80, 0.60, 0.60, 0.60, 0.60)
  i01.setArmSpeed("left", 0.60, 0.60, 0.60, 0.60)
  i01.setArmSpeed("right", 0.60, 0.60, 0.60, 0.60)
  i01.setHeadSpeed(0.65, 0.65)
  i01.moveHead(0,92)
  i01.moveArm("left",58,40,95,55)
  i01.moveArm("right",90,66,34,10)
  i01.moveHand("left",180,140,150,164,180,0)
  i01.moveHand("right",145,112,127,105,143,133)

def givetheglass():
  sleep(2)
  i01.setHandSpeed("left", 0.60, 0.60, 0.60, 0.60, 0.60, 0.60)
  i01.setHandSpeed("right", 0.60, 0.80, 0.60, 0.60, 0.60, 0.60)
  i01.setArmSpeed("left", 0.60, 1.0, 0.60, 0.60)
  i01.setArmSpeed("right", 0.60, 0.60, 0.60, 0.60)
  i01.setHeadSpeed(0.65, 0.65)
  i01.moveHead(84,79)
  i01.moveArm("left",77,75,45,17)
  i01.moveArm("right",21,80,77,10)
  i01.moveHand("left",109,138,180,164,180,60)
  i01.moveHand("right",102,86,105,105,143,133)
  i01.mouth.speakBlocking("Hello please take the glass")
  sleep(1)

def takeball():
  i01.setHandSpeed("right", 0.85, 0.75, 0.75, 0.75, 0.85, 0.75)
  i01.setArmSpeed("right", 0.85, 0.85, 0.85, 0.85)
  i01.setHeadSpeed(0.65, 0.65)
  i01.setTorsoSpeed(0.75, 0.75, 1.0)
  i01.moveHead(30,70,78,80,13)
  i01.moveArm("left",5,84,16,15)
  sleep(.5)
  i01.moveArm("right",6,73,76,16)
  sleep(.5)
  i01.moveHand("left",50,50,40,20,20,90)
  i01.moveHand("right",180,125,130,3,0,11)
  i01.moveTorso(101,100,90)

def keepball():
  i01.setHandSpeed("left", 0.65, 0.65, 0.65, 0.65, 0.65, 1.0)
  i01.setHandSpeed("right", 0.65, 0.65, 0.65, 0.65, 0.65, 1.0)
  i01.setArmSpeed("right", 0.75, 0.85, 0.95, 0.85)
  i01.setArmSpeed("left", 0.75, 0.85, 0.95, 0.85)
  i01.setHeadSpeed(0.65, 0.65)
  i01.setTorsoSpeed(0.75, 0.75, 1.0)
  i01.moveHead(20,70)
  i01.moveArm("left",5,84,16,15)
  i01.moveArm("right",54,77,55,16)
  i01.moveHand("left",50,50,40,20,20,90)
  i01.moveHand("right",180,125,130,3,0,11)
  i01.moveTorso(90,90,90)

def approachlefthand():
  i01.setHandSpeed("right", 0.75, 0.75, 0.75, 0.75, 0.75, 0.65)
  i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("right", 0.25, 0.25, 0.25, 0.25)
  i01.setHeadSpeed(0.65, 0.65)
  i01.setTorsoSpeed(0.75, 0.75, 1.0)
  i01.moveHead(20,84,78,80,13)
  i01.moveArm("left",67,52,62,23)
  i01.moveArm("right",55,61,45,16)
  i01.moveHand("left",130,50,40,180,180,0)
  i01.moveHand("right",180,125,130,3,0,11)
  i01.moveTorso(90,85,90)
  sleep(4)
  
def uselefthand():
  i01.setHandSpeed("right", 0.75, 0.75, 0.75, 0.75, 0.75, 0.65)
  i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("right", 0.25, 0.25, 0.25, 0.25)
  i01.setHeadSpeed(0.65, 0.65)
  i01.moveHead(20,84,78,80,13)
  i01.moveArm("left",65,52,59,23)
  i01.moveArm("right",82,61,50,16)
  i01.moveHand("left",140,50,40,180,180,0)
  i01.moveHand("right",140,125,130,3,0,11)
  sleep(4)

def more():
  i01.setHandSpeed("right", 0.75, 0.75, 0.75, 0.75, 0.75, 0.65)
  i01.setArmSpeed("left", 0.85, 0.85, 0.85, 0.95)
  i01.setArmSpeed("right", 0.75, 0.65, 0.65, 0.65)
  i01.setHeadSpeed(0.65, 0.65)
  i01.moveHead(16,84,78,80,13)
  i01.moveArm("left",63,52,59,23)
  i01.moveArm("right",82,60,50,16)
  i01.moveHand("left",140,148,180,180,180,0)
  i01.moveHand("right",80,114,88,3,0,11)
  sleep(3)

def handdown():
  i01.setHandSpeed("left", 0.75, 0.75, 0.75, 0.75, 0.75, 0.75)
  i01.setHandSpeed("right", 0.70, 0.70, 0.70, 0.70, 0.70, 1.0)
  i01.moveHead(16,84,78,80,13)
  i01.moveArm("left",66,52,59,23)
  i01.moveArm("right",59,60,50,16)
  i01.moveHand("left",140,148,180,180,180,0)
  i01.moveHand("right",54,95,66,3,0,11)
  sleep(2)

def isitaball():
  i01.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("right", 0.75, 0.85, 0.95, 0.85)
  i01.setArmSpeed("left", 0.75, 0.85, 0.90, 0.85)
  i01.setHeadSpeed(0.65, 0.75)
  i01.moveHead(90,83,78,80,13)
  i01.moveArm("left",70,59,95,15)
  i01.moveArm("right",12,74,33,15)
  i01.moveHand("left",170,150,180,180,180,164)
  i01.moveHand("right",105,81,78,57,62,105)

def putitdown():
  i01.setHandSpeed("left", 0.90, 0.90, 0.90, 0.90, 0.90, 0.90)
  i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("right", 0.75, 0.85, 0.95, 0.85)
  i01.setArmSpeed("left", 0.75, 0.85, 0.95, 0.85)
  i01.setHeadSpeed(0.75, 0.75)
  i01.moveHead(20,99)
  i01.moveArm("left",5,45,87,31)
  i01.moveArm("right",5,82,33,15)
  i01.moveHand("left",147,130,135,34,34,35)
  i01.moveHand("right",20,40,40,30,30,72)

def dropit():
  i01.setHandSpeed("left", 0.85, 0.85, 0.85, 0.85, 0.85, 0.85)
  i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("right", 0.75, 0.85, 0.95, 0.85)
  i01.setArmSpeed("left", 0.75, 0.85, 1.0, 0.85)
  i01.setHeadSpeed(0.75, 0.75)
  i01.moveHead(20,99)
  i01.moveArm("left",5,45,87,31)
  i01.moveArm("right",5,82,33,15)
  sleep(3)
  i01.moveHand("left",60,61,67,34,34,35)
  i01.moveHand("right",20,40,40,30,30,72)

def removeleftarm():
  i01.setHandSpeed("left", 0.85, 0.85, 0.85, 0.85, 0.85, 0.85)
  i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("right", 0.75, 0.85, 0.95, 0.85)
  i01.setArmSpeed("left", 0.95, 0.65, 0.75, 0.75)
  i01.setHeadSpeed(0.75, 0.75)
  i01.moveHead(20,100)
  i01.moveArm("left",71,94,41,31)
  i01.moveArm("right",5,82,28,15)
  i01.moveHand("left",60,43,45,34,34,35)
  i01.moveHand("right",20,40,40,30,30,72)

def armsUp():
# changed 4-28-2015
# head rotatehead, neck, eyeX, eyeY, jaw
# hand thumb, index,  majeure,  ring,  pinky, wrist
# arm bicep, rotate, rotate shoulder, omoplate
    i01.setHeadSpeed(1.0,1.0)
    i01.moveHead(180,86)
    sleep(1)
    i01.setHandSpeed("left",0.90,0.90,0.90,0.90,0.90,1.0)
    i01.setHandSpeed("right",0.90,0.90,0.90,0.90,0.90,1.0)
    i01.moveHand("left",170,170,170,170,170,33)
    i01.moveHand("right",170,170,170,170,170,180)
    sleep(3)
    i01.setArmSpeed("left",1.0,1.0,1.0,1.0)
    i01.setArmSpeed("right",1.0,1.0,1.0,1.0)
    i01.setTorsoSpeed(1.0,1.0,1.0)
    i01.moveArm("left",90,90,170,20)
    sleep(1)
    i01.moveArm("right",90,90,173,20)
    sleep(9)
    i01.setHandSpeed("left",1.0,1.0,1.0,1.0,1.0,1.0)
    i01.setHandSpeed("right",1.0,1.0,1.0,1.0,1.0,1.0)
    i01.moveHead(180,86)
    sleep(1)
    i01.moveArm("left",5,90,180,10)
    sleep(1)
    i01.moveArm("right",5,90,173,10)
    sleep(1)
    i01.moveHand("left",2,2,2,2,2,33)
    i01.moveHand("right",2,2,2,2,2,180)
    sleep(1)
    i01.moveTorso(90,90,90)
 
def relax():
# changed 4-28-2015
# head rotatehead, neck, eyeX, eyeY, jaw
# hand thumb, index,  majeure,  ring,  pinky, wrist
# arm bicep, rotate, rotate shoulder, omoplate
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
  i01.mouth.speak("relaxing")
  
def handopen():
# changed 4-28-2015
# hand thumb, index,  majeure,  ring,  pinky, wrist
  i01.setHandSpeed("left", 0.85, 0.85, 0.85, 0.85, 0.85, 0.85)
  i01.setHandSpeed("right", 0.85, 0.85, 0.85, 0.85, 0.85, 0.85)
  i01.moveHand("left",0,0,0,0,0)
  i01.moveHand("right",0,0,0,0,0)

def handclose():
# changed 4-28-2015
# hand thumb, index,  majeure,  ring,  pinky, wrist
  i01.setHandSpeed("left", 0.85, 0.85, 0.85, 0.85, 0.85, 0.85)
  i01.setHandSpeed("right", 0.85, 0.85, 0.85, 0.85, 0.85, 0.85)
  i01.moveHand("left",180,180,180,180,180)
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
  i01.setHandSpeed("left", 0.70, 0.70, 0.70, 0.70, 0.70, 0.70)
  i01.moveHand("left",180,180,180,180,180)

def closerighthand():
# changed 4-28-2015
# hand thumb, index,  majeure,  ring,  pinky, wrist
  i01.setHandSpeed("right", 0.70, 0.70, 0.70, 0.70, 0.70, 0.70)
  i01.moveHand("right",180,180,180,180,180)

def surrender():
  i01.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("right", 0.75, 0.85, 0.95, 0.85)
  i01.setArmSpeed("left", 0.75, 0.85, 0.95, 0.85)
  i01.setHeadSpeed(0.65, 0.65)
  i01.moveHead(90,90,78,100,38)
  i01.moveArm("left",90,139,15,79)
  i01.moveArm("right",90,145,37,79)
  i01.moveHand("left",50,28,30,10,10,76)
  i01.moveHand("right",10,10,10,10,10,139)

def pictureleftside():
# rotatehead 15-150, neck 15-150, eyeX 20-80, eyeY, jaw 10-70
# hand right thumb 110, index 100, majeure 120, ring 115, pinky 115, wrist 90
  i01.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setHandSpeed("right", 0.85, 0.85, 0.85, 0.85, 0.85, 0.85)
  i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("left", 0.75, 0.85, 0.95, 0.85)
  i01.setHeadSpeed(0.65, 0.65)
  i01.moveHead(170,90)
  i01.setTorsoSpeed(0.80, 0.80, 1.0)
  i01.moveTorso(90,120,90)
  sleep(3)
  i01.moveArm("left",90,105,24,75)
  sleep(.5)
  i01.moveArm("right",5,82,28,15)
  sleep(.5)
  i01.moveHand("left",50,86,97,74,106,119)
  i01.moveHand("right",81,65,82,60,105,113)

def picturerightside():
  i01.setHandSpeed("left", 0.85, 0.85, 0.85, 0.85, 0.85, 0.85)
  i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("right", 0.85, 0.85, 0.85, 0.85)
  i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
  i01.setHeadSpeed(0.65, 0.65)
  i01.moveHead(20,40)
  sleep(.5)
  i01.setTorsoSpeed(0.80, 0.80, 1.0)
  i01.moveTorso(90,30,90)
  sleep(3)
  i01.moveArm("left",5,94,28,15)
  sleep(.5)
  i01.moveArm("right",90,115,23,68)
  i01.moveHand("left",42,58,87,55,71,35)
  i01.moveHand("right",10,112,95,91,125,45)

def picturebothside():
  i01.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
  i01.setHeadSpeed(0.65, 0.65)
  i01.moveHead(109,90)
  i01.moveJaw(50)
  i01.moveArm("left",90,105,24,75)
  i01.moveArm("right",90,115,23,68)
  i01.moveHand("left",50,86,97,74,106,119)
  i01.moveHand("right",10,112,95,91,125,45)

def lookrightside():
  i01.setHeadSpeed(0.70, 0.70)
  i01.setTorsoSpeed(0.75, 0.85, 1.0)
  i01.moveHead(70,40)
  i01.moveTorso(120,30,90)

def lookleftside():
  i01.setHeadSpeed(0.70, 0.70)
  i01.setTorsoSpeed(0.75, 0.85, 1.0)
  i01.moveHead(85,140)
  i01.moveTorso(80,150,90)

def lookback():
  i01.setHeadSpeed(0.90, 0.90)
  i01.setTorsoSpeed(0.85, 0.85, 1.0)
# want to look left and down
  i01.moveHead(85,150)
  sleep(3)
  i01.moveTorso(80,180,90)
  sleep(3)
  i01.mouth.speak("I see a Inmoov shirt   and    My robot lab shirt")
  sleep(1)
  i01.mouth.speak("life is good")
  sleep(3)
  i01.moveTorso(90,90,90)
  sleep(.5)
  i01.moveHead(110,90)
  
def lookinmiddle():
  i01.setHeadSpeed(0.70, 0.70)
  i01.setTorsoSpeed(0.75, 0.75, 1.0)
  i01.moveHead(85,86)
  i01.moveTorso(90,90,90)

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
# next line changed jhs
  i01.moveArm("left",170,150,48,170)
# gaels  i01.moveArm("left",90,139,48,75)
  i01.moveArm("right",71,40,14,43)
  i01.moveHand("left",180,180,180,180,180,83)
  i01.moveHand("right",99,130,152,154,145,21)
  i01.moveTorso(120,130,90)
  sleep(4)
  i01.mouth.speakBlocking("Looks good, doesn't it")
  sleep(2)
  i01.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
  i01.setHeadSpeed(0.85, 0.85)
  i01.setTorsoSpeed(0.75, 0.75, 1.0)
  i01.moveHead(90,45)
  i01.moveArm("left",44,46,20,39)
# next line changed jhs
  i01.moveArm("right",170,165,58,160)
# gaels    i01.moveArm("right",90,145,58,74)
  i01.moveHand("left",180,180,180,180,180,83)
  i01.moveHand("right",99,130,152,154,145,21)
  i01.moveTorso(60,75,90)
  sleep(3)
  i01.mouth.speakBlocking("not bad either, don't you think")
  sleep(4)
  relax()

def shakehand():
  # When sphinx recognizes "shake hand" this method is called.
  ##rest
  i01.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
  i01.setHeadSpeed(1.0, 1.0)
  i01.setTorsoSpeed(1.0, 1.0, 1.0)
  i01.moveHead(80,86,82,78,8)
  i01.moveArm("left",5,90,30,10)
  i01.moveArm("right",5,90,30,10)
  i01.moveHand("left",2,2,2,2,2,90)
  i01.moveHand("right",2,2,2,2,2,90)
  i01.moveTorso(90,90,90)
  sleep(1)
##move arm and hand
  i01.setHandSpeed("left", 0.65, 0.65, 0.65, 0.65, 0.65, 1.0)
  i01.setHandSpeed("right", 0.65, 0.65, 0.65, 0.65, 0.65, 1.0)
  i01.setArmSpeed("right", 0.75, 0.85, 0.95, 0.85)
  i01.setArmSpeed("left", 0.75, 0.85, 0.95, 0.85)
  i01.setHeadSpeed(0.65, 0.65)
  i01.setTorsoSpeed(0.75, 0.75, 1.0)
  i01.moveHead(39,70,78,80,8)
  i01.moveArm("left",5,84,16,15)
  i01.moveArm("right",6,73,65,16)
  i01.moveHand("left",50,50,40,20,20,90)
  i01.moveHand("right",50,50,40,20,20,90)
  i01.moveTorso(101,100,90)
  sleep(1)
##close the hand
  i01.setHandSpeed("left", 0.65, 0.65, 0.65, 0.65, 0.65, 1.0)
  i01.setHandSpeed("right", 0.85, 0.85, 0.85, 0.85, 0.85, 1.0)
  i01.setArmSpeed("right", 0.75, 0.85, 0.95, 0.85)
  i01.setArmSpeed("left", 0.75, 0.85, 0.75, 0.85)
  i01.setHeadSpeed(0.65, 0.65)
  i01.setTorsoSpeed(0.75, 0.75, 1.0)
  i01.moveHead(39,70,78,80,8)
  i01.moveArm("left",5,84,16,15)
  i01.moveArm("right",6,73,62,16)
  i01.moveHand("left",50,50,40,20,20,90)
  i01.moveHand("right",180,126,120,145,168,77)
  i01.moveTorso(101,100,90)
  sleep(3)
##shake hand up
  i01.setHandSpeed("left", 0.65, 0.65, 0.65, 0.65, 0.65, 1.0)
  i01.setHandSpeed("right", 0.85, 0.85, 0.85, 0.85, 0.85, 1.0)
  i01.setArmSpeed("right", 0.75, 0.85, 0.95, 0.85)
  i01.setArmSpeed("left", 0.75, 0.85, 0.95, 0.85)
  i01.setHeadSpeed(0.45, 0.45)
  i01.setTorsoSpeed(0.75, 0.75, 1.0)
  i01.moveHead(85,90,78,80,8)
  i01.moveArm("left",5,84,16,15)
  i01.moveArm("right",6,73,70,16)
  i01.moveHand("left",50,50,40,20,20,90)
  i01.moveHand("right",180,126,120,145,168,77)
  i01.moveTorso(101,100,90)
  sleep(1)
  ##shake hand down
  x = (random.randint(1, 4))
  if x == 1:
    i01.mouth.speak("Please to meet you")
  elif x == 2:
    i01.mouth.speak("carefull my hand is made out of plastic")
  elif x == 3:
    i01.mouth.speak("I am happy to shake a human hand")
  else:
    i01.mouth.speak("it is a pleasure to meet you ")
    
  i01.mouth.speak("please to meet you")
  i01.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("right", 0.75, 0.75, 0.95, 0.85)
  i01.setHeadSpeed(1.0, 1.0)
  i01.setTorsoSpeed(1.0, 1.0, 1.0)
  i01.moveHead(85,90,78,80,8)
  i01.moveArm("left",5,84,16,15)
  i01.moveArm("right",6,73,60,16)
  i01.moveHand("left",50,50,40,20,20,90)
  i01.moveHand("right",180,126,120,145,168,77)
  i01.moveTorso(101,100,90)
  sleep(1)
  ##shake hand up
  i01.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("right", 0.75, 0.75, 0.95, 0.85)
  i01.setHeadSpeed(1.0, 1.0)
  i01.setTorsoSpeed(1.0, 1.0, 1.0)
  i01.moveHead(85,90,78,80,8)
  i01.moveArm("left",5,84,16,15)
  i01.moveArm("right",6,73,75,16)
  i01.moveHand("left",50,50,40,20,20,90)
  i01.moveHand("right",180,126,120,145,168,77)
  i01.moveTorso(101,100,90)
  sleep(1)
  ##shake hand down
  i01.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("right", 0.75, 0.75, 0.95, 0.85)
  i01.setHeadSpeed(0.45, 0.45)
  i01.setTorsoSpeed(1.0, 1.0, 1.0)
  i01.moveHead(82,88,78,80,8)
  i01.moveArm("left",5,84,16,15)
  i01.moveArm("right",6,73,62,16)
  i01.moveHand("left",50,50,40,20,20,90)
  i01.moveHand("right",180,126,120,145,168,77)
  i01.moveTorso(101,100,90)
  sleep(2)
  ## release hand
  i01.setHandSpeed("left", 0.65, 0.65, 0.65, 0.65, 0.65, 1.0)
  i01.setHandSpeed("right", 0.95, 0.95, 0.95, 0.95, 0.95, 1.0)
  i01.setArmSpeed("right", 0.75, 0.75, 0.95, 0.85)
  i01.setArmSpeed("left", 0.75, 0.85, 0.95, 0.85)
  i01.setHeadSpeed(0.45, 0.45)
  i01.setTorsoSpeed(0.75, 0.55, 1.0)
  i01.moveHead(39,70,78,80,8)
  i01.moveArm("left",5,84,16,15)
  i01.moveArm("right",6,73,62,16)
  i01.moveHand("left",50,50,40,20,20,77)
  i01.moveHand("right",20,50,40,20,20,90)
  i01.moveTorso(101,100,90)
  sleep(1)
  ##relax
  i01.setHandSpeed("left", 0.85, 0.85, 0.85, 0.85, 0.85, 0.85)
  i01.setHandSpeed("right", 0.85, 0.85, 0.85, 0.85, 0.85, 0.85)
  i01.setArmSpeed("right", 0.75, 0.85, 0.65, 0.85)
  i01.setArmSpeed("left", 0.95, 0.65, 0.75, 0.75)
  i01.setHeadSpeed(0.75, 0.75)
  i01.setTorsoSpeed(0.75, 0.75, 1.0)
  i01.moveHead(79,100,80,90,13)
  i01.moveArm("left",5,84,28,15)
  i01.moveArm("right",5,90,30,10)
  i01.moveHand("left",92,33,37,71,66,25)
  i01.moveHand("right",10,50,40,20,20,113)
  i01.moveTorso(90,90,90)

# head rotatehead, neck, eyeX, eyeY, jaw
# hand thumb, index,  majeure,  ring,  pinky, wrist
# arm bicep, rotate, shoulder, omoplate
# torso topStom 95-140
def powerdown():
#        rest()
        i01.powerDown()
        sleep(1)       
        ear.pauseListening()
#        i01.mouth.speakBlocking()
#        sleep(1)
#        rightSerialPort.digitalWrite(53, Arduino.LOW)
#        leftSerialPort.digitalWrite(53, Arduino.LOW)
        ear.lockOutAllGrammarExcept("power up")
        sleep(2)
        ear.resumeListening()
        mega.digitalReadPollingStart(readDigitalPin)
        
def powerup():
#       sleep(1)        
#        ear.pauseListening()
#        rightSerialPort.digitalWrite(53, Arduino.HIGH)
#        leftSerialPort.digitalWrite(53, Arduino.HIGH)
        i01.mouth.speakBlocking("I was sleeping")
        i01.powerUp()
        lookrightside()
        sleep(1)
        lookleftside()
        sleep(2)
        relax()
#        ear.clearLock()
#        sleep(2)
        ear.resumeListening()

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
     ear.pauseListening()
     sleep(1)

     for w in range(0,3):
          i01.setHandSpeed("left", 0.60, 0.60, 1.0, 1.0, 1.0, 1.0)
          i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 0.60)
          i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
          i01.setArmSpeed("right", 0.60, 1.0, 1.0, 1.0)
          i01.setHeadSpeed(0.65, 0.75)
          i01.moveHead(83,98)
          i01.moveArm("left",78,48,37,11)
          i01.moveArm("right",90,157,47,75)
          i01.moveHand("left",112,111,105,102,81,10)
          i01.moveHand("right",3,0,62,41,117,94)

          if w==1:
                     i01.setHandSpeed("left", 0.60, 0.60, 1.0, 1.0, 1.0, 1.0)
                     i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 0.60)
                     i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
                     i01.setArmSpeed("right", 0.65, 1.0, 1.0, 1.0)
                     i01.setHeadSpeed(0.65, 0.75)
                     i01.moveHead(83,70)
                     i01.mouth.speakBlocking("hello, my name is azuul")
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
                     ear.resumeListening()

def photo():
        i01.moveHead(87,60)
        i01.moveArm("left",78,48,37,11)
        i01.moveArm("right",46,147,5,75)
        i01.moveHand("left",138,52,159,106,120,90)
        i01.moveHand("right",80,65,94,63,70,140)

def beforehappy():
        i01.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
        i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
        i01.setArmSpeed("right", 0.85, 0.85, 0.85, 1.0)
        i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
        i01.setHeadSpeed(0.65, 0.65)
        i01.moveHead(84,88)
        i01.moveArm("left",5,82,36,11)
        i01.moveArm("right",74,112,61,29)
        i01.moveHand("left",0,88,135,94,96,90)
        i01.moveHand("right",81,79,118,47,0,90)

def happy():
     for w in range(0,3):
         sleep(1)
         i01.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
         i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
         i01.setArmSpeed("right", 0.85, 0.85, 0.85, 1.0)
         i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
         i01.setHeadSpeed(0.65, 0.65)
         i01.moveHead(84,88)
         i01.moveArm("left",5,82,36,10)
         i01.moveArm("right",74,112,61,29)
         i01.moveHand("left",0,88,135,94,96,90)
         i01.moveHand("right",81,79,118,47,0,90)
         sleep(1)
         if w==1:
                     i01.mouth.speakBlocking("happy birthday grog")
                     i01.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
                     i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
                     i01.setArmSpeed("right", 0.85, 0.85, 0.85, 1.0)
                     i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
                     i01.setHeadSpeed(0.65, 0.65)
                     i01.moveHead(42,76)
                     i01.moveArm("left",5,90,30,10)
                     i01.moveArm("right",74,70,61,10)
                     i01.moveHand("left",0,0,0,0,0,90)
                     i01.moveHand("right",81,79,118,47,0,90)
                     sleep(5)
                     ear.resumeListening()

def about():
        sleep(1)
        ear.pauseListening()
        sleep(1)
        i01.setArmSpeed("right", 0.1, 0.1, 0.2, 0.2);
        i01.setArmSpeed("left", 0.1, 0.1, 0.2, 0.2);
        i01.setHeadSpeed(0.2,0.2)
        i01.moveArm("right", 64, 94, 10, 10);
        i01.mouth.speakBlocking("I am the first life size humanoid robot you can 3D print and animate")
        i01.moveHead(65,66)
        i01.moveArm("left", 64, 104, 10, 11);
        i01.moveArm("right", 44, 84, 10, 11);
        i01.mouth.speakBlocking("my designer creator is Gael Langevin a French sculptor, model maker")
        i01.moveHead(75,86)
        i01.moveArm("left", 54, 104, 10, 11);
        i01.moveArm("right", 64, 84, 10, 20);
        i01.mouth.speakBlocking("who has released my files  to the opensource 3D world.")
        i01.moveHead(65,96)
        i01.moveArm("left", 44, 94, 10, 20);
        i01.moveArm("right", 54, 94, 20, 11);
        i01.mouth.speakBlocking("this is where my builder downloaded my files.")
        i01.moveHead(75,76)
        i01.moveArm("left", 64, 94, 20, 11);
        i01.moveArm("right", 34, 94, 10, 11);
        i01.mouth.speakBlocking("after five hundred hours of printing, four kilos of plastic, twenty seven hobby servos, blood and sweat.I was brought to life") # should be " i was borght to life."
        i01.moveHead(65,86)
        i01.moveArm("left", 24, 94, 10, 11);
        i01.moveArm("right", 24, 94, 10, 11);
        i01.mouth.speakBlocking("so if You have a 3D printer, some building skills, then you can build your own version of me") # mabe add in " alot of money"
        i01.moveHead(85,86)
        i01.moveArm("left", 5, 94, 20, 30);
        i01.moveArm("right", 24, 124, 10, 20);
        i01.mouth.speakBlocking("and if enough people build me, some day my kind could take over the world") # mabe add in " alot of money"
        i01.moveHead(75,96)
        i01.moveArm("left", 24, 104, 10, 11);
        i01.moveArm("right", 5, 94, 20, 30);
        i01.mouth.speakBlocking("I'm just kidding. i need some legs to get around, and i have to over come my  pyro-phobia, a fear of fire") # mabe add in " alot of money"
        i01.moveHead(75,96)
        i01.moveArm("left", 5, 94, 10, 11)
        i01.moveArm("right", 4, 94, 10, 11);
        i01.mouth.speakBlocking("so, until then. i will be humankind's humble servant")
        rest()
        i01.setArmSpeed("right", 1, 1, 1, 1);
        i01.setArmSpeed("left", 1, 1, 1, 1);
        i01.setHeadSpeed(1,1)
        sleep(1)
        ear.resumeListening()

def servos():
        ear.pauseListening()
        sleep(2)
        i01.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
        i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
        i01.setArmSpeed("right", 0.85, 0.85, 0.85, 0.85)
        i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
        i01.setHeadSpeed(0.65, 0.65)
        i01.moveHead(79,100)
        i01.moveArm("left",5,119,28,15)
        i01.moveArm("right",5,111,28,15)
        i01.moveHand("left",42,58,87,55,71,35)
        i01.moveHand("right",81,20,82,60,105,113)
        i01.mouth.speakBlocking("I currently have twenty seven  hobby servos installed in my body to give me life")
        i01.setHandSpeed("left", 0.85, 0.85, 0.85, 0.85, 0.85, 0.85)
        i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
        i01.setArmSpeed("right", 0.85, 0.85, 0.85, 0.85)
        i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
        i01.setHeadSpeed(0.65, 0.65)
        i01.moveHead(124,90)
        i01.moveArm("left",89,94,91,35)
        i01.moveArm("right",20,67,31,22)
        i01.moveHand("left",106,41,161,147,138,90)
        i01.moveHand("right",0,0,0,54,91,90)
        i01.mouth.speakBlocking("there's one servo  for moving my mouth up and down")
        sleep(1)
        i01.setHandSpeed("left", 0.85, 0.85, 1.0, 0.85, 0.85, 0.85)
        i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
        i01.setArmSpeed("right", 0.85, 0.85, 0.85, 0.85)
        i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
        i01.setHeadSpeed(0.65, 0.65)
        i01.moveHead(105,76);
        i01.moveArm("left",89,106,103,35);
        i01.moveArm("right",35,67,31,22);
        i01.moveHand("left",106,0,0,147,138,7);
        i01.moveHand("right",0,0,0,54,91,90);
        i01.mouth.speakBlocking("two for my eyes")
        sleep(0.2)
        i01.setHandSpeed("left", 0.85, 0.85, 1.0, 1.0, 1.0, 0.85)
        i01.moveHand("left",106,0,0,0,0,7);
        i01.mouth.speakBlocking("and two more for my head")
        sleep(0.5)
        i01.setHandSpeed("left", 0.85, 0.9, 0.9, 0.9, 0.9, 0.85)
        i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
        i01.setArmSpeed("right", 0.85, 0.85, 0.85, 0.85)
        i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
        i01.setHeadSpeed(0.65, 0.65)
        i01.moveHead(90,40);
        i01.moveArm("left",89,106,103,35);
        i01.moveArm("right",35,67,31,20);
        i01.moveHand("left",106,140,140,140,140,7);
        i01.moveHand("right",0,0,0,54,91,90);
        i01.mouth.speakBlocking("so i can look around")
        sleep(0.5)
        i01.setHeadSpeed(0.65, 0.65)
        i01.moveHead(105,125);
        i01.setArmSpeed("left", 0.9, 0.9, 0.9, 0.9)
        i01.moveArm("left",60,100,85,30);
        i01.mouth.speakBlocking("and see who's there")
        i01.setHeadSpeed(0.65, 0.65)
        i01.moveHead(40,56);
        sleep(0.5)
        i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
        i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
        i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0);
        i01.setArmSpeed("right", 0.5, 0.6, 0.5, 0.6);
        i01.moveArm("left",87,41,64,11)
        i01.moveArm("right",5,95,40,11)
        i01.moveHand("left",98,150,160,160,160,104)
        i01.moveHand("right",0,0,50,54,91,90);
        i01.mouth.speakBlocking("there's three servos  in each shoulder")
        i01.moveHead(40,67);
        sleep(2)
        i01.setHandSpeed("left", 0.8, 0.9, 0.8, 0.8, 0.8, 0.8)
        i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
        i01.setArmSpeed("right", 0.85, 0.85, 0.85, 0.85)
        i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
        i01.setHeadSpeed(0.8, 0.8)
        i01.moveHead(43,69)
        i01.moveArm("left",87,41,64,11)
        i01.moveArm("right",5,95,40,42)
        i01.moveHand("left",42,0,100,80,113,35)
        i01.moveHand("left",42,10,160,160,160,35)
        i01.moveHand("right",81,20,82,60,105,113)
        i01.mouth.speakBlocking("here is the first servo movement")
        sleep(1)
        i01.moveHead(37,60);
        i01.setHandSpeed("left", 1.0, 1.0, 0.9, 0.9, 1.0, 0.8)
        i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
        i01.moveArm("right",5,95,67,42)
        i01.moveHand("left",42,10,10,160,160,30)
        i01.mouth.speakBlocking("this is the second one")
        sleep(1)
        i01.moveHead(43,69);
        i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
        i01.moveArm("right",5,134,67,42)
        i01.moveHand("left",42,10,10,10,160,35)
        i01.mouth.speakBlocking("now you see the third")
        sleep(1)
        i01.setArmSpeed("right", 0.8, 0.8, 0.8, 0.8)
        i01.moveArm("right",20,90,45,16)
        i01.mouth.speakBlocking("they give me a more human like movement")
        sleep(1)
        i01.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
        i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0);
        i01.moveHead(43,72)
        i01.moveArm("left",90,44,66,11)
        i01.moveArm("right",90,100,67,26)
        i01.moveHand("left",42,80,100,80,113,35)
        i01.moveHand("right",81,0,82,60,105,69)
        i01.mouth.speakBlocking("but, i have only  one servo, to move each elbow")
        i01.setHandSpeed("left", 0.85, 0.85, 0.85, 0.85, 0.85, 0.85)
        i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
        i01.setArmSpeed("right", 0.85, 0.85, 0.85, 0.85)
        i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
        i01.setHeadSpeed(0.8, 0.8)
        i01.moveHead(45,62)
        i01.moveArm("left",72,44,90,11)
        i01.moveArm("right",90,95,68,15)
        i01.moveHand("left",42,0,100,80,113,35)
        i01.moveHand("right",81,0,82,60,105,0)
        i01.mouth.speakBlocking("that, leaves me, with one servo per wrist")
        i01.moveHead(40,60)
        i01.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
        i01.setHandSpeed("right", 0.9, 0.9, 0.9, 0.9, 0.9, 0.9)
        i01.moveArm("left",72,44,90,9)
        i01.moveArm("right",90,95,68,15)
        i01.moveHand("left",42,0,100,80,113,35)
        i01.moveHand("right", 10, 140,82,60,105,10)
        i01.mouth.speakBlocking("and one servo for each finger.")
        sleep(0.5)
        i01.moveHand("left",42,0,100,80,113,35)
        i01.moveHand("right", 50, 51, 15,23, 30,140);
        i01.mouth.speakBlocking("these servos are located in my forearms")
        i01.setHandSpeed("left", 0.8, 0.8, 0.8, 0.8,0.8, 0.8)
        i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
        i01.moveHand("left", 36, 52, 8,22, 20);
        i01.moveHand("right", 120, 147, 130,110, 125);
        removeleftarm()
        sleep(1)
        i01.mouth.speakBlocking("they are hooked up, by the use of tendons")
        i01.moveHand("left",10,20,30,40,60,150);
        i01.moveHand("right",110,137,120,100,105,130);
        i01.setHeadSpeed(1,1)
        i01.setArmSpeed("right", 1.0,1.0, 1.0, 1.0);
        i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0);
        relax()
        sleep(2)
        ear.resumeListening()

def howmanyfingersdoihave():
     ear.pauseListening()
     sleep(1)
     fullspeed()
     i01.moveHead(49,74)
     i01.moveArm("left",75,83,79,24)
     i01.moveArm("right",65,82,71,24)
     i01.moveHand("left",74,140,150,157,168,92)
     i01.moveHand("right",89,80,98,120,114,0)
     sleep(2)
     i01.moveHand("right",0,80,98,120,114,0)
     i01.mouth.speakBlocking("ten")

     sleep(.1)
     i01.moveHand("right",0,0,98,120,114,0)
     i01.mouth.speakBlocking("nine")

     sleep(.1)
     i01.moveHand("right",0,0,0,120,114,0)
     i01.mouth.speakBlocking("eight")

     sleep(.1)
     i01.moveHand("right",0,0,0,0,114,0)
     i01.mouth.speakBlocking("seven")

     sleep(.1)
     i01.moveHand("right",0,0,0,0,0,0)
     i01.mouth.speakBlocking("six")

     sleep(.5)
     i01.setHeadSpeed(.70,.70)
     i01.moveHead(40,105)
     i01.moveArm("left",75,83,79,24)
     i01.moveArm("right",65,82,71,24)
     i01.moveHand("left",0,0,0,0,0,180)
     i01.moveHand("right",0,0,0,0,0,0)
     sleep(0.1)
     i01.mouth.speakBlocking("and five makes eleven")

     sleep(0.7)
     i01.setHeadSpeed(0.7,0.7)
     i01.moveHead(40,50)
     sleep(0.5)
     i01.setHeadSpeed(0.7,0.7)
     i01.moveHead(49,105)
     sleep(0.7)
     i01.setHeadSpeed(0.7,0.8)
     i01.moveHead(40,50)
     sleep(0.7)
     i01.setHeadSpeed(0.7,0.8)
     i01.moveHead(49,105)
     sleep(0.7)
     i01.setHeadSpeed(0.7,0.7)
     i01.moveHead(90,85)
     sleep(0.7)
     i01.mouth.speakBlocking("eleven")
     i01.moveArm("left",70,75,70,20)
     i01.moveArm("right",60,75,65,20)
     sleep(1)
     i01.mouth.speakBlocking("that doesn't seem right")
     sleep(2)
     i01.mouth.speakBlocking("I think I better try that again")

     i01.moveHead(40,105)
     i01.moveArm("left",75,83,79,24)
     i01.moveArm("right",65,82,71,24)
     i01.moveHand("left",140,168,168,168,158,90)
     i01.moveHand("right",87,138,109,168,158,25)
     sleep(2)

     i01.moveHand("left",10,140,168,168,158,90)
     i01.mouth.speakBlocking("one")
     sleep(.1)


     i01.moveHand("left",10,10,168,168,158,90)
     i01.mouth.speakBlocking("two")
     sleep(.1)

     i01.moveHand("left",10,10,10,168,158,90)
     i01.mouth.speakBlocking("three")
     sleep(.1)
     i01.moveHand("left",10,10,10,10,158,90)

     i01.mouth.speakBlocking("four")
     sleep(.1)
     i01.moveHand("left",10,10,10,10,10,90)

     i01.mouth.speakBlocking("five")
     sleep(.1)
     i01.setHeadSpeed(0.65,0.65)
     i01.moveHead(53,65)
     i01.moveArm("right",48,80,78,11)
     i01.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
     i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
     i01.moveHand("left",10,10,10,10,10,90)
     i01.moveHand("right",10,10,10,10,10,25)
     sleep(1)
     i01.mouth.speakBlocking("and five makes ten")
     sleep(.5)
     i01.mouth.speakBlocking("there that's better")
     i01.moveHead(95,85)
     i01.moveArm("left",75,83,79,24)
     i01.moveArm("right",40,70,70,10)
     sleep(0.5)
     i01.mouth.speakBlocking("inmoov has ten fingers")
     sleep(0.5)
     i01.moveHead(90,90)
     i01.setHandSpeed("left", 0.8, 0.8, 0.8, 0.8, 0.8, 0.8)
     i01.setHandSpeed("right", 0.8, 0.8, 0.8, 0.8, 0.8, 0.8)
     i01.moveHand("left",140,140,140,140,140,60)
     i01.moveHand("right",140,140,140,140,140,60)
     sleep(1.0)
     i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
     i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
     i01.moveArm("left",5,90,30,11)
     i01.moveArm("right",5,90,30,11)
     sleep(0.5)
     relax()
     sleep(0.5)
     ear.resumeListening()

def studyball():
##keepball():
  i01.setHandSpeed("left", 0.65, 0.65, 0.65, 0.65, 0.65, 1.0)
  i01.setHandSpeed("right", 0.65, 0.65, 0.65, 0.65, 0.65, 1.0)
  i01.setArmSpeed("right", 0.75, 0.85, 0.95, 0.85)
  i01.setArmSpeed("left", 0.75, 0.85, 0.95, 0.85)
  i01.setHeadSpeed(0.65, 0.65)
  i01.setTorsoSpeed(0.75, 0.75, 1.0)
  i01.moveHead(20,70)
  i01.moveArm("left",5,84,16,15)
  i01.moveArm("right",54,77,55,16)
  i01.moveHand("left",50,50,40,20,20,90)
  i01.moveHand("right",180,125,130,3,0,11)
  i01.moveTorso(90,90,90)
  sleep(3)
##approachlefthand():
  i01.setHandSpeed("right", 0.75, 0.75, 0.75, 0.75, 0.75, 0.65)
  i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("right", 0.25, 0.25, 0.25, 0.25)
  i01.setHeadSpeed(0.65, 0.65)
  i01.setTorsoSpeed(0.75, 0.75, 1.0)
  i01.moveHead(20,84,78,80,13)
  i01.moveArm("left",67,52,62,23)
  i01.moveArm("right",55,61,45,16)
  i01.moveHand("left",130,50,40,180,180,0)
  i01.moveHand("right",180,125,130,3,0,11)
  i01.moveTorso(90,85,90)
  sleep(4)
##uselefthand():
  i01.setHandSpeed("right", 0.75, 0.75, 0.75, 0.75, 0.75, 0.65)
  i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("right", 0.25, 0.25, 0.25, 0.25)
  i01.setHeadSpeed(0.65, 0.65)
  i01.moveHead(20,84,78,80,13)
  i01.moveArm("left",65,52,59,23)
  i01.moveArm("right",82,61,50,16)
  i01.moveHand("left",140,50,40,180,180,0)
  i01.moveHand("right",140,125,130,3,0,11)
  sleep(4)
##more():
  i01.setHandSpeed("right", 0.75, 0.75, 0.75, 0.75, 0.75, 0.65)
  i01.setArmSpeed("left", 0.85, 0.85, 0.85, 0.95)
  i01.setArmSpeed("right", 0.75, 0.65, 0.65, 0.65)
  i01.setHeadSpeed(0.65, 0.65)
  i01.moveHead(16,84,78,80,13)
  i01.moveArm("left",63,52,59,23)
  i01.moveArm("right",82,60,50,16)
  i01.moveHand("left",140,148,180,180,180,0)
  i01.moveHand("right",80,114,88,3,0,11)
  sleep(3)
##handdown():
  i01.setHandSpeed("left", 0.75, 0.75, 0.75, 0.75, 0.75, 0.75)
  i01.setHandSpeed("right", 0.70, 0.70, 0.70, 0.70, 0.70, 1.0)
  i01.moveHead(16,84,78,80,13)
  i01.moveArm("left",66,52,59,23)
  i01.moveArm("right",59,60,50,16)
  i01.moveHand("left",140,148,180,180,180,0)
  i01.moveHand("right",54,95,66,3,0,11)
  sleep(2)
#isitaball():
  i01.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("right", 0.75, 0.85, 0.95, 0.85)
  i01.setArmSpeed("left", 0.75, 0.85, 0.90, 0.85)
  i01.setHeadSpeed(0.65, 0.75)
  i01.moveHead(90,83,78,80,13)
  i01.moveArm("left",70,59,95,15)
  i01.moveArm("right",12,74,33,15)
  i01.moveHand("left",170,150,180,180,180,164)
  i01.moveHand("right",105,81,78,57,62,105)
  i01.mouth.speakBlocking("I will start tracking the object")
  sleep(2)
  i01.mouth.speakBlocking("you need to set the point")
  i01.headTracking.startLKTracking()
  i01.eyesTracking.startLKTracking()
  sleep()
  
def phonehome():
    relax()
    i01.setHeadSpeed(1.0,1.0,1.0,1.0,1.0)
    i01.setArmSpeed("left",1.0,1.0,1.0,1.0)
    i01.setArmSpeed("right",1.0,1.0,1.0,1.0)
    i01.setHandSpeed("left",1.0,1.0,1.0,1.0,1.0,1.0)
    i01.setHandSpeed("right",1.0,1.0,1.0,1.0,1.0,1.0)
    i01.setTorsoSpeed(1.0,1.0,1.0)
    i01.moveHead(160,68)
    i01.moveArm("left",5,86,30,20)
    i01.moveArm("right",86,140,83,80)
    i01.moveHand("left",99,140,173,167,130,26)
    i01.moveHand("right",135,6,170,145,168,180)
    i01.moveTorso(25,80,90)
    sleep(2)
    i01.mouth.speakBlocking("E,T phone the big home of the inmoov nation")
    sleep(0.2)
    relax()
    
def madeby():
    relax()
    sleep(1)
    i01.moveHead(80,86)
    i01.moveArm("left",5,90,30,10)
    i01.moveArm("right",5,90,30,10)
    i01.moveHand("left",45,40,30,25,35,90)
    i01.moveHand("right",55,2,50,48,30,90)
    i01.moveTorso(90,90,90)
    sleep(3)
    #i01.mouth.speakBlocking("hello")
    i01.mouth.speakBlocking("bonjour")
    i01.moveHead(80,98)
    i01.moveArm("left",5,90,30,10)
    i01.moveArm("right",5,90,30,10)
    i01.moveHand("left",45,40,30,25,35,90)
    i01.moveHand("right",55,2,50,48,30,90)
    i01.moveTorso(90,90,90)
    sleep(1)
    i01.moveHead(90,89)
    i01.moveArm("left",42,104,30,10)
    i01.moveArm("right",33,116,30,10)
    i01.moveHand("left",45,40,30,25,35,120)
    i01.moveHand("right",55,2,50,48,30,40)
    i01.moveTorso(90,90,90)
    sleep(1)
    i01.moveHead(80,98)
    i01.moveArm("left",5,99,30,16)
    i01.moveArm("right",5,94,30,16)
    i01.moveHand("left",120,116,110,115,98,73)
    i01.moveHand("right",114,146,125,113,117,109)
    i01.moveTorso(90,90,90)
    #i01.mouth.speakBlocking("my name is inmoov")
    i01.mouth.speakBlocking("je m'appelle inmouv")
    i01.moveHead(68,90)
    i01.moveArm("left",5,99,30,16)
    i01.moveArm("right",85,102,38,16)
    i01.moveHand("left",120,116,110,115,98,73)
    i01.moveHand("right",114,146,161,132,168,19)
    i01.moveTorso(90,90,90)
    sleep(0.5)
    ##i01.setHandSpeed("left", 0.85, 0.85, 0.85, 0.85, 0.85, 1.0)
    ##i01.setHandSpeed("right", 0.85, 0.85, 0.85, 0.85, 0.85, 1.0)
    i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
    i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
    ##i01.setHeadSpeed(1.0, 0.90)
    ##i01.setTorsoSpeed(1.0, 1.0, 1.0)
    i01.moveHead(87,94)
    i01.moveArm("left",5,99,36,16)
    i01.moveArm("right",81,105,42,16)
    i01.moveHand("left",120,116,110,115,98,50)
    i01.moveHand("right",114,118,131,132,168,19)
    i01.moveTorso(90,90,90)
    sleep(1)
    #i01.mouth.speakBlocking("I am created by gael langevin")
    i01.mouth.speakBlocking("j'ai ete creer par gael langevin")
    i01.setHandSpeed("left", 0.90, 0.90, 0.90, 0.90, 0.90, 0.95)
    i01.setHandSpeed("right", 0.90, 0.90, 0.90, 0.90, 0.90, 0.95)
    i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
    i01.setArmSpeed("right", 0.90, 1.0, 1.0, 1.0)
    ##i01.setHeadSpeed(1.0, 0.90)
    ##i01.setTorsoSpeed(1.0, 1.0, 1.0)
    i01.moveHead(105,94)
    i01.moveArm("left",5,99,36,16)
    i01.moveArm("right",81,105,42,16)
    i01.moveHand("left",120,116,110,115,98,50)
    i01.moveHand("right",114,118,131,132,168,19)
    i01.moveTorso(90,90,90)
    sleep(0.2)
    i01.moveHead(80,86)
    i01.moveArm("left",5,96,25,10)
    i01.moveArm("right",5,94,26,10)
    i01.moveHand("left",110,62,56,88,81,18)
    i01.moveHand("right",78,88,101,95,81,137)
    i01.moveTorso(90,90,90)
    sleep(0.2)
    i01.moveHead(75,97)
    i01.moveArm("left",85,106,25,18)
    i01.moveArm("right",87,107,32,18)
    i01.moveHand("left",110,62,56,88,81,145)
    i01.moveHand("right",78,88,101,95,81,27)
    i01.moveTorso(90,90,90)
    #i01.mouth.speakBlocking("who is a french sculptor, designer")
    i01.mouth.speakBlocking("qui est un sculpteur, designer francais")
    sleep(0.5)
    i01.moveHead(80,86)
    i01.moveArm("left",5,96,25,10)
    i01.moveArm("right",5,94,26,10)
    i01.moveHand("left",110,62,56,88,81,18)
    i01.moveHand("right",78,88,101,95,81,137)
    i01.moveTorso(90,90,90)
    sleep(1)
    i01.moveHead(75,97)
    i01.moveArm("left",6,91,22,14)
    i01.moveArm("right",87,107,32,18)
    i01.moveHand("left",110,62,56,88,81,0)
    i01.moveHand("right",78,88,101,95,81,27)
    i01.moveTorso(90,90,90)
    i01.mouth.speakBlocking("my software is being developped by myrobtlab dot org")
    i01.mouth.speakBlocking("mon logiciel est developpe par myrobotlab point org")
    sleep(1)
    i01.moveHead(20,69)
    i01.moveArm("left",6,91,22,14)
    i01.moveArm("right",87,107,32,21)
    i01.moveHand("left",110,62,56,88,81,0)
    i01.moveHand("right",78,88,101,95,81,27)
    i01.moveTorso(90,90,90)
    #i01.mouth.speakBlocking("I am totally build with 3 D printed parts")
    i01.mouth.speakBlocking("je suis entierement imprimer en 3 D")
    i01.moveHead(75,97)
    i01.moveArm("left",85,106,25,18)
    i01.moveArm("right",87,107,32,18)
    i01.moveHand("left",110,62,56,88,81,145)
    i01.moveHand("right",78,88,101,95,81,27)
    i01.moveTorso(90,90,90)
    sleep(1)
    i01.moveHead(33,110)
    i01.moveArm("left",85,104,25,18)
    i01.moveArm("right",87,41,47,18)
    i01.moveHand("left",110,62,56,88,81,145)
    i01.moveHand("right",111,75,117,125,111,143)
    i01.moveTorso(90,90,90)
    sleep(1)
    i01.moveHead(62,102)
    i01.moveArm("left",85,104,25,18)
    i01.moveArm("right",87,41,47,18)
    i01.moveHand("left",110,62,56,88,81,145)
    i01.moveHand("right",111,75,117,125,111,143)
    i01.moveTorso(90,90,90)
    #i01.mouth.speakBlocking("which means all my parts")
    i01.mouth.speakBlocking("ce qui veut dire que toutes mes pieces,")
    i01.moveHead(79,88)
    i01.moveArm("left",85,104,25,18)
    i01.moveArm("right",87,59,46,18)
    i01.moveHand("left",110,62,56,88,81,145)
    i01.moveHand("right",59,75,117,125,111,113)
    i01.moveTorso(90,90,90)
    #i01.mouth.speakBlocking("are made on a home 3 D printer")
    i01.mouth.speakBlocking("sont fabriquer sur une petite imprimante familiale")
    sleep(1)
    i01.moveHead(40,84)
    i01.moveArm("left",85,72,38,18)
    i01.moveArm("right",87,64,47,18)
    i01.moveHand("left",124,97,66,120,130,35)
    i01.moveHand("right",59,75,117,125,111,113)
    i01.moveTorso(90,90,90)
    #i01.mouth.speakBlocking("each parts are design to fit 12 centimeter cube build area")
    i01.mouth.speakBlocking("chaque piece est concu dans un format de 12 centimetre cube,")
    sleep(1)
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
    sleep(1)
    #i01.mouth.speakBlocking("so anyone can reproduce me")
    i01.mouth.speakBlocking("de facon a ce que tout le monde puisse me reproduire")
    fullspeed()
    i01.moveHead(80,98)
    i01.moveArm("left",5,90,30,10)
    i01.moveArm("right",5,90,30,10)
    i01.moveHand("left",45,40,30,25,35,90)
    i01.moveHand("right",55,2,50,48,30,90)
    i01.moveTorso(90,90,90)
    sleep(1)
    #i01.mouth.speakBlocking("cool, don't you think")
    i01.mouth.speakBlocking("c'est cool, vous ne trouvez pas")
    sleep(1)
    #i01.mouth.speakBlocking("thank you for listening")
    i01.mouth.speakBlocking("merci de votre attention")
    i01.moveHead(116,80)
    i01.moveArm("left",85,93,42,16)
    i01.moveArm("right",87,93,37,18)
    i01.moveHand("left",124,82,65,81,41,143)
    i01.moveHand("right",59,53,89,61,36,21)
    i01.moveTorso(90,90,90)
    sleep(0.2)
    relax()
    
def lookaroundyou(): 
     i01.setHeadSpeed(0.8, 0.8, 0.6, 0.6, 1.0)
     for y in range(0, 3):
         # This only gets called if "data" = "look around you"
         # data = msg_i01_ear_recognized.data[0]
         data = "look around you"
         if (data == "can i have your attention"):
             i01.mouth.speak("ok you have my attention")
             stopit()
             x = (random.randint(1, 6))
             if x == 1:
                 i01.head.neck.moveTo(90)
             elif x == 2:
                 i01.head.rothead.moveTo(80)
             elif x == 3:
                 headdown()
             elif x == 4:
                 headupp()
             elif x == 5:
                 headright()
             elif x == 6:
                 headleft()
             sleep(1)
         x = (random.randint(1, 4))
         if x == 1:
             i01.mouth.speak("looking nice")
         if x == 2:
             i01.mouth.speak("i like it here")
         if x == 3:
             i01.mouth.speak("time just flies away")
         if x == 4:
             i01.mouth.speak("ok let's do something")
             sleep(2)
             x = (random.randint(1, 4))
             if x == 1:
                 comehere()
             if x == 2:
                 perfect()
                 sleep(2)
                 rest()
                 sleep(1)
                 relax()
             if x == 3:
                 rest()
             if x == 4:
                 fingerleft()
                 sleep(3)
                 relax()
 
def headfront():
     i01.head.neck.moveTo(90)
     i01.head.rothead.moveTo(90)
  
def headdown():
     i01.head.neck.moveTo(0)
  
def headupp():
     i01.head.neck.moveTo(180) 
 
def headright():
     i01.head.rothead.moveTo(0)
  
def headleft():
     i01.head.rothead.moveTo(180)
     
def Torso():
    i01.setTorsoSpeed(1.0, 1.0, 1.0)
    i01.moveTorso(60,90,90)
    sleep(2)
    i01.moveTorso(120,90,90)
    sleep(2)
    i01.moveTorso(90,90,90)
    sleep(2)     

def systemcheck():
     sleep(2)
     i01.setHeadSpeed(.75,.75)
     i01.moveHead(90,90)
     sleep(1)
     i01.moveHead(72,64)
     sleep(2)
     i01.moveHead(155,94)
     sleep(2)
     i01.moveHead(90,138)
     sleep(2)
     i01.moveHead(29,95)
     sleep(2)
     i01.moveHead(90,90)
     sleep(1.5)
     i01.mouth.speakBlocking("Head, neck and mouth,   check")
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
     i01.mouth.speakBlocking("right arm and right shoulder,    check")
     sleep(1)
     i01.setHeadSpeed(.9,.9)
     i01.moveHead(20,122)
     i01.setArmSpeed("left",.75,.75,.75,.75)
     i01.moveArm("left",24,62,52,45)
     sleep(2)
     i01.moveHead(90,90)
     i01.setHeadSpeed(.9,.9)
     sleep(1)
     i01.mouth.speakBlocking("left arm and left shoulder,    check")
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
     i01.mouth.speakBlocking(" hands and Wrists,    check")
     sleep(1)

     i01.setTorsoSpeed(0.80, 0.80, 1.0)
     i01.moveTorso(30,30,90)
     sleep(5)
     i01.moveTorso(140,150,90)
     sleep(5)
     i01.moveTorso(80,90,90)
     sleep(3) 
     i01.mouth.speakBlocking(" hips and waste,    check")
 
     i01.moveHead(90,90)
     i01.moveArm("left",0,90,30,10)
     i01.moveArm("right",0,90,30,10)
     i01.moveHand("left",0,0,0,0,0,90)
     i01.moveHand("right",0,0,0,0,0,90)
     i01.mouth.speakBlocking("all servos are functioning properly")
     sleep(1.5)
     i01.mouth.speakBlocking("awaiting your commands")
     sleep()
     relax()    
