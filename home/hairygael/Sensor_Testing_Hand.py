#This simple sensor InMoov script is tested on MyRobotLab version 1.0.2693
#The result can be seen in the Oscope and with the finger action.

leftPort = "COM3"

i01 = Runtime.createAndStart("i01", "InMoov")
leftHand = Runtime.create("i01.leftHand","InMoovHand")
i01.startLeftHand(leftPort)

left=Runtime.create("i01.left", "Arduino")
left.setBoard("atmega328")
left = Runtime.start("i01.left", "Arduino")
left.connect("COM3")

 
def publishPin(pins):
    for pin in range(0, len(pins)):
        print pins[pin].address, pins[pin].value  #these values are between 0-1024
        if pins[pin].value<=538:
          print "No pressure"
        if pins[pin].value>=539 and pins[pin].value<=540:
          print "Low pressure"
          FingerGoesBack()
        if pins[pin].value>=541 and pins[pin].value<=543:
          print "Soft pressure"
          FingerGoesBack()
        if pins[pin].value>=544:
          print "High pressure"
          FingerGoesBack()  
 
left.addListener("publishPinArray","python","publishPin")
sleep(5)
left.enablePin(54,1) #54 is pin A0, 1 is the number of polls per seconds

i01.leftHand.setAutoDisable(True)

def moveFingerSlowly():
    i01.leftHand.index.enable()
    i01.leftHand.index.setVelocity(25)
    sleep(2)
    i01.leftHand.index.moveTo(180)

def FingerGoesBack():
    i01.leftHand.index.enable()
    i01.leftHand.index.setVelocity(-1)
    i01.leftHand.index.moveTo(0) 
