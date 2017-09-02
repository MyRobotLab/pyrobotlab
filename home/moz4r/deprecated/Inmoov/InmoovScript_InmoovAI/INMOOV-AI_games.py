# -*- coding: utf-8 -*- 

################################################################################
# LOTO
################################################################################	

def loto(phrase,the,chance,fin):
	table1 = [(random.randint(1,49)), (random.randint(1,49)), (random.randint(1,49)), (random.randint(1,49)),(random.randint(1,49))]
	tablefin = []
	doublon = []

	for i in table1:
		if i not in tablefin:
			tablefin.append(i) #supprime les doublons
		else:
			doublon.append(i) #extraire les doublons
			d = len(doublon)
			while d > 0:
			#nouveau tirage
				doublon = []
				table1 = [(random.randint(1,49)), (random.randint(1,49)), (random.randint(1,49)), (random.randint(1,49)),(random.randint(1,49))]
				# recherche doublon
				for i in table1:
					if i not in tablefin:
						tablefin.append(i) #supprime les doublons
					else:
						doublon.append(i) #extraire les doublons
					# si il existe doublon d+1 et vite la table
					if (len(doublon)==1)or(len(doublon)==2)or(len(doublon)==3)or(len(doublon)==4)or(len(doublon)==5):
						talkBlocking("j ai trouver un doublon , je refais un tirage")
						d = d+1
						doublon =[]
					else:
						d = 0
		break
	# tri la table avant de la dire
	table1.sort()
	talkBlocking(phrase)
	talkBlocking(the+str(table1[0]))
	talkBlocking(the+str(table1[1]))
	talkBlocking(the+str(table1[2]))
	talkBlocking(the+str(table1[3]))
	talkBlocking(the+str(table1[4]))
	talkBlocking(chance+str(random.randint(1,9)))
	talkBlocking(fin)
	
################################################################################
# THE BOT REPEAT WORDS
################################################################################	

def ParrotModFunc(ParrotModVal):
	global ParrotMod
	ParrotMod=ParrotModVal
	chatBot.getResponse("SYSTEM PARROT " + str(ParrotModVal))
	
	
################################################################################
# JOUER AUX MOTS - PLAY WITH WORDS
################################################################################
	
def PlayWithWords(word):
	FindImage(word)
	talkBlocking(word)
	for i in word.decode( "utf8" ):
		if i.isalpha():
			#print "SAY "+i
			TimeNoSpeak="OFF"
			folderLetterPic="pictures\\games\\alphabet\\"
			print folderLetterPic+i+".jpg"
			try:
				r=image.displayFullScreen(folderLetterPic+i+".jpg",1)
			except:
				pass
			talk(i)
			sleep(2)
	FindImage(word)
	sleep(1)
	image.exitFS()
	image.closeAll()
	TimeNoSpeak="ON"
	
	
################################################################################
#1. 2. 3. SUN !!! ( Grandmother's footsteps )
# SETUP :
################################################################################
global FourMeters
FourMeters=0.08
global InFrontOfMe
InFrontOfMe=0.28
################################################################################
	
ReculeTimer = Runtime.start("ReculeTimer","Clock")
ReculeTimer.setInterval(15000)	

def ReculeTimerFunc(timedata):
	#little fix to avoid speak loop
	print openCvModule
	global FaceDetected
	global MoveHeadRandom
	
	ear.pauseListening()
	
	
	if FaceDetected==1:
		if random.randint(1,2)==2:
			RightArmAheadBehind()
			#talk("recule")
			chatBot.getResponse("SYSTEM YOU ARE TOO NEAR OF ME")
		else:
			RightArmAheadBehind()
			#talk("recule")
			chatBot.getResponse("SYSTEM YOU ARE TOO NEAR OF ME2")
	else:
		if random.randint(1,2)==2:
			#talk("no visage")
			chatBot.getResponse("SYSTEM I DONT SEE YOU")
		else:
			#talk("no visage")
			chatBot.getResponse("SYSTEM I DONT SEE YOU2")
			
	#WebkitSpeachReconitionFix.stopClock()	
ReculeTimer.addListener("pulse", python.name, "ReculeTimerFunc")	

