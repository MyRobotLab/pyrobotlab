#file : InMoov2.FingerStarter with voice control.py

# this will run with versions of MRL NIXIE
# a very minimal script for InMoov
# although this script is very short you can still
# do voice control of a finger servo
#The "finger" is the index finger of the hand
#index Arduino connection pin 3

i01_right = runtime.start('i01.right', 'Arduino')
i01_right.connect("COM9")

i01 = Runtime.start("i01", "InMoov2")
i01.startEar()
#################
i01_mouth = runtime.create('i01.mouth', 'MarySpeech')
i01_mouth.setVoice('Mark')
i01.startMouth()
##############
i01_rightHand = Runtime.start("i01.rightHand", "InMoov2Hand")
# tweaking defaults settings of right hand index
i01_rightHand_index.map(0,180,35,140)
i01_right.attach("i01.rightHand")
##############
i01.startChatBot()
##############
# verbal commands set in the chatbot
##############
# OPEN YOUR FINGER.
# CLOSE YOUR FINGER.
# FINGER TO THE MIDDLE.
# ACTION YOUR FINGER.
# OPEN HAND.
# CLOSE HAND.
# OPEN HANDS.
# CLOSE HANDS.
# OPEN YOUR RIGHT HAND.
# OPEN YOUR LEFT HAND.
# CLOSE YOUR RIGHT HAND.
# CLOSE YOUR LEFT HAND.
# SLOWLY CLOSE YOUR RIGHT HAND.


def fingeropen():
  #i01.moveHand("right",0,0,0,0,0,0)
  i01_rightHand_index.moveTo(0)

def fingerclose():
  #i01.moveHand("right",0,180,0,0,0,0)
  i01_rightHand_index.moveTo(180)

def fingermiddle():
  #i01.moveHand("right",0,90,0,0,0,0)
  i01_rightHand_index.moveTo(90)

def fingeraction():
   i01_rightHand_index.setSpeed(500)## High speed
   i01_rightHand_index.moveTo(0)
   i01_rightHand_index.moveTo(180)
   i01_rightHand_index.moveTo(0)
   i01_rightHand_index.moveTo(180)
   i01_rightHand_index.moveTo(0)
   i01_rightHand_index.moveTo(180)
   i01_rightHand_index.moveTo(0)
