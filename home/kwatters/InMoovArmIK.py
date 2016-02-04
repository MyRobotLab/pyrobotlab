##########################################
# Example python script to demonstrate
# InverseKinematics for the InMoovArm
# 
##########################################
from time import sleep


######################
# work around until the race conditions in MRL are fixed.
######################
def resetArm():
    global leftArm
    leftArm.detach()
    sleep(2)
    leftArm.attach(leftPort)
    sleep(2)
    leftArm.bicep.attach()
    leftArm.rotate.attach()
    leftArm.shoulder.attach()
    leftArm.omoplate.attach()

############################################################
# MAIN Entry Point
############################################################
# Create the IK Service
ik = Runtime.createAndStart("ik", "InverseKinematics3D")
# Create the left arm of the inmoov
leftArm = Runtime.start("leftArm", "InMoovArm");
# connect the left arm.
leftPort = "COM21"
leftArm.connect(leftPort)
# update the IK service with the DH parameter description of the inmoov arm.
ik.setCurrentArm(leftArm.getDHRobotArm())
# wire in the callbacks between IK and the InMoovArm
ik.addListener("publishJointAngles", leftArm.getName(), "onJointAngles")

# start up a joystick service.
joystick = Runtime.start("joystick", "Joystick");
joystick.setController(2);
joystick.addInputListener(ik);
joystick.startPolling()
# TODO: start polling.

# start the web gui up.
webgui = Runtime.createAndStart("webgui", "WebGui")
# work around to re-attach the arduino and servos
# sometimes they don't attach on first try due to some race conditions. 



resetArm()
#x = 0.1
#y = 0.1
#z = 100.0
#ik.moveTo(x,y,z)
# print(ik.currentPosition())

