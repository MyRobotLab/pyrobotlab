PaupiereServoGauche = Runtime.start("PaupiereServoGauche","Servo")
PaupiereServoDroite = Runtime.start("PaupiereServoDroite","Servo")


PaupiereDroiteMINPaupiereInverted=PaupiereDroiteMIN
PaupiereDroiteMAXPaupiereInverted=PaupiereDroiteMAX
PaupiereGaucheMINPaupiereInverted=PaupiereGaucheMIN
PaupiereGaucheMAXPaupiereInverted=PaupiereGaucheMAX
if PaupiereInverted==1:
	PaupiereDroiteMIN=PaupiereDroiteMAXPaupiereInverted
	PaupiereDroiteMAX=PaupiereDroiteMINPaupiereInverted
	PaupiereGaucheMIN=PaupiereGaucheMAXPaupiereInverted
	PaupiereGaucheMAX=PaupiereGaucheMINPaupiereInverted
	

if IsInmoovArduino==1:
	PaupiereServoGauche.setMinMax(PaupiereGaucheMIN , PaupiereGaucheMAX)

	if PaupiereArduino=="left":
	  if IhaveEyelids==1 or IhaveEyelids==2:
		PaupiereServoGauche.attach(left, PaupiereGaucheServoPin)
	else:
	  if IhaveEyelids==1 or IhaveEyelids==2:
		PaupiereServoGauche.attach(right, PaupiereGaucheServoPin)

	if PaupiereArduino=="left":
	  if IhaveEyelids==2:
		
		PaupiereServoDroite.setMinMax(PaupiereDroiteMIN , PaupiereDroiteMAX)
		PaupiereServoDroite.attach(left, PaupiereDroiteServoPin)
	else:
	  if IhaveEyelids==2:
		
		PaupiereServoDroite.setMinMax(PaupiereDroiteMIN , PaupiereDroiteMAX)
		PaupiereServoDroite.attach(right, PaupiereDroiteServoPin)



	clock = Runtime.start("clock","Clock")
	clock.setInterval(1000)
	# define a ticktock method
	def clignement(timedata):
		PaupiereServoGauche.moveTo(PaupiereGaucheMIN)
		if IhaveEyelids==2:
			PaupiereServoDroite.moveTo(PaupiereDroiteMAX)
		sleep(0.12)
		PaupiereServoGauche.moveTo(PaupiereGaucheMAX)
		if IhaveEyelids==2:
			PaupiereServoDroite.moveTo(PaupiereDroiteMIN)
		
	#on fait un double clignement ou pas
		if random.randint(0,1)==1:
			sleep(0.2)
			PaupiereServoGauche.moveTo(PaupiereGaucheMIN)
			if IhaveEyelids==2:
				PaupiereServoDroite.moveTo(PaupiereDroiteMAX)
			sleep(0.12)
			PaupiereServoGauche.moveTo(PaupiereGaucheMAX)
			if IhaveEyelids==2:
				PaupiereServoDroite.moveTo(PaupiereDroiteMIN)
	#on redefini une valeur aleatoire pour le prochain clignement
		clock.setInterval(random.randint(10000,30000))
	#create a message routes
	clock.addListener("pulse", python.name, "clignement")
	# start the clock
	clock.startClock()