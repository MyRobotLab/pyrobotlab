import threading

########################################
# The Walking Thread
# This is a thread that you can pass 
# an inmoov and a servo to.  It will
# start walking forward and animating in a loop
########################################
class WalkingThread(threading.Thread):
  # constructor for the thread, takes i01 and forwardServo
  def __init__(self,i01,forwardServo):
    super(WalkingThread, self).__init__()
    print "Here we are"
    self.forwardServo = forwardServo
    self.i01 = i01
    # initially the thread is not running.
    self.running = False
  # The thread is started this method runs  
  def run(self):
    # flip the state to running
    self.running = True
    # move the servo to go forward
    self.forwardServo.moveTo(60)
    # while we are running, animate
    while self.running:
      print "Walking..."
      sleep(2)
      print "Thread"
      sleep(2)
    # we are no longer running, move servo and relax.  
    print "Stopped"
    forwardServo.moveTo(93)
    self.relax()
    
  def relax(self):
    i01.rest()
 
#############################################################
# Main program entry point
#############################################################
# Configure com ports
leftPort = "COM15"
rightPort = "COM19"
# star the InMoov
i01 = Runtime.createAndStart("i01", "InMoov")
# tell the inmoov to be a quiet and obiedient slave.
i01.setMute(True)
# start the inmoov
i01.startAll(leftPort, rightPort)

forwardServo = Runtime.createAndStart("forwardServo", "Servo")
# TODO: attach the servo
# forwardServo.attach()

# Create a thread object that can be global ? 
walkingThread = WalkingThread(i01,forwardServo)
 
def heard(data):
  global walkingThread
  if (data == "go forward"):
    # start the walking thread.
    walkingThread.start()
  if (data == "kill the motor"):
    # tell the thread to stop so it breaks out of the loop
    walkingThread.running = False
        
