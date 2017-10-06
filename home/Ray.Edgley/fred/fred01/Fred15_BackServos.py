#########################################################
# Fred15 Setup the Back Servos
#########################################################
# We will be using the following services:
#    Servo Service
#########################################################
# In Freds back we have the Servo Controller allocated to handle
# all the servos not otherwise covered by the head or arms
# That leave the headY for tilting the head up and down, headRoll,
# Both Left and Right Omoplates and the Left and Right Shoulder rotators
# There is also the stomach servo in both the Top for left and right tilt 
# of the body and mid for the body rotation

# Lets start with the headY servo.
# First we need to create the Servo Service using the Runtime Service
headY = Runtime.createAndStart("headY", "Servo")

# the servo is connected to, in this case pin 8
headY.attach(back,8)

# Now we tell the Servo Service about our servos limits, in some cases if the servo goes to far, things will break
headY.setMinMax(0,180)

# This allows you to map the input to the Servo service to an actual servo position output
headY.map(0,180,1,180)

# there is a rest command that can be issued to the servo, 
# when that happens, this is the position that the servo will go to
headY.setRest(90)

# if your servo run backwards, then set this to true in order to reverse it.
headY.setInverted(True)

# degrees per second rotational velocity, setting -1 will set the speed to the servo's default
headY.setVelocity(70)

# this allows the Servo Sevice to turn off the motor when it has reached the target position.
# the major advantage to this is the servos will use less power and have a lower chance of buring out.
headY.setAutoDisable(True)

# Ok now that we have fully defined the headX servo lets make sure it is in the rest position.
headY.rest()

# commands not used here but will be in other parts on the program are the following:
# headY.moveTo(x) where x is the position you want move to.
# headY.moveToBlockig(x) as above except execution of the program will pause until the position is reached.
# headY.disable() will turn off the servo without unloading the service.
# headY.enable() the oposite of disable will turn the servo back on after being disabled.
# disable and enable are not required if setAutoDisable is set to True

# For each servo that we have, we need to create a Servo Service, so this will be a process
# of repeating what we did above for each servo just using a diferent object name.
headRoll = Runtime.createAndStart("headRoll", "Servo")
headRoll.attach(back,9)
headRoll.setMinMax(45,135)
headRoll.map(0,180,1,180)
headRoll.setRest(90)
headRoll.setInverted(True)
headRoll.setVelocity(60)
headRoll.setAutoDisable(True)
headRoll.rest()

backTopStomach = Runtime.createAndStart("backTopStomach", "Servo")
backTopStomach.attach(back,10)
backTopStomach.setMinMax(0,180)
backTopStomach.map(0,180,1,180)
backTopStomach.setRest(90)
backTopStomach.setInverted(False)
backTopStomach.setVelocity(60)
backTopStomach.setAutoDisable(True)
backTopStomach.rest()

backMidStomach = Runtime.createAndStart("backMidStomach", "Servo")
backMidStomach.attach(back,11)
backMidStomach.setMinMax(0,180)
backMidStomach.map(0,180,1,180)
backMidStomach.setRest(90)
backMidStomach.setInverted(False)
backMidStomach.setVelocity(60)
backMidStomach.setAutoDisable(True)
backMidStomach.rest()

backRightOmo = Runtime.createAndStart("backRightOmo", "Servo")
backRightOmo.attach(back,0)
backRightOmo.setMinMax(115,180)
backRightOmo.setRest(120)
backRightOmo.map(0,180,1,180)
backRightOmo.setRest(90)
backRightOmo.setInverted(False)
backRightOmo.setVelocity(60)
backRightOmo.setAutoDisable(True)
backRightOmo.rest()

backRightShoulder = Runtime.createAndStart("backRightShoulder", "Servo")
backRightShoulder.attach(back,1)
backRightShoulder.setMinMax(0,180)
backRightShoulder.setRest(5)
backRightShoulder.map(0,180,1,180)
backRightShoulder.setRest(90)
backRightShoulder.setInverted(False)
backRightShoulder.setVelocity(60)
backRightShoulder.setAutoDisable(True)
backRightShoulder.rest()

backLeftOmo = Runtime.createAndStart("backLeftOmo", "Servo")
backLeftOmo.attach(back,15)
backLeftOmo.setMinMax(118,180)
backLeftOmo.setRest(120)
backLeftOmo.map(0,180,1,180)
backLeftOmo.setRest(90)
backLeftOmo.setInverted(False)
backLeftOmo.setVelocity(60)
backLeftOmo.setAutoDisable(True)
backLeftOmo.rest()

backLeftShoulder = Runtime.createAndStart("backLeftShoulder", "Servo")
backLeftShoulder.attach(back,14)
backLeftShoulder.setMinMax(0,180)
backLeftShoulder.setRest(5)
backLeftShoulder.map(0,180,1,180)
backLeftShoulder.setRest(90)
backLeftShoulder.setInverted(False)
backLeftShoulder.setVelocity(60)
backLeftShoulder.setAutoDisable(True)
backLeftShoulder.rest()
