leap = Runtime.start("leap","LeapMotion")
 
leap.addLeapDataListener(python)
 
def onLeapData(data):
  print (data.rightHand.index)
 
leap.startTracking()
