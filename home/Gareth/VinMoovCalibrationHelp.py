# Modified by Gareth for Calibvration purposes :-)
# This is file starts and controls MRL InMoov 
# service and attaches it to the Blender virtual InMoov
# Blender (2.72b) must be running a Blender.py TCP/IP server file
from time import sleep

vPortLeft = "vleft"
vPortRight = "vright"

###########################################################################
### special virtual blender handling - not in "regular" scripts - begin ###

# start blender service
blender = Runtime.start("blender", "Blender")

# connect blender service to running Blender (2.72b) instance
if (not blender.connect()):
	print("could not connect")

# get Blender.py version 
# FIXME - compare expected version !
blender.getVersion()

# pre-create Arduinos 
i01_left = Runtime.start("i01.left", "Arduino")
i01_right = Runtime.start("i01.right", "Arduino")
sleep(3)
# blender "attach" will connect Arduinos with serial ports running
# over tcp/ip sockets to Blender.py
blender.attach(i01_left)
#blender.attach(i01_right)
sleep(3)
### special virtual blender handling - not in "regular" scripts - end  ###
##########################################################################

# resume "regular" script
# connect head
i01 = Runtime.start("i01", "InMoov")
i01.startHead(vPortLeft)
i01.startLeftArm(vPortLeft)
#i01.startRightArm(vPortRight)
sleep(3)
mc = i01.startMouthControl("vPortLeft")
speech = i01.startMouth()
speech.speak("begin")
i01.startHead(vPortLeft)
# tweaking default settings of eyes
i01.head.eyeY.setMinMax(0,180)
i01.head.eyeY.map(0,180,75,95)
i01.head.eyeY.setRest(85)
i01.head.eyeX.setMinMax(0,180)
i01.head.eyeX.map(0,180,70,100)
i01.head.eyeX.setRest(85)
i01.head.neck.setMinMax(0,180)
i01.head.neck.map(0,180,15,155)
i01.head.neck.setRest(70)
i01.head.rothead.setMinMax(0,180)
i01.head.rothead.map(0,180,30,150)
i01.head.rothead.setRest(86)
# tweaking default settings of jaw
i01.head.jaw.setMinMax(6,25)
#i01.head.jaw.map(0,180,10,35)
i01.mouthControl.setmouth(6,25)

##############
i01.startLeftHand(vPortLeft)
# tweaking default settings of left hand
i01.leftHand.thumb.setMinMax(0,180)
i01.leftHand.index.setMinMax(0,180)
i01.leftHand.majeure.setMinMax(0,180)
i01.leftHand.ringFinger.setMinMax(0,180)
i01.leftHand.pinky.setMinMax(0,180)
i01.leftHand.thumb.map(0,180,45,140)
i01.leftHand.index.map(0,180,40,140)
i01.leftHand.majeure.map(0,180,30,176)
i01.leftHand.ringFinger.map(0,180,25,175)
i01.leftHand.pinky.map(0,180,15,112)
################
i01.startLeftArm(vPortLeft)
#tweak defaults LeftArm
#i01.leftArm.bicep.setMinMax(0,90)
#i01.leftArm.rotate.setMinMax(46,160)
#i01.leftArm.shoulder.setMinMax(30,100)
#i01.leftArm.omoplate.setMinMax(10,75)

#################
i01.startRightArm(vPortRight)
# tweak default RightArm
#i01.rightArm.bicep.setMinMax(0,90)
#i01.rightArm.rotate.setMinMax(46,160)
#i01.rightArm.shoulder.setMinMax(30,100)
#i01.rightArm.omoplate.setMinMax(10,75)

################
# virtual InMoov config begin ##############

def rest(delay):
 speech.speak("rest")
 i01.moveHead(80,86,82,78,76)
 i01.moveArm("left",5,90,30,10)
 i01.moveArm("right",5,90,30,10)
 i01.moveHand("left",2,2,2,2,2,90)
 i01.moveHand("right",2,2,2,2,2,90)
 i01.moveTorso(90,90,90)
 sleep(delay)
def handsforwards(delay):
 speech.speak("arms forwards")
 i01.moveHead(99, 82);
 i01.moveArm("left", 9, 115, 96, 51);
 i01.moveArm("right", 13, 104, 101, 49);
 i01.moveHand("left", 61, 0, 14, 38, 15, 0);
 i01.moveHand("right", 0, 24, 54, 50, 82, 180);
 sleep(delay)
rest(5) 
handsforwards(5)
rest(5)
# virtual InMoov config end ##############
