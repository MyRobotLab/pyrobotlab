#########################################################
# Fred12 Setup the Head Servos
#########################################################
# We will be using the following services:
#    Servo Service
#########################################################
# In Fred's head, we have a Servo to turn the head from side to side (HeadX), a Jaw Servo for the mouth
# to open and close and servos to control the eyes.
# Lets look at the HeadX servo first
# First we need to create a Servo Service, like all the other Services, we do this using the Runtime Sevice
headX = Runtime.createAndStart("headX", "Servo")

# Next we need to attach ther servo Service to a Controller Service, in this case it  will be the head
# Adafruit16ChServoDriver. We also need to tell the Servo Service which pin on the controller
# the servo is connected to, in this case pin 3
headX.attach(head,3)

# Now we tell the Servo Service about our servos limits, in some cases if the servo goes to far, things will break
headX.setMinMax(0,180)

# This allows you to map the input to the Servo service to an actual servo position output
headX.map(0,180,1,180)

# there is a rest command that can be issued to the servo, 
# when that happens, this is the position that the servo will go to
headX.setRest(90)

# if your servo run backwards, then set this to true in order to reverse it.
headX.setInverted(True)

# degrees per second rotational velocity, setting -1 will set the speed to the servo's default
headX.setVelocity(60)

# this allows the Servo Sevice to turn off the motor when it has reached the target position.
# the major advantage to this is the servos will use less power and have a lower chance of buring out.
headX.setAutoDisable(True)

# Ok now that we have fully defined the headX servo lets make sure it is in the rest position.
headX.rest()

# commands not used here but will be in other parts on the program are the following:
# headX.moveTo(x) where x is the position you want move to.
# headX.moveToBlockig(x) as above except execution of the program will pause until the position is reached.
# headX.disable() will turn off the servo without unloading the service.
# headX.enable() the oposite of disable will turn the servo back on after being disabled.
# disable and enable are not required if setAutoDisable is set to True

# For each servo that we have, we need to create a Servo Service
jaw = Runtime.createAndStart("jaw", "Servo")
jaw.attach(head,2)
jaw.setMinMax(90,165)
jaw.map(90,166,90,165)
jaw.setRest(160)
jaw.setInverted(True)
jaw.setVelocity(-1)
jaw.setAutoDisable(True)
jaw.rest()

eyesX = Runtime.createAndStart("eyesX", "Servo")
eyesX.attach(head,0)
eyesX.setMinMax(0,180)
eyesX.map(0,180,0,180)
eyesX.setRest(90)
eyesX.setInverted(False)
eyesX.setVelocity(-1)
eyesX.setAutoDisable(True)

eyesY = Runtime.createAndStart("eyesY", "Servo")
eyesY.attach(head,1)
eyesY.setMinMax(0,180)
eyesY.map(0,180,0,180)
eyesY.setRest(90)
eyesY.setInverted(False)
eyesY.setVelocity(-1)
eyesY.setAutoDisable(True)
