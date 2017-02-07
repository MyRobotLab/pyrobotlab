#MARTY I2C PI
#SCRIPT BASED ON MATS WORK
#SCRIPT PUSHED INSIDE inmoovCustom : https://github.com/MyRobotLab/inmoov/tree/master/InmoovScript

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
eyes = Runtime.createAndStart("eyes", "Servo")
armLeft = Runtime.createAndStart("armLeft", "Servo")
armRight = Runtime.createAndStart("armRight", "Servo")
sleep(1)

ledBlue=14
ledRed=13
ledGreen=12

vitesse=80

cuisseDroiteRest=90
genouDroiteRest=90
chevilleDroiteRest=80
cuisseGaucheRest=97
genouGaucheRest=95
chevilleGaucheRest=90
armLeftRest=90
armRightRest=120
eyesRest=90

cuisseDroite.setRest(cuisseDroiteRest)
genouDroite.setRest(genouDroiteRest)
chevilleDroite.setRest(chevilleDroiteRest)
cuisseGauche.setRest(cuisseGaucheRest)
genouGauche.setRest(genouGaucheRest)
chevilleGauche.setRest(chevilleGaucheRest)
eyes.setRest(eyesRest)
eyes.map(0,180,66,100)
armLeft.setRest(armLeftRest)
armRight.setRest(armRightRest)


cuisseDroite.attach(adaFruit16c,0)
genouDroite.attach(adaFruit16c,1)
chevilleDroite.attach(adaFruit16c,2)
cuisseGauche.attach(adaFruit16c,4)
genouGauche.attach(adaFruit16c,5)
chevilleGauche.attach(adaFruit16c,15)
eyes.attach(adaFruit16c,8)
armLeft.attach(adaFruit16c,9)
armRight.attach(adaFruit16c,10)




eyes.setVelocity(-1)
armLeft.setVelocity(-1)
armRight.setVelocity(-1)



cuisseDroite.rest()
genouDroite.rest()
chevilleDroite.rest()
cuisseGauche.rest()
genouGauche.rest()
chevilleGauche.rest()
eyes.rest()
armLeft.rest()
armRight.rest()
sleep(2)

cuisseDroite.detach()
genouDroite.detach()
chevilleDroite.detach()
cuisseGauche.detach()
genouGauche.detach()
chevilleGauche.detach()
armLeft.detach()
armRight.detach()


def walk(step):
	talkBlocking("D'accord, c'est parti !")
	start(step)
	talk("Je m'aichauffe")
	cuisseDroite.attach()
	genouDroite.attach()
	chevilleDroite.attach()
	cuisseGauche.attach()
	genouGauche.attach()
	chevilleGauche.attach()
	genouGauche.attach()
	armLeft.attach()
	armRight.attach()
	cuisseDroite.setVelocity(vitesse)
	genouDroite.setVelocity(vitesse)
	chevilleDroite.setVelocity(vitesse)
	cuisseGauche.setVelocity(vitesse)
	genouGauche.setVelocity(vitesse)
	chevilleGauche.setVelocity(vitesse)

	for i in range(1,step) :
		armLeft.moveTo(50)
		armRight.moveTo(50)
		chevilleDroite.moveTo(chevilleDroiteRest+20)
		chevilleGauche.moveTo(chevilleGaucheRest+30)
		sleep(0.8)
		cuisseGauche.moveTo(cuisseDroiteRest+40)
		cuisseDroite.moveTo(chevilleDroiteRest-40)
		sleep(0.8)
		chevilleDroite.moveTo(chevilleDroiteRest-30)
		chevilleGauche.moveTo(chevilleGaucheRest-20)
		sleep(0.8)
		cuisseGauche.moveTo(cuisseGaucheRest)
		cuisseDroite.moveTo(chevilleDroiteRest)
		armLeft.moveTo(90)
		armRight.moveTo(90)
		sleep(0.8)


	cuisseDroite.detach()
	genouDroite.detach()
	chevilleDroite.detach()
	cuisseGauche.detach()
	genouGauche.detach()
	chevilleGauche.detach()
	eyes.detach()

def start(step):
	sleep(5)
	armLeft.attach()
	armRight.attach()
	armLeft.attach()
	eyes.attach()
	eyes.moveTo(180)
	armRight.moveTo(0)
	sleep(2)
	eyes.moveTo(0)
	armRight.moveTo(120)
	sleep(1)
	eyes.moveTo(180)
	sleep(0)
	eyes.moveTo(180)
	sleep(2)
	eyes.moveTo(0)
	armRight.moveTo(armRightRest)
	

adaFruit16c.setPinValue(7,0)
adaFruit16c.setPinValue(ledGreen,0)
adaFruit16c.setPinValue(ledRed,0)
adaFruit16c.setPinValue(ledBlue,0)
	
def red():
	adaFruit16c.setPinValue(7,0)
	adaFruit16c.setPinValue(ledGreen,1)
	adaFruit16c.setPinValue(ledRed,0)
	adaFruit16c.setPinValue(ledBlue,1)

def blue():
	adaFruit16c.setPinValue(7,0)
	adaFruit16c.setPinValue(ledGreen,1)
	adaFruit16c.setPinValue(ledRed,1)
	adaFruit16c.setPinValue(ledBlue,0)
	
def green():
	adaFruit16c.setPinValue(7,0)
	adaFruit16c.setPinValue(ledGreen,0)
	adaFruit16c.setPinValue(ledRed,1)
	adaFruit16c.setPinValue(ledBlue,1)

def noLed():
	adaFruit16c.setPinValue(ledGreen,0)
	adaFruit16c.setPinValue(ledRed,0)
	adaFruit16c.setPinValue(ledBlue,0)
	adaFruit16c.setPinValue(7,1)
	

red()
sleep(1)	
green()
sleep(1)
blue()
sleep(1)
noLed()


led = Runtime.start("led","Clock")
led.setInterval(100)
global i
i=0
def ledFunc(timedata):
	global i
	if i==0:
		red()
		i=1
	else:
		noLed()
		i=0
	led.setInterval(random.randint(10,100))

led.addListener("pulse", python.name, "ledFunc")
