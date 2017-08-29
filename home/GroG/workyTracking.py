useVirtualArduino = True;

xPin = 9;
yPin = 6;
arduinoPort = "COM5";
cameraIndex = 0;
# using Sarxos for usb webcam, the other frame grabbers only worked on my integrated camera
frameGrabberType = "org.myrobotlab.opencv.SarxosFrameGrabber";

Runtime.start("gui", "SwingGui");

if useVirtualArduino:
  virtual = Runtime.start("virtual", "VirtualArduino");
  virtual.connect(arduinoPort);


t01 = Runtime.start("t01", "Tracking");
x = t01.getX();
# invert if necessary
# x.setInverted(True);

y = t01.getY();
# invert if necessary
# y.setInverted(True);

t01.connect(arduinoPort, xPin, yPin, cameraIndex);
opencv = t01.getOpenCV();
# noticed some swing display issues - I don't think Sarxos gets updated to display
opencv.setFrameGrabberType(frameGrabberType);
opencv.broadcastState();

# not sure if necessary - but get things to settle for 3 seconds
# before starting tracking
sleep(3);
# do lk optical point tracking
# t01.startLKTracking();
# do face tracking
t01.faceDetect();
