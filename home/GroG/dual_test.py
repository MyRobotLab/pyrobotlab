##############################################################
# MyRobotLab configuration file
# This file is generated from a running instance of MyRobotLab.
# It is meant to get MyRobotLab as close to that instance's state a possible.
# This file can be generated at any time using Runtime.save(filename)
# More information @ http://myrobotlab.org and https://github.com/myrobotlab
# version 1.1.1619314253
# generated Sun Apr 25 09:10:16 PDT 2021

##############################################################
## imports ####
import time
from time import sleep
import org.myrobotlab.framework.Platform as Platform
import org.myrobotlab.service.Runtime as Runtime

# Platform.setVirtual(True)
##############################################################
## creating 41 services ####
# Although Runtime.start(name,type) both creates and starts services it might be desirable on creation to
# substitute peers, types or references of other sub services before the service is "started"
# e.g. i01 = Runtime.create('i01', 'InMoov') # this will "create" the service and config could be manipulated before starting 
# e.g. i01_left = Runtime.create('i01.left', 'Ssc32UsbServoController')
runtime = Runtime.getInstance()
i01_leftArm_bicep = Runtime.start('i01.leftArm.bicep', 'Servo')
i01_leftHand_index = Runtime.start('i01.leftHand.index', 'Servo')
i01_servomixer = Runtime.start('i01.servomixer', 'ServoMixer')
i01_rightArm_rotate = Runtime.start('i01.rightArm.rotate', 'Servo')
i01_head_neck = Runtime.start('i01.head.neck', 'Servo')
# i01_leftArm = Runtime.start('i01.leftArm', 'InMoov2Arm')
# jme = Runtime.start('jme', 'JMonkeyEngine')
# i01_rightArm = Runtime.start('i01.rightArm', 'InMoov2Arm')
# i01_leftHand = Runtime.start('i01.leftHand', 'InMoov2Hand')
i01_rightHand_thumb = Runtime.start('i01.rightHand.thumb', 'Servo')
# i01_mouthControl = Runtime.start('i01.mouthControl', 'MouthControl')
i01_leftArm_omoplate = Runtime.start('i01.leftArm.omoplate', 'Servo')
i01_rightArm_bicep = Runtime.start('i01.rightArm.bicep', 'Servo')
i01 = Runtime.start('i01', 'InMoov2')
i01_rightArm_shoulder = Runtime.start('i01.rightArm.shoulder', 'Servo')
i01_leftHand_ringFinger = Runtime.start('i01.leftHand.ringFinger', 'Servo')
i01_rightHand_ringFinger = Runtime.start('i01.rightHand.ringFinger', 'Servo')
webgui = Runtime.create('webgui', 'WebGui')
webgui.autoStartBrowser(False)
webgui.startService()
i01_leftArm_shoulder = Runtime.start('i01.leftArm.shoulder', 'Servo')
i01_rightArm_omoplate = Runtime.start('i01.rightArm.omoplate', 'Servo')
i01_torso_lowStom = Runtime.start('i01.torso.lowStom', 'Servo')
i01_leftHand_thumb = Runtime.start('i01.leftHand.thumb', 'Servo')
i01_rightHand_pinky = Runtime.start('i01.rightHand.pinky', 'Servo')
i01_leftHand_majeure = Runtime.start('i01.leftHand.majeure', 'Servo')
i01_leftHand_pinky = Runtime.start('i01.leftHand.pinky', 'Servo')
i01_rightHand_index = Runtime.start('i01.rightHand.index', 'Servo')
security = Runtime.start('security', 'Security')
i01_leftArm_rotate = Runtime.start('i01.leftArm.rotate', 'Servo')
i01_rightHand_majeure = Runtime.start('i01.rightHand.majeure', 'Servo')
# i01_head = Runtime.start('i01.head', 'InMoov2Head')
i01_torso_topStom = Runtime.start('i01.torso.topStom', 'Servo')
i01_torso_midStom = Runtime.start('i01.torso.midStom', 'Servo')
i01_head_jaw = Runtime.start('i01.head.jaw', 'Servo')
# i01_torso = Runtime.start('i01.torso', 'InMoov2Torso')
i01_leftHand_wrist = Runtime.start('i01.leftHand.wrist', 'Servo')
python = Runtime.start('python', 'Python')
i01_head_rollNeck = Runtime.start('i01.head.rollNeck', 'Servo')
i01_head_rothead = Runtime.start('i01.head.rothead', 'Servo')
# i01_rightHand = Runtime.start('i01.rightHand', 'InMoov2Hand')
i01_rightHand_wrist = Runtime.start('i01.rightHand.wrist', 'Servo')

