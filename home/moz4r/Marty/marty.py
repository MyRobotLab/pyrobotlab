#MARTY I2C PI SERVO TEST
#SCRIPT BASED ON MATS WORK
from time import sleep
raspi = Runtime.createAndStart("RasPi","RasPi")
adaFruit16c = Runtime.createAndStart("AdaFruit16C","Adafruit16CServoDriver")
adaFruit16c.setController("RasPi","1","0x40")
#
# This part is common for both devices and creates two servo instances
# on port 3 and 8 on the Adafruit16CServoDriver
# Change the names of the servos and the pin numbers to your usage
thumb = Runtime.createAndStart("Thumb", "Servo")
sleep(1)
thumb.setVelocity(30)
# attach it to the pwm board - pin 3 & 8
thumb.attach(adaFruit16c,0)
thumb.moveTo(90)
sleep(1)
thumb.setVelocity(10)
thumb.moveTo(180)
sleep(5)
thumb.detach()
sleep(5)
thumb.attach(adaFruit16c,0)
thumb.moveTo(90)