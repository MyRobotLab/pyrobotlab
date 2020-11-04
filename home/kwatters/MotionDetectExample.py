from org.myrobotlab.opencv import OpenCVFilterMotionDetect


# This is the callback method that will get the notification.
def onMotionDetected(rects):
  print "Hello birdie!"
  for rect in rects:
    print rect.x()
    print rect.y()
    print rect.width()
    print rect.height()

# start the OpenCV service
opencv =  Runtime.createAndStart("opencv", "OpenCV")

# Create the motion detection filter.
md = OpenCVFilterMotionDetect("motion")
opencv.addFilter(md)

# Wire the callback for the motion detection.
opencv.addListener("publishMotionDetected", "python", "onMotionDetected");

# Start the camera.
opencv.capture()


## TODO: subscribe to the publishMotion callback.

# ik.addListener("publishJointAngles", leftArm.getName(), "onJointAngles")

