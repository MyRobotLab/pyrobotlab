# A script to test tracking on the Raspberry Pi driving servos with the AdaFruit16ServoDriver service
# as at mrl development build version 2423
# a mashup of code taken from Mats:
# https://github.com/MyRobotLab/pyrobotlab/blob/master/home/Mats/Tracking.py
# and also from Grog:
# http://myrobotlab.org/content/tracking-results
#


#start an AdaFruit16C I2C servo driver service
adaFruit16c1 = Runtime.createAndStart("AdaFruit16C1","Adafruit16CServoDriver")

#start a Raspberry Pi service
raspi = Runtime.createAndStart("RasPi","RasPi")

#attach the AdaFruit16C I2C servo driver to the Raspberry Pi
adaFruit16c1.setController("RasPi","1","0x40")

#set the frequency for the AdaFruit16C I2C servo driver to 50 Hz
adaFruit16c1.setPWMFreq(1,50)

#Define the AdaFruit16C I2C servo driver x and y tracking servo pins 
#articulated neck servos

centreneckPin = 1 # vertical motion
mainneckPin = 2 # horizontal motion
xPin = 1; # horizontal motion
yPin = 2; # vertical motion

#set which camera to use. In my case, 0 references the Raspberry Pi camera
cameraIndex = 0

# set the port to which the Arduino is connected
# We won't actually use the Arduino for servo connectivity, but this is here to make things worky for now
# The Virtual Arduino actually might be better here...
arduinoPort = '/dev/ttyUSB0'

#start an Arduino service instance
arduino = Runtime.start("tracker.controller","Arduino")

#define a tracker PID instance
pid = Runtime.start("tracker.pid","Pid")

#connect the arduino to the arduino port
arduino.connect(arduinoPort)

#rest for a bit
sleep(1)

#define the tracker x and y servo instances
x = Runtime.start("tracker.x","Servo")
y = Runtime.start("tracker.y","Servo")
# x.setInverted(True)
# y.setInverted(True)

#rest again
sleep(1)

#attach x servo to the AdaFruit16C servo driver, set servo limits, speed and rest position
x.attach(adaFruit16c1,mainneckPin,90,10)
x.setMinMax(30,160)
x.setRest(90)
x.rest()

#attach y servo to the AdaFruit16C servo driver, set servo limits, speed and rest position
y.attach(adaFruit16c1,centreneckPin,100,10)
y.setMinMax(90,160)
y.setRest(100)
y.rest()

# start a tracker service instance
tracker = Runtime.start("tracker","Tracking")

#set the x and y PID values
pid.setPID("x", 20.0, 5.0, 0.1);
pid.setPID("y", 20.0, 5.0, 0.1);

#get the tracker opencv service instance
opencv = Runtime.getService("tracker.opencv")

#as at mrl development build 2423 this next piece is required on the Raspberry Pi (3) under javacv1.3 
#for opencv to return video frames
frameGrabberType = "org.bytedeco.javacv.FFmpegFrameGrabber";
opencv.captureFromResourceFile("/dev/video0");
opencv.setFrameGrabberType(frameGrabberType);
#opencv.broadcastState();
#rest for a bit
sleep(3);

#start the opencv video frame capture
opencv.capture();

#opencv.addFilter("PyramidDown1","PyramidDown")
#opencv.addFilter("Gray1","Gray")
#opencv.addFilter("lkOpticalTrack1","LKOpticalTrack")
#opencv.setDisplayFilter("lkOpticalTrack1")
#sleep(1)
#opencv.invokeFilterMethod("lkOpticalTrack1","samplePoint",160,120)

#start tracking
tracker.faceDetect()
#tracker.startLKTracking()

#as at the time of writing, awaiting a possible logic change in the tracker.connect() logic
#to allow the tracker service to see the I2C connected servos

