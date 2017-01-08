# ##############################################################################
#						*** RIGHT HAND ***
# ##############################################################################

# rotationCylindre------pin 46
# berceau------pin 49

 
  
# ##############################################################################
# 							PERSONNAL PARAMETERS
# ##############################################################################  
  
#read current skeleton part config
ThisSkeletonPart=inspect.getfile(inspect.currentframe()).replace('.py','')
try:
	CheckFileExist(ThisSkeletonPart)
	ThisSkeletonPartConfig = ConfigParser.ConfigParser()
	ThisSkeletonPartConfig.read(ThisSkeletonPart+'.config')

	isNez=ThisSkeletonPartConfig.getboolean('MAIN', 'isNez') 
	autoDetach=ThisSkeletonPartConfig.getboolean('MAIN', 'autoDetach')
except:
	errorSpokenFunc('ConfigParserProblem','nez.config')
	pass
    
  
  
  
# ##############################################################################
# 								SERVO FUNCTIONS
# ##############################################################################

if isNez==1 and (ScriptType=="RightSide" or ScriptType=="Full"):
	if RightPortIsConnected:
		
		rotationCylindre = Runtime.create("rotationCylindre", "Servo")
		rotationCylindre.map(0,180,ThisSkeletonPartConfig.getint('SERVO_MINIMUM', 'rotationCylindre'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM', 'rotationCylindre')) 
		rotationCylindre.setVelocity(ThisSkeletonPartConfig.getint('DEF_SPEED', 'rotationCylindre'))
		rotationCylindre.setRest(ThisSkeletonPartConfig.getint('SERVO_MAP_REST', 'rotationCylindre'))
		rotationCylindre = Runtime.start("rotationCylindre","Servo")
		rotationCylindre.attach(right, 0, 48)
		berceau = Runtime.create("berceau", "Servo")
		berceau.map(0,180,ThisSkeletonPartConfig.getint('SERVO_MINIMUM', 'berceau'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM', 'berceau')) 
		berceau.setVelocity(ThisSkeletonPartConfig.getint('DEF_SPEED', 'berceau'))
		berceau.setRest(ThisSkeletonPartConfig.getint('SERVO_MAP_REST', 'berceau'))
		berceau = Runtime.start("berceau","Servo")
		berceau.attach(right, 21, 46)
			
		if autoDetach:
			rotationCylindre.enableAutoAttach(1)
			berceau.enableAutoAttach(1)
			
		
		rotationCylindre.rest()
		berceau.rest()
		sleep(1)
		rotationCylindre.detach()
		berceau.detach()
		
	else:
		#we force parameter if arduino is off
		isNez=0
		
#todo set inverted
