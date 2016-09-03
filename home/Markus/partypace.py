
from java.lang import String
import time 
millis = time.time()

keyboard = Runtime.createAndStart("keyboard", "Keyboard")
keyboard.addListener("keyCommand", python.getName(), "input")

leftPort = "COM3"
rightPort = "COM7"


i01 = Runtime.createAndStart("i01", "InMoov")

# starts everything
i01.startAll(leftPort, rightPort)

torso = i01.startTorso("COM3")

left = Runtime.getService("i01.left")
right = Runtime.getService("i01.right")

isRunning = False

#############################################################################################
# Markus Mod

i01.leftArm.omoplate.map(10,80,80,20)
i01.rightArm.omoplate.map(10,80,80,10)
i01.leftArm.shoulder.map(0,180,170,15)
i01.rightArm.shoulder.map(0,180,190,50)
i01.leftArm.rotate.map(40,180,140,20)
i01.rightArm.rotate.map(40,180,140,20)
i01.leftArm.bicep.map(5,90,90,20)
i01.rightArm.bicep.map(5,90,90,20)
i01.head.rothead.map(30,150,150,30)
i01.torso.topStom.map(60,120,70,110)
i01.head.eyeX.map(60,100,90,50)
i01.head.eyeY.map(50,100,100,50)
i01.head.neck.map(20,160,160,20)

############################################################
#to tweak the default Pid values
i01.headTracking.xpid.setPID(10.0,5.0,0.1)
i01.headTracking.ypid.setPID(10.0,5.0,0.1)
i01.eyesTracking.xpid.setPID(15.0,5.0,0.1)
i01.eyesTracking.ypid.setPID(15.0,5.0,0.1)
############################################################

partypace = 1.0

i01.systemCheck()

# Hastighet vid start

i01.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
i01.setHeadSpeed(0.8, 0.8)
i01.mouth.speak("working on full speed")


##################################################################

# Input from the keyboard is routed here
def input(cmd):
    if (cmd == "P"):
        global millis
        interval = time.time() -  millis
        millis = time.time()
        global partypace
        partypace = (round(interval,2))
        print partypace
    if (cmd == "L"):
      global isRunning
      isRunning = True
        
    if (cmd == "S"):
      global isRunning
      isRunning = False
               
# Method to blink the leds and sleep for a moment.
def led():
    left.digitalWrite(42, 1) # ON
    left.digitalWrite(43, 0) # OFF
    left.digitalWrite(44, 1) # ON
    left.digitalWrite(45, 1) # ON
    sleep(0.2)   
    left.digitalWrite(42, 0) # OFF
    left.digitalWrite(43, 0) # OFF
    left.digitalWrite(44, 0) # OFF
    left.digitalWrite(45, 0) # OFF
    sleep (partypace - 0.2)

# Main program Loop
while True:
   if isRunning == True:
     # If we're running. flip the led()  (this method will block the correct amount of time)
     led()
   else:
     # keep the CPU from going crazy.
     sleep (partypace)
     