##############################################################
## creating client connections connections ####

##############################################################
## configuring services ####


# Servo Config : i01_head_neck
# sets initial position of servo before moving
# in theory this is the position of the servo when this file was created
i01_head_neck.setPosition(53)
i01_head_neck.map(20.0,160.0,20.0,160.0)
i01_head_neck.setInverted(False)
i01_head_neck.setSpeed(45.0)
i01_head_neck.setRest(90.0)
i01_head_neck.setPin(5)
i01_head_neck.setAutoDisable(False)



# Servo Config : i01_head_rothead
# sets initial position of servo before moving
# in theory this is the position of the servo when this file was created
i01_head_rothead.setPosition(90)
i01_head_rothead.map(30.0,150.0,30.0,150.0)
i01_head_rothead.setInverted(False)
i01_head_rothead.setSpeed(45.0)
i01_head_rothead.setRest(90.0)
i01_head_rothead.setPin(7)
i01_head_rothead.setAutoDisable(False)


# Servo Config : i01_leftArm_bicep
# sets initial position of servo before moving
# in theory this is the position of the servo when this file was created
i01_leftArm_bicep.setPosition(40)
i01_leftArm_bicep.map(5.0,90.0,5.0,90.0)
i01_leftArm_bicep.setInverted(False)
i01_leftArm_bicep.setSpeed(20.0)
i01_leftArm_bicep.setRest(5.0)
i01_leftArm_bicep.setPin(8)
i01_leftArm_bicep.setAutoDisable(False)

# Servo Config : i01_leftHand_index
# sets initial position of servo before moving
# in theory this is the position of the servo when this file was created
i01_leftHand_index.setPosition(38)
i01_leftHand_index.map(0.0,180.0,0.0,180.0)
i01_leftHand_index.setInverted(False)
i01_leftHand_index.setSpeed(45.0)
i01_leftHand_index.setRest(2.0)
i01_leftHand_index.setPin(3)
i01_leftHand_index.setAutoDisable(False)

# Servo Config : i01_rightArm_rotate
# sets initial position of servo before moving
# in theory this is the position of the servo when this file was created
i01_rightArm_rotate.setPosition(90)
i01_rightArm_rotate.map(40.0,180.0,40.0,180.0)
i01_rightArm_rotate.setInverted(False)
i01_rightArm_rotate.setSpeed(20.0)
i01_rightArm_rotate.setRest(90.0)
i01_rightArm_rotate.setPin(9)
i01_rightArm_rotate.setAutoDisable(False)


# Servo Config : i01_rightHand_thumb
# sets initial position of servo before moving
# in theory this is the position of the servo when this file was created
i01_rightHand_thumb.setPosition(2)
i01_rightHand_thumb.map(0.0,180.0,0.0,180.0)
i01_rightHand_thumb.setInverted(False)
i01_rightHand_thumb.setSpeed(45.0)
i01_rightHand_thumb.setRest(2.0)
i01_rightHand_thumb.setPin(2)
i01_rightHand_thumb.setAutoDisable(False)

