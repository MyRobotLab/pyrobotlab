##########################################
# Example python script to demonstrate
# InverseKinematics for the InMoovArm
# 
##########################################

# Create the IK Service
ik = Runtime.createAndStart("ik", "InverseKinematics3D")
# Create the left arm of the inmoov
leftArm = Runtime.start("leftArm", "InMoovArm");

# connect the left arm.
leftPort = "COM31"
leftArm.connect(leftPort)
ik.setCurrentArm(leftArm.getDHRobotArm())
ik.addListener("publishJointAngles", leftArm.getName(), "onJointAngles")

x = 0.0
y = 0.0
z = 0.0

ik.moveTo(x,y,z)

print(ik.currentPosition())
