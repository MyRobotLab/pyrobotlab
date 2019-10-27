# Start a virtual Arduino as a placeholder for the Arduino references
leftvaport = "COM99"
leftva = Runtime.start("leftva","VirtualArduino")
leftva.connect(leftvaport)
# Start a Arduino service that connects to the virtual Arduino
leftard = Runtime.start("leftardleftarm.arduino","Arduino")
leftard.connect(leftvaport)
# Start the InMoovArm service
leftarm = Runtime.start("leftArm","InMoovArm")
# Start the servodrier
adaleft = Runtime.start("adaleft","Adafruit16CServoDriver")
# Start and attach the servodriver to Raspi 
raspi = Runtime.start("raspi","RasPi")
sleep(5)
adaleft.attach("raspi","1","0x40")
# Get a handle to each servo and attach to the pins of the servo driver
leftarmbiceps = Runtime.getService("leftArm.bicep")
leftarmbiceps.attach("adaleft",1)
#
leftarmrotate = Runtime.getService("leftArm.rotate")
leftarmrotate.attach("adaleft",2)
# And so on...

