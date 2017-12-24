#########################################################
# Fred14 Setup the Left Arm Servos
#########################################################
# We will be using the following services:
#    Servo Service
#########################################################
# I Fred's Left Arm, we have the Bicep Rotator, the Elbow, 
# the Wrist and the five fingures. 
# You know it's just like the Right Arm
# Lets start with the Bicep Rotator.
# All service are created using the Runtime Service.
leftBicep = Runtime.createAndStart("leftBicep", "Servo")

# Next we need to attach ther servo Service to a Controller Service, in this case it  will be the head
# Adafruit16ChServoDriver. We also need to tell the Servo Service which pin on the controller
# the servo is connected to, in this case pin 15
leftBicep.attach(leftArm,15)

# Now we tell the Servo Service about our servos limits, in some cases if the servo goes to far, things will break
leftBicep.setMinMax(0,180)

# This allows you to map the input to the Servo service to an actual servo position output
leftBicep.map(0,180,1,180)

# there is a rest command that can be issued to the servo, 
# when that happens, this is the position that the servo will go to
leftBicep.setRest(90)

# if your servo run backwards, then set this to true in order to reverse it.
leftBicep.setInverted(False)

# degrees per second rotational velocity, setting -1 will set the speed to the servo's default
leftBicep.setVelocity(60)

# this allows the Servo Sevice to turn off the motor when it has reached the target position.
# the major advantage to this is the servos will use less power and have a lower chance of buring out.
leftBicep.setAutoDisable(True)

# Ok now that we have fully defined the headX servo lets make sure it is in the rest position.
leftBicep.rest()

# commands not used here but will be in other parts on the program are the following:
# leftBicep.moveTo(x) where x is the position you want move to.
# leftBicep.moveToBlockig(x) as above except execution of the program will pause until the position is reached.
# leftBicep.disable() will turn off the servo without unloading the service.
# leftBicep.enable() the oposite of disable will turn the servo back on after being disabled.
# disable and enable are not required if setAutoDisable is set to True

# For each servo that we have, we need to create a Servo Service, so this will be a process
# of repeating what we did above for each servo just using a diferent object name.
leftElbow = Runtime.createAndStart("leftElbow", "Servo")
leftElbow.attach(leftArm,14)
leftElbow.setMinMax(0,180)
leftElbow.map(0,180,1,180)
leftElbow.setRest(90)
leftElbow.setInverted(False)
leftElbow.setVelocity(60)
leftElbow.setAutoDisable(True)
leftElbow.rest()

leftWrist = Runtime.createAndStart("leftWrist", "Servo")
leftWrist.attach(leftArm,0)
leftWrist.setMinMax(0,180)
leftWrist.map(0,180,1,180)
leftWrist.setRest(90)
leftWrist.setInverted(False)
leftWrist.setVelocity(60)
leftWrist.setAutoDisable(True)
leftWrist.rest()

leftThumb = Runtime.createAndStart("leftThumb", "Servo")
leftThumb.attach(leftArm,1)
leftThumb.setMinMax(0,180)
leftThumb.map(0,180,1,180)
leftThumb.setRest(90)
leftThumb.setInverted(False)
leftThumb.setVelocity(60)
leftThumb.setAutoDisable(True)
leftThumb.rest()

leftIndex = Runtime.createAndStart("leftIndex", "Servo")
leftIndex.attach(leftArm,2)
leftIndex.setMinMax(0,180)
leftIndex.map(0,180,1,180)
leftIndex.setRest(90)
leftIndex.setInverted(False)
leftIndex.setVelocity(60)
leftIndex.setAutoDisable(True)
leftIndex.rest()

leftMajure = Runtime.createAndStart("leftMajure", "Servo")
leftMajure.attach(leftArm,3)
leftMajure.setMinMax(0,180)
leftMajure.map(0,180,1,180)
leftMajure.setRest(90)
leftMajure.setInverted(False)
leftMajure.setVelocity(60)
leftMajure.setAutoDisable(True)
leftMajure.rest()

leftRing = Runtime.createAndStart("leftRing", "Servo")
leftRing.attach(leftArm,4)
leftRing.setMinMax(0,180)
leftRing.map(0,180,1,180)
leftRing.setRest(90)
leftRing.setInverted(False)
leftRing.setVelocity(60)
leftRing.setAutoDisable(True)
leftRing.rest()

leftLittle = Runtime.createAndStart("leftLittle", "Servo")
leftLittle.attach(leftArm,5)
leftLittle.setMinMax(0,180)
leftLittle.map(0,180,1,180)
leftLittle.setRest(90)
leftLittle.setInverted(False)
leftLittle.setVelocity(60)
leftLittle.setAutoDisable(True)
leftLittle.rest()
