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
# Update this to be your controller
uberjoy.setController(2)
uberjoy.startPolling()

############################
# Attach the joystick to 
# the inmoov service servos
############################

def AListener(value):
  i01.rightHand.close()
  
def XListener(value):
  i01.rightHand.open()  

########################################################
# Left Arm Control  (left joystick for rotate and shoulder)
########################################################
uberjoy.map("x", -1, 1, i01.rightArm.rotate.min, i01.rightArm.rotate.max)
uberjoy.addXListener(i01.rightArm.rotate)

uberjoy.map("y", -1, 1, i01.rightArm.shoulder.max, i01.rightArm.shoulder.min)
uberjoy.addYListener(i01.rightArm.shoulder)

uberjoy.map("z", 0, 1, i01.rightArm.bicep.max, i01.rightArm.bicep.min)
uberjoy.addZListener(i01.rightArm.bicep)

uberjoy.map("rx", -1, 1, i01.rightHand.wrist.max, i01.rightHand.wrist.min)
uberjoy.addRXListener(i01.rightHand.wrist)

uberjoy.map("ry", -1, 1, i01.rightArm.omoplate.max, i01.rightArm.omoplate.min)
uberjoy.addRYListener(i01.rightArm.omoplate)

uberjoy.addListener("publish0", "python", "AListener")
uberjoy.addListener("publish2", "python", "XListener")