########################################
#we ceate a separated thread : it is better to prevent slow down because of loops and sleep and opencv thread
########################################
class soleilEtape1(threading.Thread):
  

	def __init__(self):
		super(soleilEtape1, self).__init__()
		print "Here we are"
		self.running = False
	
	def run(self):
		global TimoutVar
		global openCvModule
		global FaceHadMoved
		global DistanceOfTheFace
		global Ispeak
		global IcanMoveHeadRandom
		global IcanMoveEyelids
		global FourMeters
		global InFrontOfMe
		global etape
		IcanMoveEyelids=0
		
		sleep(3)
		etape=0
		ReculeTimerIsStarted=0
		self.running = True
		openCvModule="CalcDistance"
		while self.running:
			#print "dbg: MoveHeadRandom :",MoveHeadRandom
			Ispeak=1
			
			
			if etape==0:
				print "opencv thread starting"
				TimoutVar=-1
				TimoutTimer.setInterval(60000)
				
				WebkitSpeachReconitionFix.stopClock()
				ear.pauseListening()
				etape=1
				TimoutTimer.startClock()
			
			while etape==1 and DistanceOfTheFace!=10 and DistanceOfTheFace>FourMeters:
				Ispeak=1
				
				if ReculeTimerIsStarted==0:
					
					ReculeTimer.startClock()
					ReculeTimerIsStarted=1
				
				if TimoutVar>=1:
					chatBot.getResponse("SYSTEM TIMEOUT 123")
					ReculeTimerIsStarted=0
					ReculeTimer.stopClock()
					Ispeak=0
					sleep(10)
					TimoutVar=-1
					break
			
			if etape==1 and DistanceOfTheFace!=0 and DistanceOfTheFace<=FourMeters:
				
				talk("Ok tu es à 4 mètres environ")
				
				ear.pauseListening()
				talk("C'est parti!")
				IcanMoveHeadRandom=0
				ReculeTimer.stopClock()
				TimoutTimer.stopClock()
				sleep(7)
				WebkitSpeachReconitionFix.stopClock()
				ear.pauseListening()
				openCvModule="123"
				
				TimoutVar=1
				etape=2
				TimoutTimer.setInterval(6000)
				TimoutTimer.startClock()
				
			
			if etape==2 and (FaceHadMoved[0]!=0 or FaceHadMoved[1]!=0 or FaceHadMoved[2]!=0):
				CauseMove=""
				if FaceHadMoved[3]!=0:
					CauseMove="De gauche à droite" # From lelt to right
				if FaceHadMoved[4]!=0:
					CauseMove="De haut en bas" # From up to bootm
				if FaceHadMoved[5]!=0:
					CauseMove="Basculé d'avant en arrière" # From ahead to behind
				chatBot.getResponse("SYSTEM YOU LOSE BECAUSE " + CauseMove)
				
				
				TimoutTimer.stopClock()
				TimoutVar=-1
				etape=1
				ReculeTimerIsStarted=0
				sleep(5)
				openCvModule="CalcDistance"
				DistanceOfTheFace=10
				FaceHadMoved=[0,0,0,0,0,0]
				
			
			
			if etape==2 and TimoutVar>0 and (FaceHadMoved[0]==0 and FaceHadMoved[1]==0 and FaceHadMoved[2]==0):
				openCvModule="Nothing"
				chatBot.getResponse("CACHE TES YEUX")
				
				#talk("yeux")
				sleep(4)
				rest()
				
				chatBot.getResponse("SYSTEM SOLEIL")
				
				#talk("soleil")
				
				WebkitSpeachReconitionFix.stopClock()
				ear.pauseListening()
				TimoutVar=-1
				TimoutTimer.startClock()
				openCvModule="123"
				sleep(1)
				FaceHadMoved=[0,0,0,0,0,0]
				
			if etape==2 and DistanceOfTheFace>InFrontOfMe and DistanceOfTheFace!=10:
				chatBot.getResponse("YOU WIN")
				SuperThumb()
				etape=3
				
			if etape==3:
				ReculeTimer.stopClock()
				TimoutTimer.stopClock()
				openCvModule="nothing"
				etape=-1
				self.running = False
				break
				#self.running = False
				
				
				
		 
		print "Stopped"

########################################
#end of the opencv thread
########################################		
	
soleilEtape1 = soleilEtape1()
	
def soleil():
	openCvInit()
	sleep(2)
	global MoveEyesRandom
	global openCvModule
	MoveEyesRandom=0
	openCvModule="CalcDistance"
	sleep(15)
	if IsInmoovArduino==1:
		head.rest()
	soleilEtape1.start()
	
def stopJeux():
	global etape
	etape=3
	
	try:
		ReculeTimer.stopClock()
		TimoutTimer.stopClock()
		soleilEtape1.running = False
		soleilEtape1.join()
	except:
		print "thread stop error"
	