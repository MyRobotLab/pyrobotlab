PaupiereServoGauche = Runtime.create("PaupiereServoGauche","Servo")
PaupiereServoDroite = Runtime.create("PaupiereServoDroite","Servo")


	
def PositionPaupiere(posGauche,posDroite,vitesse):
	if IsInmoovArduino==1:
		
		PaupiereServoGauche.setSpeed(vitesse)
		PaupiereServoDroite.setSpeed(vitesse)
		PaupiereAttach(1)
		PaupiereServoGauche.moveTo(posGauche)
		if IhaveEyelids==2:
			PaupiereServoDroite.moveTo(posDroite)
			
def PaupiereAttach(status):
	if IsInmoovArduino==1:
		if status==0:
			PaupiereServoGauche.detach()
			if IhaveEyelids==2:
				PaupiereServoDroite.detach()
		else:
			PaupiereServoGauche.attach()
			if IhaveEyelids==2:
				PaupiereServoDroite.attach()
			
PaupiereServoGauche.setMinMax(PaupiereGaucheMIN,PaupiereGaucheMAX) 
PaupiereServoDroite.setMinMax(PaupiereDroiteMIN,PaupiereDroiteMAX)
PaupiereServoGauche.map(0,180,PaupiereGaucheMIN,PaupiereGaucheMAX)
PaupiereServoDroite.map(0,180,PaupiereDroiteMAX,PaupiereDroiteMIN)

PaupiereServoGauche = Runtime.start("PaupiereServoGauche","Servo")
PaupiereServoDroite = Runtime.start("PaupiereServoDroite","Servo")

if PaupiereInverted==1:
	PaupiereServoGauche.map(0,180,PaupiereGaucheMAX,PaupiereGaucheMIN)
	PaupiereServoDroite.map(0,180,PaupiereDroiteMIN,PaupiereDroiteMAX)
	
if IsInmoovArduino==1:

	if PaupiereArduino=="left":
	  if IhaveEyelids==1 or IhaveEyelids==2:
		PaupiereServoGauche.attach(left, PaupiereGaucheServoPin, PaupiereGaucheMIN, 10000)
	else:
	  if IhaveEyelids==1 or IhaveEyelids==2:
		PaupiereServoGauche.attach(right, PaupiereGaucheServoPin, PaupiereGaucheMIN, 10000)

	if PaupiereArduino=="left":
	  if IhaveEyelids==2:
		PaupiereServoDroite.attach(left, PaupiereDroiteServoPin, 0, 10000)
	else:
	  if IhaveEyelids==2:
		PaupiereServoDroite.attach(right, PaupiereDroiteServoPin, 0, 10000)
	
	clockPaupiere = Runtime.start("clockPaupiere","Clock")
	clockPaupiere.setInterval(1000)
	# define a ticktock method
	def clignement(timedata):
		global RobotIsStarted
		global IcanMoveEyelids
		RobotIsStarted+=1
		if RobotIsStarted>2 and IcanMoveEyelids==1:
			PaupiereAttach(1)
			PaupiereServoGauche.setSpeed(1)
			PaupiereServoDroite.setSpeed(1)
			PositionPaupiere(0,0,1)
			sleep(0.12)
			PositionPaupiere(180,180,1)
		
	#on fait un double clignement ou pas
			if random.randint(0,1)==1:
				sleep(0.2)
				PositionPaupiere(0,0,1)
				sleep(0.12)
				PositionPaupiere(180,180,1)
				#on redefini une valeur aleatoire pour le prochain clignement
		clockPaupiere.setInterval(random.randint(10000,30000))
		sleep(0.12)
		PaupiereAttach(0)
				
	#create a message routes
	clockPaupiere.addListener("pulse", python.name, "clignement")
	# start the clock
	if RobotIsStarted==0:
		PositionPaupiere(180,180,0.5)
		sleep(3)
		
	clockPaupiere.startClock()
