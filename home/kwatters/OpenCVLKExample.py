from org.myrobotlab.opencv import OpenCVFilterLKOpticalTrack

#######################################################
# call back - all data from opencv will come back to this method
def onOpenCVData(data):
  # lots of data available.. this prints the points if available to the python console..
  print data.getPoints()

#######################################################
# Main entry point for script
#######################################################
# grab a handle to the current python service
python = Runtime.start("python","Python")
# start up opencv service
opencv = Runtime.start("opencv", "OpenCV")
# service specific config.. optional
# opencv.cameraIndex = 0
# opencv.height = 480
# opencv.width = 640
# create the lk tracking filter and add it to the opencv service
lkFilter = OpenCVFilterLKOpticalTrack("lkFilter")
opencv.addFilter(lkFilter)
# subscribe to the open cv callback 
# mapping is from publishOpenCVData to onOpenCVData by convention. 
python.subscribe("opencv", "publishOpenCVData")
# sleep(1)
opencv.capture()
# give a moment for the camera to warm up and stablize
sleep(10)
x=0.5
y=0.5
# manually start sampling a point  (additive to existing points)
lkFilter.samplePoint(x,y)
# track the point for 10 seconds
sleep(10)
# stop tracking the point.
# remove all points currently being tracked.
lkFilter.clearPoints()
