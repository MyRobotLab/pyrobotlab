#########################################
# Sabertooth.py
# categories: motor
# more info @: http://myrobotlab.org/service/Sabertooth
#########################################
# uncomment for virtual hardware
# virtual = True

port = "COM14"

# start optional virtual serial service, used for test
if ("virtual" in globals() and virtual):
    # use static method Serial.connectVirtualUart to create
    # a virtual hardware uart for the serial service to
    # connect to
    uart = Serial.connectVirtualUart(port)
    uart.logRecv(true) # dump bytes sent from sabertooth

# start the services
sabertooth = Runtime.start("sabertooth","Sabertooth")
m1 = Runtime.start("m1","MotorPort")
m2 = Runtime.start("m2","MotorPort")
joy = Runtime.start("joy","Joystick")

# configure services
m1.setPort("m1")
m2.setPort("m2")

# attach services
sabertooth.attach(m1)
sabertooth.attach(m2)

# FIXME - sabertooth.attach(motor1) & sabertooth.attach(motor2)
# FIXME - motor1.attach(joystick) !
sabertooth.connect(port)

m1.stop();
m2.stop();

# speed up the motor
for x in range(0,100):
  pwr = x * .01
  print('power ', pwr)
  m1.move(pwr)
  sleep(0.01)

sleep(1)

# slow down the motor
for x in range(100, -1, -1):
  pwr = x * .01
  print('power ', pwr)
  m1.move(pwr)
  sleep(0.01)

# move motor clockwise
m1.move(0.3)
sleep(1)
m1.stop()

# move motor counter-clockwise
m1.move(-0.3)
sleep(1)
m1.stop()
