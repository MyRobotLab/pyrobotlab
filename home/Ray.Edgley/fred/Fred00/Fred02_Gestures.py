########################################
# Fred's Gestures
########################################
# This file contains the Gestures that have 
# been created to be used by various processes.

def GoToSleep():
   fred01.headX.rest()
   fred01.HeadY.moveTo(0.8*HeadY.getMin())
   
def WakeUpFromSleep():
   fred01.HeadY.rest()

def Yes():
   fred01.HeadY.moveTo(0.8*HeadY.getMax())
   sleep(0.5)
   fred01.HeadY.moveTo(0.8*HeadY.getMin())
   sleep(0.5)
   fred01.HeadY.moveTo(0.8*HeadY.getMax())
   sleep(0.5)
   fred01.HeadY.moveTo(0.8*HeadY.getMax())
   sleep(0.5)
   fred01.HeadY.moveTo(0.8*HeadY.getMin())
   sleep(0.5)
   fred01.HeadY.rest()

def No():
   fred01.HeadX.moveTo(0.8*HeadX.getMax())
   sleep(0.5)
   fred01.HeadX.moveTo(0.8*HeadX.getMin())
   sleep(0.5)
   fred01.HeadX.moveTo(0.8*HeadX.getMax())
   sleep(0.5)
   fred01.HeadX.moveTo(0.8*HeadX.getMax())
   sleep(0.5)
   fred01.HeadX.moveTo(0.8*HeadX.getMin())
   sleep(0.5)
   fred01.HeadX.rest()
