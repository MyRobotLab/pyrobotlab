webgui = Runtime.createAndStart("WebGui","WebGui")
# Create and start the Arduino servicen and connect it to the serial port
arduino = Runtime.createAndStart("Arduino","Arduino")
arduino.connect("COM4")
# Start the Adafruit16CServodriver that can be used for all PCA9685 devices
# and connect it to the Arduino i2c interface using the default bus and
# address
adaFruit16c = Runtime.createAndStart("AdaFruit16C","Adafruit16CServoDriver")
adaFruit16c.setController("Arduino")
# create a new servo
thumb = Runtime.createAndStart("Thumb", "Servo")
elbow = Runtime.createAndStart("Elbow", "Servo")
# attach it to the pwm board - pin 3 & 8
thumb.attach(adaFruit16c,3)
elbow.attach(adaFruit16c,8)
# When this script has been executed you should be able to 
# move the servos using the GUI or using python
