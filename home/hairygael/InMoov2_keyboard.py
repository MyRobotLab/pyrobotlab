# A small script to run the InMoov hand with Keyboard control via python 
# To be used with version MRL above 1.0.2000

# Define the Arduino COM port
rightPort = "COM7"
# Here we start InMoov
i01 = Runtime.createAndStart("i01", "InMoov")
i01.startRightHand(rightPort)
# We want to map our servos to avoid forcing the servos
i01.rightHand.thumb.map(0,180,10,158)
i01.rightHand.index.map(0,180,42,160)
i01.rightHand.majeure.map(0,180,45,165)
i01.rightHand.ringFinger.map(0,180,35,145)
i01.rightHand.pinky.map(0,180,35,140)
i01.rightHand.wrist.map(0,180,40,15)
# We set the servos to disable after a few seconds to avoid burning
i01.rightHand.setAutoDisable(True)
# We start our keyboard
keyboard = Runtime.start("keyboard", "Keyboard")
keyboard.addKeyListener(python);

rightIndexPos = 0

# We define our keys
def onKey(key):
    print "you pressed ", key
    if (key=="O"):
             handopen()
    if (key=="C"):
             handclose()
    if (key=="A"):
             openindex()
    if (key=="Q"):
             closeindex()                           
    if (key=="K"):
             rightIndexPos++;
             i01.rightHand.index.moveTo(rightIndexPos)                           
    if (key=="L"):
             rightIndexPos--;
             i01.rightHand.index.moveTo(rightIndexPos)                           
           
print "here waiting"
keypress = keyboard.readKey()
print "finally you pressed", keypress, "!"

# End adding keyboard control
# Starting finger or hand movements exemples

def handopen():
  i01.setHandVelocity("right",-1.0,-1.0,-1.0,-1.0,-1.0,-1.0)
  i01.moveHand("right",0,0,0,0,0)

def handclose():
  i01.setHandVelocity("right",50,50,50,50,50,50)
  i01.moveHand("right",180,180,180,180,180)
  
def openindex():
  i01.rightHand.index.setVelocity(-1)
  i01.rightHand.index.moveTo(180)

def closeindex():
  i01.rightHand.index.setVelocity(-1)
  i01.rightHand.index.moveTo(0)     
