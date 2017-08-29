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
# Create the IK Service
ik = Runtime.createAndStart("ik", "InverseKinematics3D")
# Create the left arm of the inmoov
leftArm = Runtime.start("i01.leftArm", "InMoovArm");
# connect the left arm.
leftPort = "COM21"
leftArm.connect(leftPort)
# update the IK service with the DH parameter description of the inmoov arm.
ik.setCurrentArm(leftArm.getDHRobotArm())
# wire in the callbacks between IK and the InMoovArm
ik.addListener("publishJointAngles", leftArm.getName(), "onJointAngles")

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

resetArm()
#x = 0.1
#y = 0.1
#z = 100.0
#ik.moveTo(x,y,z)
# print(ik.currentPosition())

# starting point
# x , y , z
ik.centerAllJoints()


x1 = ik.currentPosition().x
y1 = ik.currentPosition().y
z1 = ik.currentPosition().z


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

ik.centerAllJoints()
sleep(1.0)

ik.moveTo(curX,curY,curZ)

print ik.currentPosition()

for i in range(0 , 100):
  curX+=dx
  curY+=dy  
  curZ+=dz
  ik.moveTo(curX, curY, curZ)    
  sleep(delay)

print ik.currentPosition()
