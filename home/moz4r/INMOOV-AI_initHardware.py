# -- coding: utf-8 --
# ##############################################################################
# 							    *** Initialisation hardware ***
# ##############################################################################
# -----------------------------------
# - Rachel the humanoïde (Anthony)
# - Jarvis (Dom)
# -----------------------------------
# ##############################################################################

# Service MRL InMoov
i01 = Runtime.create("i01", "InMoov")

# disable autocheck
i01.setMute(1)

# ##############################################################################
# InMoov servo configuration
# ##############################################################################

# Left arduino
left = Runtime.create("i01.left", "Arduino")
left.setBoard(BoardTypeLeft)
leftHand = Runtime.create("i01.leftHand", "InMoovHand")
leftArm = Runtime.create("i01.leftArm", "InMoovArm")
leftArm.bicep.setMinMax(BicepsLeftMIN,BicepsLeftMAX) 
leftArm.bicep.map(0,180,BicepsLeftMIN,BicepsLeftMAX)
leftArm.bicep.setRest(BicepsLeftMIN)
leftArm.shoulder.setMinMax(ShoulderLeftMIN,ShoulderLeftMAX) 
leftArm.shoulder.map(0,180,ShoulderLeftMIN,ShoulderLeftMAX)
leftArm.shoulder.setRest(ShoulderLeftMIN)
leftArm.shoulder.setRest(0)
leftHand.thumb.setMinMax(ThumbLeftMIN,ThumbLeftMAX) 
leftHand.index.setMinMax(IndexLeftMIN,IndexLeftMAX) 
leftHand.majeure.setMinMax(majeureLeftMIN,majeureLeftMAX) 
leftHand.ringFinger.setMinMax(ringFingerLeftMIN,ringFingerLeftMAX) 
leftHand.pinky.setMinMax(pinkyLeftMIN,pinkyLeftMAX) 
leftHand.thumb.map(0,180,ThumbLeftMIN,ThumbLeftMAX) 
leftHand.index.map(0,180,IndexLeftMIN,IndexLeftMAX) 
leftHand.majeure.map(0,180,majeureLeftMIN,majeureLeftMAX) 
leftHand.ringFinger.map(0,180,ringFingerLeftMIN,ringFingerLeftMAX) 
leftHand.pinky.map(0,180,majeureLeftMIN,majeureLeftMAX)
head = Runtime.create("i01.head","InMoovHead")
head.jaw.setMinMax(JawMIN,JawMAX)
if JawInverted==1:
	head.jaw.map(0,180,JawMAX,JawMIN)
else:
	head.jaw.map(0,180,JawMIN,JawMAX)
head.jaw.setRest(0)

head.eyeX.setMinMax(EyeXMIN,EyeXMAX)
head.eyeX.map(0,180,EyeXMIN,EyeXMAX)
head.eyeX.setRest(EyeXRest)

head.eyeY.setMinMax(EyeYMIN,EyeYMAX)
head.eyeY.map(0,180,EyeYMIN,EyeYMAX)
head.eyeY.setRest(EyeYRest)

head.neck.setMinMax(MinNeck,MaxNeck)
if NeckInverted==1: 
	head.neck.map(0,180,MaxNeck,MinNeck)
else:
	head.neck.map(0,180,MinNeck,MaxNeck)
head.neck.setRest(NeckRest)

head.rothead.setMinMax(MinRotHead,MinRotHead)
if RotHeadInverted==1: 
	head.rothead.map(0,180,MaxRotHead,MinRotHead)
else:
	head.rothead.map(0,180,MinRotHead,MaxRotHead)
head.rothead.setRest(RotHeadRest)

