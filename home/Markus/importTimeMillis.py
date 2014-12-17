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
 
 
####################################################################
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
#to tweak the default PID values
i01.headTracking.xpid.setPID(10.0,5.0,0.1)
i01.headTracking.ypid.setPID(10.0,5.0,0.1)
i01.eyesTracking.xpid.setPID(15.0,5.0,0.1)
i01.eyesTracking.ypid.setPID(15.0,5.0,0.1)
############################################################
 
i01.systemCheck()
 
# Hastighet vid start
 
i01.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
i01.setHeadSpeed(0.8, 0.8)
i01.mouth.speak("working on full speed")
 
 
##################################################################
 
 
def input(cmd):
    global millis
    
 
    if (cmd == "C"):
        i01.captureGesture()
    
    if (cmd == "A"):
        i01.mouth.audioFile.playFile("C:\Users\Markus\Music\little teapot.mp3", False)
        millis = time.time()
    
    if (cmd == "S"):
       interval = time.time() -  millis
       millis = time.time()
       print ("    sleep(" + str(round(interval,2) - (0.2)) + ")")
       print ("    i01.head.jaw.moveTo(50)")
       print ("    sleep(0.2)")
       print ("    i01.head.jaw.moveTo(10)")
       i01.head.jaw.moveTo(50)
       sleep(0.2)
       i01.head.jaw.moveTo(10)
 
 
    if (cmd == "1"):
       interval = time.time() -  millis
       millis = time.time()
       print ("    sleep(" + str(round(interval,2)) + ")")
       print ('    i01.moveArm("right",90,40,30,46)')
       i01.moveArm("right",90,40,30,46)
 
    if (cmd == "2"):
       interval = time.time() -  millis
       millis = time.time()
       print ("    sleep(" + str(round(interval,2)) + ")")
       print ('    i01.moveArm("left",90,150,30,65)')
       i01.moveArm("left",90,150,30,65)
 
 
    if (cmd == "3"):
       interval = time.time() -  millis
       millis = time.time()
       print ("    sleep(" + str(round(interval,2)) + ")")
       print ("    i01.moveTorso(117,90,90)")
       i01.moveTorso(117,90,90)
 
    if (cmd == "4"):
       interval = time.time() -  millis
       millis = time.time()
       print ("    sleep(" + str(round(interval,2)) + ")")
       print ("    i01.moveTorso(86,90,90)")
       i01.moveTorso(86,90,90)
 
 
    if (cmd == "5"):
       interval = time.time() -  millis
       millis = time.time()
       print ("    sleep(" + str(round(interval,2)) + ")")
       print ('    i01.moveArm("left",5,90,30,10)')
       print ('    i01.moveArm("right",5,90,30,10)')
       i01.moveArm("left",5,90,30,10)
       i01.moveArm("right",5,90,30,10)