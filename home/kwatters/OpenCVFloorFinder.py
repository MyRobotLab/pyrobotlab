from org.myrobotlab.opencv  import OpenCVFilterFloorFinder

# create the OpenCV service
opencv = Runtime.createAndStart("opencv", "OpenCV")

# create the floor finder filter
floorFinder = OpenCVFilterFloorFinder("floorFinder")

# specify the settings on the floor finder
floorFinder.updateUpDiff(3,3,3)
floorFinder.updateLoDiff(3,3,3)
floorFinder.updateFillColor(255,255,255)

# add the filter to open CV
opencv.addFilter(floorFinder)

# start the camera
opencv.capture()
