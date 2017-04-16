##################################################################
# Leap Motion Example Script
##################################################################
import csv
# when leap motion data is detected, it will be passed in here
def onLeapData(data):
  # process the data that came in.
  # right hand first
  #create file
  global writer
  f = open("Index.csv", "wb")
  writer = csv.writer(f)
  
  if (data.rightHand):
    # if the data has a right hand, print out some info about it.
    print("Right Index =" + str(data.rightHand.index))
    # update a position of
    columns = [ data.rightHand.thumb, 
                data.rightHand.index, 
                data.rightHand.middle,
                data.rightHand.ring,
                data.rightHand.pinky,
                data.rightHand.posX,
                data.rightHand.posY,
                data.rightHand.posZ ]
    writer.writerow(columns)
    
  else:
    # the right hand wasn't found.
    print("Right hand not detected.")
  # left hand data.
  
  if (data.frame):
    # this is the raw frame info from the leap if you want it.
    print(str(frame))
    
###########################################################
# MAIN Script entry point
###########################################################

# create the leap motion service
leap = Runtime.createAndStart("leap","LeapMotion")
# connect python as a listener for the onLeapData callback
leap.addLeapDataListener(python)
# start the leap motion watching for valid frames.
leap.startTracking()