# Servo Config : i01_leftArm_omoplate
# sets initial position of servo before moving
# in theory this is the position of the servo when this file was created
i01_leftArm_omoplate.setPosition(38)
i01_leftArm_omoplate.map(10.0,80.0,10.0,80.0)
i01_leftArm_omoplate.setInverted(False)
i01_leftArm_omoplate.setSpeed(20.0)
i01_leftArm_omoplate.setRest(10.0)
i01_leftArm_omoplate.setPin(11)
i01_leftArm_omoplate.setAutoDisable(False)

# Servo Config : i01_rightArm_bicep
# sets initial position of servo before moving
# in theory this is the position of the servo when this file was created
i01_rightArm_bicep.setPosition(22)
i01_rightArm_bicep.map(5.0,90.0,5.0,90.0)
i01_rightArm_bicep.setInverted(False)
i01_rightArm_bicep.setSpeed(20.0)
i01_rightArm_bicep.setRest(5.0)
i01_rightArm_bicep.setPin(8)
i01_rightArm_bicep.setAutoDisable(False)

# InMoov2 Config : i01
# i01.setVirtual(True)
# i01.setMute(False)
# start groups of sub services
# i01.startHead()
# i01.startLeftHand()
#  i01.getRightHand()
# i01.startLeftArm()
# i01.startSimulator()
# i01.getRightArm()
# i01.startTorso()

# Servo Config : i01_rightArm_shoulder
# sets initial position of servo before moving
# in theory this is the position of the servo when this file was created
i01_rightArm_shoulder.setPosition(92)
i01_rightArm_shoulder.map(0.0,180.0,0.0,180.0)
i01_rightArm_shoulder.setInverted(False)
i01_rightArm_shoulder.setSpeed(17.0)
i01_rightArm_shoulder.setRest(30.0)
i01_rightArm_shoulder.setPin(10)
i01_rightArm_shoulder.setAutoDisable(False)

# Servo Config : i01_leftHand_ringFinger
# sets initial position of servo before moving
# in theory this is the position of the servo when this file was created
i01_leftHand_ringFinger.setPosition(2)
i01_leftHand_ringFinger.map(0.0,180.0,0.0,180.0)
i01_leftHand_ringFinger.setInverted(False)
i01_leftHand_ringFinger.setSpeed(45.0)
i01_leftHand_ringFinger.setRest(2.0)
i01_leftHand_ringFinger.setPin(5)
i01_leftHand_ringFinger.setAutoDisable(False)

# Servo Config : i01_rightHand_ringFinger
# sets initial position of servo before moving
# in theory this is the position of the servo when this file was created
i01_rightHand_ringFinger.setPosition(2)
i01_rightHand_ringFinger.map(0.0,180.0,0.0,180.0)
i01_rightHand_ringFinger.setInverted(False)
i01_rightHand_ringFinger.setSpeed(45.0)
i01_rightHand_ringFinger.setRest(2.0)
i01_rightHand_ringFinger.setPin(5)
i01_rightHand_ringFinger.setAutoDisable(False)

# WebGui Config : webgui
webgui.autoStartBrowser(False)
webgui.setPort(8888)
webgui.setAddress("0.0.0.0")

# Servo Config : i01_leftArm_shoulder
# sets initial position of servo before moving
# in theory this is the position of the servo when this file was created
i01_leftArm_shoulder.setPosition(76)
i01_leftArm_shoulder.map(0.0,180.0,0.0,180.0)
i01_leftArm_shoulder.setInverted(False)
i01_leftArm_shoulder.setSpeed(20.0)
i01_leftArm_shoulder.setRest(30.0)
i01_leftArm_shoulder.setPin(10)
i01_leftArm_shoulder.setAutoDisable(False)

# Servo Config : i01_rightArm_omoplate
# sets initial position of servo before moving
# in theory this is the position of the servo when this file was created
i01_rightArm_omoplate.setPosition(10)
i01_rightArm_omoplate.map(10.0,80.0,10.0,80.0)
i01_rightArm_omoplate.setInverted(False)
i01_rightArm_omoplate.setSpeed(20.0)
i01_rightArm_omoplate.setRest(10.0)
i01_rightArm_omoplate.setPin(11)
i01_rightArm_omoplate.setAutoDisable(False)

