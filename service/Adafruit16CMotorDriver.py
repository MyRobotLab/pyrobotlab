# From version 1.0.2316 use attach instead of setController
# An example of how to use the Adafruit16CServoDriver to 
# drive a motor.
#
# Runtime.start("webgui", "WebGui");
arduino = Runtime.createAndStart("Arduino", "Arduino");
arduino.connect("COM3")
sleep(5)
ada = Runtime.createAndStart("Ada","Adafruit16CServoDriver")
# ada.setController(arduino,"1","0x40")
ada.attach(arduino,"1","0x40")
sleep(2)
motor01 = Runtime.createAndStart("motor01", "Motor");
motor01.setPwmPins(0,1);
motor01.attach(ada);
motor01.move(0.3);
