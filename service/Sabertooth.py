#########################################
# Sabertooth.py
# categories: motor
# more info @: http://myrobotlab.org/service/Sabertooth
#########################################
# uncomment for virtual hardware
# virtual = True

port = "COM99"

# start optional virtual serial service, used for test
if ("virtual" in globals() and virtual):
    # use static method Serial.connectVirtualUart to create
    # a virtual hardware uart for the serial service to
    # connect to
    uart = Serial.connectVirtualUart(port)
    uart.logRecv(true) # dump bytes sent from sabertooth

# start the services
sabertooth = Runtime.start("sabertooth","Sabertooth")
serial = Runtime.start("serial","Serial")
m1 = Runtime.start("m1","MotorPort")
m2 = Runtime.start("m2","MotorPort")
# joy = Runtime.start("joy","Joystick")

# configure & attach services
sabertooth.attach(serial)
m1.setPort("m1")
m2.setPort("m2")

# FIXME - sabertooth.attach(motor1) & sabertooth.attach(motor2)
# FIXME - motor1.attach(joystick) !

sabertooth.connect(port)

for x in range(0,120):
  print('power ', x)
  sabertooth.driveForwardMotor1(x)
  sleep(0.5)

sleep(1)

for x in range(120, -1, -1):
  print('power ', x)
  sabertooth.driveForwardMotor2(x)
  sleep(0.5)
