##################################################
# Inverse Kinematics
# This is an example to build up a robot arm
# using (modified?) DH parameters
# then use the InverseKinematics3D service to
# compute the forward and inverse kinematics for 
# the arm.
##################################################
from time import sleep
from org.myrobotlab.service import InMoovArm
from org.myrobotlab.kinematics import DHRobotArm
from org.myrobotlab.kinematics import DHLink
from org.myrobotlab.kinematics import DHLinkType

# Create a robot arm
myRobotArm = DHRobotArm()

# Lets create a 2 link robot arm
# Create the first link in the arm specified by 100,100,0,90
# additionally specify a name for the link which can be used elsewhere. 
d1 = 100
r1 = 100
theta = 0
alpha = 90
link0 = DHLink("base", d1, r1, theta, alpha)

# Create the second link (same as the first link.)
d1 = 100
r1 = 100
theta = 0
alpha = 90
link1 = DHLink("link1", d1, r1, theta, alpha)

# Add the links to the robot arm
myRobotArm.addLink(link0)
myRobotArm.addLink(link1)


# create the  IK3D service.
ik3d= Runtime.createAndStart("ik3d", "InverseKinematics3D")

# assign our custom DH robot arm to the IK service.
ik3d.setCurrentArm(myRobotArm)


# print out the current postion of the arm.
print ik3d.getCurrentArm().getPalmPosition()


# Now, pick a start/end point 
# and begin moving along a stright line as specified by the start/stop point.

# starting point
# x , y , z
x1 = 100
y1 = 100
z1 = 100

# ending point
# x , y , z
x2 = 200
y2 = -400
z2 = 100

# how many steps will we take to get there
numSteps = 100
# delay between steps (in seconds) (this will control the velocity of the end effector.
delay = 0.1 

# lets compute how long the path is.
# this is the change in x,y,z between the two points
# divided up into numSteps, so we know how much to
# move in the x,y,z direction for each step.
dx = 1.0*(x2 - x1)/numSteps
dy = 1.0*(y2 - y1)/numSteps
dz = 1.0*(z2 - z1)/numSteps

# our starting point for the iteratin
# set that to the current x,y,z position 
curX = x1
curY = y1
curZ = z1

# tell the arm to configure to that point
ik3d.moveTo(curX,curY,curZ)

# iterate over the 100 steps
for i in range(0 , 100):
  # Increment our desired current position by dx,dy,dz 
  curX+=dx
  curY+=dy  
  curZ+=dz
# tell the ik engine to move to that new point
  ik3d.moveTo(curX, curY, curZ)    
  # pause for a moment to let the arm arrive at it's destination
  # smaller delay = faster movement.
  sleep(delay)