# Servo Config : i01_torso_lowStom
# sets initial position of servo before moving
# in theory this is the position of the servo when this file was created
i01_torso_lowStom.setPosition(76)
i01_torso_lowStom.map(0.0,180.0,0.0,180.0)
i01_torso_lowStom.setInverted(False)
i01_torso_lowStom.setSpeed(5.0)
i01_torso_lowStom.setRest(90.0)
i01_torso_lowStom.setPin(29)
i01_torso_lowStom.setAutoDisable(False)

# Servo Config : i01_leftHand_thumb
# sets initial position of servo before moving
# in theory this is the position of the servo when this file was created
i01_leftHand_thumb.setPosition(43)
i01_leftHand_thumb.map(0.0,180.0,0.0,180.0)
i01_leftHand_thumb.setInverted(False)
i01_leftHand_thumb.setSpeed(45.0)
i01_leftHand_thumb.setRest(2.0)
i01_leftHand_thumb.setPin(2)
i01_leftHand_thumb.setAutoDisable(False)

# Servo Config : i01_rightHand_pinky
# sets initial position of servo before moving
# in theory this is the position of the servo when this file was created
i01_rightHand_pinky.setPosition(45)
i01_rightHand_pinky.map(0.0,180.0,0.0,180.0)
i01_rightHand_pinky.setInverted(False)
i01_rightHand_pinky.setSpeed(45.0)
i01_rightHand_pinky.setRest(2.0)
i01_rightHand_pinky.setPin(6)
i01_rightHand_pinky.setAutoDisable(False)

# Servo Config : i01_leftHand_majeure
# sets initial position of servo before moving
# in theory this is the position of the servo when this file was created
i01_leftHand_majeure.setPosition(2)
i01_leftHand_majeure.map(0.0,180.0,0.0,180.0)
i01_leftHand_majeure.setInverted(False)
i01_leftHand_majeure.setSpeed(45.0)
i01_leftHand_majeure.setRest(2.0)
i01_leftHand_majeure.setPin(4)
i01_leftHand_majeure.setAutoDisable(False)

# Servo Config : i01_leftHand_pinky
# sets initial position of servo before moving
# in theory this is the position of the servo when this file was created
i01_leftHand_pinky.setPosition(2)
i01_leftHand_pinky.map(0.0,180.0,0.0,180.0)
i01_leftHand_pinky.setInverted(False)
i01_leftHand_pinky.setSpeed(45.0)
i01_leftHand_pinky.setRest(2.0)
i01_leftHand_pinky.setPin(6)
i01_leftHand_pinky.setAutoDisable(False)

# Servo Config : i01_rightHand_index
# sets initial position of servo before moving
# in theory this is the position of the servo when this file was created
i01_rightHand_index.setPosition(2)
i01_rightHand_index.map(0.0,180.0,0.0,180.0)
i01_rightHand_index.setInverted(False)
i01_rightHand_index.setSpeed(45.0)
i01_rightHand_index.setRest(2.0)
i01_rightHand_index.setPin(3)
i01_rightHand_index.setAutoDisable(False)

# Servo Config : i01_leftArm_rotate
# sets initial position of servo before moving
# in theory this is the position of the servo when this file was created
i01_leftArm_rotate.setPosition(113)
i01_leftArm_rotate.map(40.0,180.0,40.0,180.0)
i01_leftArm_rotate.setInverted(False)
i01_leftArm_rotate.setSpeed(20.0)
i01_leftArm_rotate.setRest(90.0)
i01_leftArm_rotate.setPin(9)
i01_leftArm_rotate.setAutoDisable(False)

