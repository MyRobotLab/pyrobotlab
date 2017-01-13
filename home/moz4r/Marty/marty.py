#MARTY I2C PI
#SCRIPT BASED ON MATS WORK
from time import sleep
raspi = Runtime.createAndStart("RasPi","RasPi")
adaFruit16c = Runtime.createAndStart("AdaFruit16C","Adafruit16CServoDriver")
adaFruit16c.setController("RasPi","1","0x40")
#
# This part is common for both devices and creates two servo instances
# on port 3 and 8 on the Adafruit16CServoDriver
# Change the names of the servos and the pin numbers to your usage
cuisseDroite = Runtime.createAndStart("cuisseDroite", "Servo")
genouDroite = Runtime.createAndStart("genouDroite", "Servo")
chevilleDroite = Runtime.createAndStart("chevilleDroite", "Servo")
cuisseGauche = Runtime.createAndStart("cuisseGauche", "Servo")
genouGauche = Runtime.createAndStart("genouGauche", "Servo")
chevilleGauche = Runtime.createAndStart("chevilleGauche", "Servo")
sleep(1)


cuisseDroiteRest=90
genouDroiteRest=90
chevilleDroiteRest=80
cuisseGaucheRest=97
genouGaucheRest=95
chevilleGaucheRest=90

cuisseDroite.setRest(cuisseDroiteRest)
genouDroite.setRest(genouDroiteRest)
chevilleDroite.setRest(chevilleDroiteRest)
cuisseGauche.setRest(cuisseGaucheRest)
genouGauche.setRest(genouGaucheRest)
chevilleGauche.setRest(chevilleGaucheRest)



cuisseDroite.attach(adaFruit16c,0)
sleep(1)
genouDroite.attach(adaFruit16c,1)
sleep(1)
chevilleDroite.attach(adaFruit16c,2)
sleep(1)
cuisseGauche.attach(adaFruit16c,4)
sleep(1)
genouGauche.attach(adaFruit16c,5)
sleep(1)
chevilleGauche.attach(adaFruit16c,6)
sleep(1)

cuisseDroite.enableAutoAttach(1)
genouDroite.enableAutoAttach(1)
chevilleDroite.enableAutoAttach(1)
cuisseGauche.enableAutoAttach(1)
genouGauche.enableAutoAttach(1)
chevilleGauche.enableAutoAttach(1)



cuisseDroite.setVelocity(30)
genouDroite.setVelocity(30)
chevilleDroite.setVelocity(30)
cuisseGauche.setVelocity(30)
genouGauche.setVelocity(30)
chevilleGauche.setVelocity(30)


cuisseDroite.rest()
genouDroite.rest()
chevilleDroite.rest()
cuisseGauche.rest()
genouGauche.rest()
chevilleGauche.rest()

sleep(3)


chevilleDroite.moveTo(chevilleDroiteRest+30)
chevilleGauche.moveTo(chevilleGaucheRest+40)
sleep(3)
cuisseGauche.moveTo(cuisseGaucheRest+40)
sleep(3)
chevilleDroite.moveTo(chevilleDroiteRest)
chevilleGauche.moveTo(chevilleGaucheRest)
sleep(3)
cuisseGauche.rest()
sleep(5)



cuisseDroite.rest()
genouDroite.rest()
chevilleDroite.rest()
cuisseGauche.rest()
genouGauche.rest()
chevilleGauche.rest()
