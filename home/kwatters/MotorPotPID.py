##########################################
# Example of using a PID controller to 
# a joint angle using a 12 DC motor and 
# a linear trim rotary potentiometer.
##########################################
from org.myrobotlab.service import Runtime
from org.myrobotlab.service import Arduino
from time import sleep

# these are D6,D7 for 2 PWM motor control
pwmPin = 6
dirPin = 7
# this is "A7" on the Arduino Mega
potPin = 61

# port = "/dev/ttyACM0"
port = "COM31"

# to help avoid buffer overruns when sampling data from the arduino
sampleRate = 25

# Runtime.start("webgui", "WebGui")
# Start the Arduino
arduino = Runtime.start("arduino", "Arduino")
arduino.connect(port)
# a slight pause to let the arduino connect (maybe not necessary)
sleep(2)
# set up the motor control pins to be output
arduino.pinMode(pwmPin, Arduino.OUTPUT)
arduino.pinMode(dirPin, Arduino.OUTPUT)
# set the analog pin to be an input pin
arduino.pinMode(potPin, Arduino.INPUT)
# set the sample rate for the analog pins
arduino.setSampleRate(sampleRate)
arduino.analogReadPollingStart(potPin)
# start the motor service and attach it to the arduino
m1 = Runtime.start("m1", "Motor");
m1.setTypeSimple(pwmPin, dirPin);
m1.attach(arduino)
# create a PID2 service.
pid = Runtime.start("pid", "PID2")
# a name for my PID control
key = "test"
# set the pid parameters KP KI KD  (for now just porportial control)
pid.setPID(key, 0.002, 0.00, 0.00)
direction = 1
pid.setControllerDirection(key, direction)
pid.setMode(key, 1)
# clip the output values from the pid control to a range between -1 and 1. 
pid.setOutputRange(key, -1.0, 1.0)
# This is the desired sample value from the potentiometer 512 = ~ 90 degrees
desiredValue = 512
pid.setSetpoint(key, desiredValue)
pid.setSampleTime(key, 40)

# a helper callback function when data is published from the 
# potentiometer on the arduino wire it into the input of the PID controller
def input(pinData):
    global pid
    global key
    global desiredValue
    global m1
    print "PIN DATA:"+str(pinData)
    pid.setInput(key,pinData.value)
    pid.compute(key)
    output = pid.getOutput(key)
    print "PID OUTPUT: " + str(output)
    # we need to use the output to control the velocity of 
    m1.move(output)
    
# attach our callback 
arduino.addListener("publishPin", "python", "input")

# That's all folks!
