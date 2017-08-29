#file : InMoov2.FingerStarter with voice control.py

# this will run with versions of MRL 1.0.107
# a very minimal script for InMoov
# although this script is very short you can still
# do voice control of a finger box
# for any command which you say - you will be required to say a confirmation
# e.g. you say -> open finger, InMoov will ask -> "Did you say open finger?", you will need to 
# respond with a confirmation ("yes","correct","yeah","ya")
#The "finger" is the index of the hand
#index Arduino connection pin 3

rightPort = "COM7"

i01 = Runtime.createAndStart("i01", "InMoov")
i01.startEar()
#################
i01.startMouth()
i01.mouth.setGoogleURI("http://thehackettfamily.org/Voice_api/api2.php?voice=Ryan&txt=")
##############
i01.startRightHand(rightPort)
# tweaking defaults settings of right hand index
i01.rightHand.index.setMinMax(0,180)
i01.rightHand.index.map(0,180,35,140)

# verbal commands
ear = i01.ear

ear.addCommand("attach right hand", "i01.rightHand", "attach")
ear.addCommand("disconnect right hand", "i01.rightHand", "detach")
ear.addCommand("attach finger", "i01.rightHand.index", "attach")
ear.addCommand("disconnect finger", "i01.rightHand.index", "detach")
ear.addCommand("open finger", "python", "fingeropen")
ear.addCommand("close finger", "python", "fingerclose")
ear.addCommand("finger to the middle", "python", "fingermiddle")
ear.addCommand("rest", i01.getName(), "rest")
ear.addCommand("capture gesture", ear.getName(), "captureGesture")
ear.addCommand("manual", ear.getName(), "lockOutAllGrammarExcept", "voice control")
ear.addCommand("voice control", ear.getName(), "clearLock")
 
ear.addComfirmations("yes","correct","yeah","ya") 
ear.addNegations("no","wrong","nope","nah")

ear.startListening()

def fingeropen():
  i01.moveHand("right",0,0,0,0,0,0)

def fingerclose():
  i01.moveHand("right",0,180,0,0,0,0)

def fingermiddle():
  i01.moveHand("right",0,90,0,0,0,0)