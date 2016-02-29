
from time import sleep

# Configure com ports
leftPort = "COM15"
rightPort = "COM19"
i01 = Runtime.createAndStart("i01", "InMoov")

# tell the inmoov to be a quiet and obiedient slave.
i01.setMute(True)
i01.startAll(leftPort, rightPort)


# Gestures to use
def fullspeed():
  i01.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
  i01.setHeadSpeed(1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setTorsoSpeed(1.0, 1.0, 1.0)

def carrybaby():
    i01.moveHead(18,111,85,85,5)
    i01.moveArm("left",81,50,45,16)
    i01.moveArm("right",78,44,50,31)
    i01.moveHand("left",180,180,180,180,180,25)
    i01.moveHand("right",111,128,140,151,169,86)
    i01.moveTorso(90,90,90)
    
def fisthips():
  i01.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
  i01.setHeadSpeed(0.65, 0.75)
  i01.moveHead(138,80)
  i01.moveArm("left",79,45,23,41)
  i01.moveArm("right",71,40,14,39)
  i01.moveHand("left",180,180,180,180,180,47)
  i01.moveHand("right",99,130,152,154,145,180)
  i01.moveTorso(90,90,90)


i01.rest()
sleep(5)
fullspeed()
sleep(5)
carrybaby()
sleep(5)
i01.rest()
sleep(2)
i01.detach()



i01.rest()