# Servo Config : i01_rightHand_majeure
# sets initial position of servo before moving
# in theory this is the position of the servo when this file was created
i01_rightHand_majeure.setPosition(2)
i01_rightHand_majeure.map(0.0,180.0,0.0,180.0)
i01_rightHand_majeure.setInverted(False)
i01_rightHand_majeure.setSpeed(45.0)
i01_rightHand_majeure.setRest(2.0)
i01_rightHand_majeure.setPin(4)
i01_rightHand_majeure.setAutoDisable(False)

# Servo Config : i01_torso_topStom
# sets initial position of servo before moving
# in theory this is the position of the servo when this file was created
i01_torso_topStom.setPosition(77)
i01_torso_topStom.map(60.0,120.0,60.0,120.0)
i01_torso_topStom.setInverted(False)
i01_torso_topStom.setSpeed(5.0)
i01_torso_topStom.setRest(90.0)
i01_torso_topStom.setPin(27)
i01_torso_topStom.setAutoDisable(False)

# Servo Config : i01_torso_midStom
# sets initial position of servo before moving
# in theory this is the position of the servo when this file was created
i01_torso_midStom.setPosition(57)
i01_torso_midStom.map(0.0,180.0,0.0,180.0)
i01_torso_midStom.setInverted(False)
i01_torso_midStom.setSpeed(5.0)
i01_torso_midStom.setRest(90.0)
i01_torso_midStom.setPin(28)
i01_torso_midStom.setAutoDisable(False)

# Servo Config : i01_head_jaw
# sets initial position of servo before moving
# in theory this is the position of the servo when this file was created
i01_head_jaw.setPosition(15)
i01_head_jaw.map(10.0,25.0,10.0,25.0)
i01_head_jaw.setInverted(False)
i01_head_jaw.setSpeed(45.0)
i01_head_jaw.setRest(10.0)
i01_head_jaw.setPin(26)
i01_head_jaw.setAutoDisable(False)

# Servo Config : i01_leftHand_wrist
# sets initial position of servo before moving
# in theory this is the position of the servo when this file was created
i01_leftHand_wrist.setPosition(90)
i01_leftHand_wrist.map(0.0,180.0,0.0,180.0)
i01_leftHand_wrist.setInverted(False)
i01_leftHand_wrist.setSpeed(45.0)
i01_leftHand_wrist.setRest(90.0)
i01_leftHand_wrist.setPin(7)
i01_leftHand_wrist.setAutoDisable(False)

# Servo Config : i01_head_rollNeck
# sets initial position of servo before moving
# in theory this is the position of the servo when this file was created
i01_head_rollNeck.setPosition(102)
i01_head_rollNeck.map(20.0,160.0,20.0,160.0)
i01_head_rollNeck.setInverted(False)
i01_head_rollNeck.setSpeed(None)
i01_head_rollNeck.setRest(90.0)
# i01_head_rollNeck.setPin(null)
i01_head_rollNeck.setAutoDisable(False)

# Servo Config : i01_rightHand_wrist
# sets initial position of servo before moving
# in theory this is the position of the servo when this file was created
i01_rightHand_wrist.setPosition(90)
i01_rightHand_wrist.map(0.0,180.0,0.0,180.0)
i01_rightHand_wrist.setInverted(False)
i01_rightHand_wrist.setSpeed(45.0)
i01_rightHand_wrist.setRest(90.0)
i01_rightHand_wrist.setPin(7)
i01_rightHand_wrist.setAutoDisable(False)

# the code above was mostly generated

# let inmoov2 start the simulator - it does a 
# large amount of configuration and adding nodes
jme = i01.startSimulator()

# re-map a couple servos i have backwards in the sim vs real
jme.setMapper("i01.head.neck", 0, 180, -20, 20)
jme.setMapper("i01.head.rothead", 0, 180, 180, 0)

#
arduino = Runtime.start('arduino', 'Arduino')
arduino.connect('/dev/ttyACM0')

sleep(3)
arduino.attach("i01.head.neck")
arduino.attach("i01.head.rothead")

cv = Runtime.start('cv', 'OpenCV')
# i01_eye = Runtime.start('eye', 'OpenCV')
cv.capture(4)
