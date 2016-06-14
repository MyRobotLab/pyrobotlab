#file : InMoov2.FingerStarter with voice control.py

# this will run with versions of MRL 1.0.107
# a very minimal script for InMoov
# although this script is very short you can still
# do voice control of a finger box
# for any command which you say - you will be required to say a confirmation
# e.g. you say -> open finger, InMoov will ask -> "Did you say open finger?", you will need to 
# respond with a confirmation ("yes","correct","yeah","ya")

rightPort = "COM7"

i01 = Runtime.createAndStart("i01", "InMoov")
i01.startEar()
##############
i01.startRightHand(rightPort)
# tweaking defaults settings of right hand
#i01.rightHand.index.setMinMax(0,160)
#################

# verbal commands
ear = i01.ear

ear.addCommand("attach finger", "i01.rightHand.Index", "attach")
ear.addCommand("disconnect finger", "i01.rightHand.Index", "detach")
ear.addCommand("rest", i01.getName(), "rest")
ear.addCommand("open finger", "python", "fingeropen")
ear.addCommand("close finger", "python", "fingerclose")
ear.addCommand("finger to the middle", "python", "fingermiddle")
ear.addCommand("capture gesture", ear.getName(), "captureGesture")
ear.addCommand("manual", ear.getName(), "lockOutAllGrammarExcept", "voice control")
ear.addCommand("voice control", ear.getName(), "clearLock")
 
ear.addComfirmations("yes","correct","yeah","ya") 
ear.addNegations("no","wrong","nope","nah")

ear.startListening()

def fingeropen():
  i01.moveIndex("left",0,0,0,0,0)

def fingerclose():
  i01.moveIndex("left",180,180,180,180,180)

def fingermiddle():
  i01.moveIndex("left",90,90,90,90,90)