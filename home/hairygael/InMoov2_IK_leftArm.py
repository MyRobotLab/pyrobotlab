##########################################
# Example python script to demonstrate
# InverseKinematics for the InMoovArm
# 
##########################################
from time import sleep
import org.myrobotlab.framework.Platform as Platform


######################
# work around until the race conditions in MRL are fixed.
######################
def resetArm():
    #global leftArm
    #leftArm.detach()
    #sleep(2)
    #leftArm.attach(leftPort)
    #sleep(2)
    #leftArm.bicep.attach()
    #leftArm.rotate.attach()
    #leftArm.shoulder.attach()
    #leftArm.omoplate.attach()
    pass

############################################################
# MAIN Entry Point
############################################################
Platform.setVirtual(True)
# Create the IK Service
ik = Runtime.createAndStart("ik", "InverseKinematics3D")
# Create the left arm of the inmoov
i01 = Runtime.start('i01', 'InMoov2')
i01.setVirtual(True)
i01_leftArm = Runtime.start("i01.leftArm", "InMoov2Arm")
i01_leftArm_shoulder = Runtime.start('i01.leftArm.shoulder', 'Servo')
i01_leftArm_rotate = Runtime.start('i01.leftArm.rotate', 'Servo')
i01_leftArm_bicep = Runtime.start('i01.leftArm.bicep', 'Servo')
i01_leftArm_omoplate = Runtime.start('i01.leftArm.omoplate', 'Servo')
# Create the arduino
i01_left = Runtime.start('i01.left', 'Arduino')

# Servo Config : i01_leftArm_rotate
i01_leftArm_rotate.setPosition(90)
i01_leftArm_rotate.map(40.0,180.0,64.0,132.0)
i01_leftArm_rotate.setInverted(False)
i01_leftArm_rotate.setSpeed(20.0)
i01_leftArm_rotate.setRest(90.0)
i01_leftArm_rotate.setPin(9)
i01_leftArm_rotate.setAutoDisable(True)

# Servo Config : i01_leftArm_bicep
i01_leftArm_bicep.setPosition(0)
i01_leftArm_bicep.map(0.0,90.0,46.0,96.0)
i01_leftArm_bicep.setInverted(False)
i01_leftArm_bicep.setSpeed(20.0)
i01_leftArm_bicep.setRest(0.0)
i01_leftArm_bicep.setPin(8)
i01_leftArm_bicep.setAutoDisable(True)

# Servo Config : i01_leftArm_omoplate
i01_leftArm_omoplate.setPosition(10)
i01_leftArm_omoplate.map(10.0,80.0,42.0,80.0)
i01_leftArm_omoplate.setInverted(False)
i01_leftArm_omoplate.setSpeed(20.0)
i01_leftArm_omoplate.setRest(10.0)
i01_leftArm_omoplate.setPin(11)
i01_leftArm_omoplate.setAutoDisable(True)

# Servo Config : i01_leftArm_shoulder
i01_leftArm_shoulder.setPosition(30)
i01_leftArm_shoulder.map(0.0,180.0,40.0,147.0)
i01_leftArm_shoulder.setInverted(False)
i01_leftArm_shoulder.setSpeed(20.0)
i01_leftArm_shoulder.setRest(30.0)
i01_leftArm_shoulder.setPin(10)
i01_leftArm_shoulder.setAutoDisable(True)


# Arduino Config : i01_right
i01_left.setVirtual(False)
# we have the following ports : [COM3.UART, COM4.UART, COM4, COM3]
i01_left.connect("COM7")
i01_left.setBoardMega()
# make sure the pins are set before attaching
i01_leftArm_shoulder.setPin("10")
i01_leftArm_bicep.setPin("8")
i01_leftArm_omoplate.setPin("11")
i01_leftArm_rotate.setPin("9")
i01_left.attach("i01.leftArm.shoulder")
i01_left.attach("i01.leftArm.bicep")
i01_left.attach("i01.leftArm.omoplate")
i01_left.attach("i01.leftArm.rotate")

jme = i01.startSimulator()

# update the IK service with the DH parameter description of the inmoov arm.
ik.setCurrentArm("i01_leftArm", i01_leftArm.getDHRobotArm("arm", "left"))
# wire in the callbacks between IK and the InMoovArm
ik.addListener("publishJointAngles", i01_leftArm.getName(), "onJointAngles")

# start up a joystick service.
useJoystick = False
if useJoystick:
  joystick = Runtime.start("joystick", "Joystick");
  joystick.setController(8);
  joystick.addInputListener(ik);
  joystick.startPolling()
  # TODO: start polling.

# start the web gui up.
# webgui = Runtime.createAndStart("webgui", "WebGui")
# work around to re-attach the arduino and servos
# sometimes they don't attach on first try due to some race conditions. 

#resetArm()
#x = 0.1
#y = 0.1
#z = 100.0
#ik.moveTo(x,y,z)
# print(ik.currentPosition())

# starting point
# x , y , z
ik.centerAllJoints("i01_leftArm")


x1 = ik.currentPosition("i01_leftArm").x
y1 = ik.currentPosition("i01_leftArm").y
z1 = ik.currentPosition("i01_leftArm").z


x = 0
y = -50
z = -200

# ending point
# x , y , z
x2 = x1 +x
y2 = y1 +y
z2 = z1 +z


startPoint = [ x1, y1, z1 ]
# move along the x in a straight line from 100 to 500
endPoint = [ x2 , y2 , z2 ]

# how many steps?  
numSteps = 100

# delay between steps (in seconds)
delay = 0.1 

# lets compute how long the path is.
dx = 1.0*(x2 - x1)/numSteps
dy = 1.0*(y2 - y1)/numSteps
dz = 1.0*(z2 - z1)/numSteps

# our current xyz
curX = startPoint[0]
curY = startPoint[1]
curZ = startPoint[2]

ik.centerAllJoints("i01_leftArm")
sleep(1.0)

ik.moveTo("i01_leftArm", curX,curY,curZ)

print ik.currentPosition("i01_leftArm")

for i in range(0 , 100):
  curX+=dx
  curY+=dy  
  curZ+=dz
  ik.moveTo("i01_leftArm", curX, curY, curZ)    
  sleep(delay)

print ik.currentPosition("i01_leftArm")
