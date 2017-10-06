#########################################################
# Fred13 Setup the Right Arm Servos
#########################################################
# We will be using the following services:
#    Servo Service
#########################################################
# I Fred's Right Arm, we have the Bicep Rotator, the Elbow, 
# the Wrist and the five fingures
# Lets start with the Bicep Rotator.
# All service are created using the Runtime Service.
rightBicep = Runtime.createAndStart("rightBicep", "Servo")

# Next we need to attach ther servo Service to a Controller Service, in this case it  will be the head
# Adafruit16ChServoDriver. We also need to tell the Servo Service which pin on the controller
# the servo is connected to, in this case pin 15
rightBicep.attach(rightArm,15)

# Now we tell the Servo Service about our servos limits, in some cases if the servo goes to far, things will break
rightBicep.setMinMax(0,180)

# This allows you to map the input to the Servo service to an actual servo position output
rightBicep.map(0,180,1,180)

# there is a rest command that can be issued to the servo, 
# when that happens, this is the position that the servo will go to
rightBicep.setRest(90)

# if your servo run backwards, then set this to true in order to reverse it.
rightBicep.setInverted(False)

# degrees per second rotational velocity, setting -1 will set the speed to the servo's default
rightBicep.setVelocity(60)

# this allows the Servo Sevice to turn off the motor when it has reached the target position.
# the major advantage to this is the servos will use less power and have a lower chance of buring out.
rightBicep.setAutoDisable(True)

# Ok now that we have fully defined the headX servo lets make sure it is in the rest position.
rightBicep.rest()

# commands not used here but will be in other parts on the program are the following:
# rightBicep.moveTo(x) where x is the position you want move to.
# rightBicep.moveToBlockig(x) as above except execution of the program will pause until the position is reached.
# rightBicep.disable() will turn off the servo without unloading the service.
# rightBicep.enable() the oposite of disable will turn the servo back on after being disabled.
# disable and enable are not required if setAutoDisable is set to True

# For each servo that we have, we need to create a Servo Service, so this will be a process
# of repeating what we did above for each servo just using a diferent object name.
rightElbow = Runtime.createAndStart("rightElbow", "Servo")
rightElbow.attach(rightArm,14)
rightElbow.setMinMax(0,180)
rightElbow.map(0,180,1,180)
rightElbow.setRest(90)
rightElbow.setInverted(False)
rightElbow.setVelocity(60)
rightElbow.setAutoDisable(True)
rightElbow.rest()

rightWrist = Runtime.createAndStart("rightWrist", "Servo")
rightWrist.attach(rightArm,0)
rightWrist.setMinMax(0,180)
rightWrist.map(0,180,1,180)
rightWrist.setRest(90)
rightWrist.setInverted(False)
rightWrist.setVelocity(60)
rightWrist.setAutoDisable(True)
rightWrist.rest()

rightThumb = Runtime.createAndStart("rightThumb", "Servo")
rightThumb.attach(rightArm,1)
rightThumb.setMinMax(0,180)
rightThumb.map(0,180,1,180)
rightThumb.setRest(90)
rightThumb.setInverted(False)
rightThumb.setVelocity(60)
rightThumb.setAutoDisable(True)
rightThumb.rest()

rightIndex = Runtime.createAndStart("rightIndex", "Servo")
rightIndex.attach(rightArm,2)
rightIndex.setMinMax(0,180)
rightIndex.map(0,180,1,180)
rightIndex.setRest(90)
rightIndex.setInverted(False)
rightIndex.setVelocity(60)
rightIndex.setAutoDisable(True)
rightIndex.rest()

rightMajure = Runtime.createAndStart("rightMajure", "Servo")
rightMajure.attach(rightArm,3)
rightMajure.setMinMax(0,180)
rightMajure.map(0,180,1,180)
rightMajure.setRest(90)
rightMajure.setInverted(False)
rightMajure.setVelocity(60)
rightMajure.setAutoDisable(True)
rightMajure.rest()

rightRing = Runtime.createAndStart("rightRing", "Servo")
rightRing.attach(rightArm,4)
rightRing.setMinMax(0,180)
rightRing.map(0,180,1,180)
rightRing.setRest(90)
rightRing.setInverted(False)
rightRing.setVelocity(60)
rightRing.setAutoDisable(True)
rightRing.rest()

rightLittle = Runtime.createAndStart("rightLittle", "Servo")
rightLittle.attach(rightArm,5)
rightLittle.setMinMax(0,180)
rightLittle.map(0,180,1,180)
rightLittle.setRest(90)
rightLittle.setInverted(False)
rightLittle.setVelocity(60)
rightLittle.setAutoDisable(True)
rightLittle.rest()