# Right arduino
right=Runtime.create("i01.right", "Arduino")
right.setBoard(BoardTypeRight)
rightHand = Runtime.create("i01.rightHand", "InMoovHand")
rightArm = Runtime.create("i01.rightArm", "InMoovArm")
rightArm.bicep.setMinMax(BicepsRightMIN,BicepsRightMAX) 
rightArm.bicep.map(0,180,BicepsRightMIN,BicepsRightMAX)
rightArm.bicep.setRest(BicepsRightMIN)
rightArm.shoulder.setRest(0)
rightHand.thumb.setMinMax(ThumbRightMIN,ThumbRightMAX) 
rightHand.index.setMinMax(IndexRightMIN,IndexRightMAX) 
rightHand.majeure.setMinMax(majeureRightMIN,majeureRightMAX) 
rightHand.ringFinger.setMinMax(ringFingerRightMIN,ringFingerRightMAX) 
rightHand.pinky.setMinMax(pinkyRightMIN,pinkyRightMAX) 
rightHand.thumb.map(0,180,ThumbRightMIN,ThumbRightMAX) 
rightHand.index.map(0,180,IndexRightMIN,IndexRightMAX) 
rightHand.majeure.map(0,180,majeureRightMIN,majeureRightMAX) 
rightHand.ringFinger.map(0,180,ringFingerRightMIN,ringFingerRightMAX) 
rightHand.pinky.map(0,180,majeureRightMIN,majeureRightMAX)

torso = Runtime.create("i01.torso", "InMoovTorso")
torso.topStom.setMinMax(TorsoTopMin,TorsoTopMax)
torso.topStom.map(0,180,TorsoTopMin,TorsoTopMax)
torso.topStom.setRest(TorsoTopRest)
torso.midStom.setMinMax(TorsoMidMin,TorsoMidMax)
torso.midStom.map(0,180,TorsoMidMin,TorsoMidMax)
torso.midStom.setRest(TorsoMidRes)

# Start the arduino
i01 = Runtime.start("i01","InMoov")
head = Runtime.start("i01.head", "Arduino")
if IsInmoovArduino==1:
	
	left = Runtime.start("i01.left", "Arduino")
	
	head.setSpeed(DefaultSpeed,DefaultSpeed,DefaultSpeed,DefaultSpeed,DefaultSpeed)
	head.rothead.setSpeed(0.1)
	head.neck.setSpeed(0.1)
	i01.startHead(leftPort)
	i01.head.eyeY.rest()
	i01.head.eyeX.rest()
	head.neck.setSpeed(NeckSpeed)
	
	i01.startLeftHand(leftPort)
	i01.startLeftArm(leftPort)
	
	if MRLmouthControl==1:
		i01.startMouthControl(leftPort)
		i01.mouthControl.setmouth(0,180)
    
	if TorsoArduino=="left":	
		torso = i01.startTorso(leftPort)
	else:
		torso = i01.startTorso(rightPort)
	
	#i01.startHeadTracking(leftPort)
	
	right = Runtime.start("i01.right", "Arduino")
  
	i01.startRightHand(rightPort,"")
	i01.startRightArm(rightPort)
	
  # gestion des mouvement latéraux de la tete ( mod pistons de Bob )
	HeadSide = Runtime.create("HeadSide","Servo")
	HeadSide.setMinMax(MinHeadSide,MaxHeadSide)
	HeadSide.map(0,180,MinHeadSide,MaxHeadSide)
	HeadSide.setRest(HeadSideRest)
	HeadSide.setSpeed(PistonSideSpeed)
	HeadSide = Runtime.start("HeadSide","Servo")
	if HeadSideArduino=="left":
		HeadSide.attach(left, HeadSidePin, HeadSideRest, 500)
	else:
		HeadSide.attach(right, HeadSidePin, HeadSideRest, 500)
	HeadSide.setSpeed(PistonSideSpeed)

i01.startMouth()
i01.startEar()
ear = i01.ear
mouth = i01.mouth

# ##############################################################################
# Activator arduino configuration
# ##############################################################################
if Activator==1 and IsInmoovArduino==1:
	if ActivatorControler=="left":
		ActivatorControler=left
	else:
		ActivatorControler=right

	ActivatorArduino = Runtime.createAndStart("ActivatorArduino","Arduino")
	ActivatorArduino.setBoard(BoardTypeActivator)
	ActivatorArduino.connect(ActivatorControler,ActivatorPort)
  

  
