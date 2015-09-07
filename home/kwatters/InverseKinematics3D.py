from time import sleep
from org.myrobotlab.service import InMoovArm

# create the  IK3D service.
ik3d= Runtime.createAndStart("ik3d", "InverseKinematics3D")

ik3d.setCurrentArm(InMoovArm.getDHRobotArm())

# starting point
# x , y , z
x1 = 100
y1 = 100
z1 = 100

# ending point
# x , y , z
x2 = 500
y2 = 100
z2 = 100


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

ik3d.moveTo(curX,curY,curZ)

for i in range(0 , 100):
  curX+=dx
  curY+=dy  
  curZ+=dz
  ik3d.moveTo(curX, curY, curZ)    
  sleep(delay)
  






    
    
    


