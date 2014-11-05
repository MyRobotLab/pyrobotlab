import time
leftPort = "COM15"
rightPort = "COM19"
############################
# Start the InMoov Service
############################
i01 = Runtime.createAndStart("i01", "InMoov")
i01.startAll(leftPort, rightPort)
############################
# Start the Joystick service
############################
uberjoy = Runtime.createAndStart("uberjoy", "Joystick")
uberjoy.setController(2)
uberjoy.startPolling()
############################
# Attach the joystick to 
# the inmoov service servos
############################
########################################################
# Left Arm Control  (left joystick for rotate and shoulder)
########################################################
uberjoy.map("x", -1, 1, 0, 180)
uberjoy.addXListener(i01.leftArm.rotate)
uberjoy.map("y", -1, 1, 0, 180)
uberjoy.addYListener(i01.leftArm.shoulder)
########################################################
# Right Arm Control  (right joystick for rotate and shoulder)
########################################################
uberjoy.map("rx", -1, 1, 0, 180)
uberjoy.addXListener(i01.rightArm.rotate)
uberjoy.map("ry", -1, 1, 0, 180)
uberjoy.addYListener(i01.rightArm.shoulder)