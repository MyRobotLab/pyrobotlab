# A script to test opencv tracking in MyRobotLab with an Arduino connected to a Raspberry Pi 3
# as at mrl development build version 2489
# a mashup of code taken from Mats:
# https://github.com/MyRobotLab/pyrobotlab/blob/master/home/Mats/Tracking.py
# and also from Grog:
# http://myrobotlab.org/content/tracking-results
#

from org.myrobotlab.opencv import OpenCVFilterPyramidDown

#Define the x and y tracking servo pins 
#articulated neck servos

centreneckPin = 1 # vertical motion
mainneckPin = 2 # horizontal motion
xPin = 9; # horizontal motion
yPin = 10; # vertical motion

#set which camera to use. In my case, 0 references the Raspberry Pi camera
cameraIndex = 0

# set the port to which the Arduino is connected
arduinoPort = '/dev/ttyUSB0'

# start a tracker service instance
tracker = Runtime.start("tracker", "Tracking");

tracker.connect(arduinoPort, xPin, yPin, cameraIndex);

x = tracker.getX();
# invert if necessary
# x.setInverted(True);
x.setVelocity(20)
x.setMinMax(60,90)
#x.setInverted(True);
x.setRest(85)
x.rest()
 
y = tracker.getY();
y.setVelocity(20)
y.setInverted(True);
y.setMinMax(60,75)
y.setRest(70)
y.rest()



#start an Arduino service instance
#arduino = Runtime.start("tracker.controller","Arduino")

#define a tracker PID instance
pid = Runtime.start("tracker.pid","Pid")

#set the x and y PID values
#pid.setPID("x", 20.0, 5.0, 0.1);
#pid.setPID("y", 20.0, 5.0, 0.1);

opencv = Runtime.start("tracker.opencv","OpenCV")
pid.setPID("x", 5.0, 1.0, 0.1);
pid.setPID("y", 5.0, 1.0, 0.1);


#get the tracker opencv service instance
#opencv = Runtime.getService("tracker.opencv")
sleep(2);

#opencv.addFilter("PyramidDown1","PyramidDown")
#opencv.addFilter("Gray1","Gray")

#as at mrl development build 2423 this next piece is required on the Raspberry Pi (3) under javacv1.3 
#for opencv to return video frames
#frameGrabberType = "org.bytedeco.javacv.FFmpegFrameGrabber";
#opencv.captureFromResourceFile("/dev/video0");
#opencv.setFrameGrabberType(frameGrabberType);
#opencv.broadcastState();
#sleep(3);
#rest for a bit
#sleep(3);

tracker.y.setInverted(True);

# additional PyramidDown filter for improved framerate on the Pi (~15 fps)
PreFilterPyramidDown = OpenCVFilterPyramidDown("PreFilterPyramidDown") 
tracker.preFilters.add(PreFilterPyramidDown)
tracker.opencv.setDisplayFilter("PreFilterPyramidDown")

#start the opencv video frame capture
opencv.capture();

#opencv.addFilter("lkOpticalTrack1","LKOpticalTrack")
#opencv.setDisplayFilter("lkOpticalTrack1")
#sleep(1)
#opencv.invokeFilterMethod("lkOpticalTrack1","samplePoint",160,120)

#start tracking

#1# tracker.startLKTracking()
#2# tracker.findFace()
#3# tracker.faceDetect()


