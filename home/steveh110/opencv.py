
# call back - all data from opencv will come back to 
# this method
def onOpenCVData(data):
	global MODEVIDEO
	global CompteurTraking
	global RECONAISSANCE
	global INTERLOCUTEUR


		
	if MODEVIDEO == 1 :
  		opencv.addFilter("PyramidDown")
		opencv.addFilter("Gray")
		opencv.addFilter("FaceDetect")
		opencv.setDisplayFilter("FaceDetect")
		MODEVIDEO = 2
		print("mode video 1")

	if MODEVIDEO == 2 :
  		test = False
  		print("mode video 2")
  		 		
  		if CompteurTraking > 100 :
  			CompteurTraking = 0
  			MODEVIDEO = 3
  			opencv.removeFilters()
  			RECONAISSANCE=opencv.addFilter("FaceRecognizer")
			opencv.setDisplayFilter("FaceRecognizer")
			RECONAISSANCE.train()# it takes some time to train and be able to recognize face
			 			
  		# check for a bounding box
  		if data.getBoundingBoxArray() != None:
    			for box in data.getBoundingBoxArray():
    				x = box.x *100
    				y = box.y *100
    				x2 = box.width *100
    				y2 = box.height*100
    				Xcentre = x + (x2 / 2)
    				Ycentre = y + (y2 / 2)
    				CompteurTraking = CompteurTraking + 1
    				test = True
    				Suivi(Xcentre,Ycentre)
  		if test != True :
  			CompteurTraking = 0	

  	
	if MODEVIDEO == 3 :
		nom=RECONAISSANCE.getLastRecognizedName()

		if isinstance(nom, unicode)  and nom != INTERLOCUTEUR :
			print("je t ais reconnu")
			chatBot.startSession("ProgramAB",nom,"steve")
			INTERLOCUTEUR = nom
		if isinstance(nom, unicode) and nom == INTERLOCUTEUR :
			MODEVIDEO = 0
			opencv.removeFilters()
			try:
				#text = "Salut " + nom
				#mouth.speakBlocking(text)
				chatBot.getResponse("SALUT 2")
				MODEVIDEO = 10
				opencv.removeFilters()
			except:
				pass
				
	if MODEVIDEO == 4 :
		opencv.addFilter("PyramidDown")
		opencv.addFilter("Gray")
		opencv.addFilter("FaceDetect")
		opencv.setDisplayFilter("FaceDetect")
		MODEVIDEO = 5

	if MODEVIDEO == 5 :
		if data.getBoundingBoxArray() != None:
    			for box in data.getBoundingBoxArray():
    				x = box.x *100
    				y = box.y *100
    				x2 = box.width *100
    				y2 = box.height*100
    				Xcentre = x + (x2 / 2)
    				Ycentre = y + (y2 / 2)
    				Suivi(Xcentre,Ycentre)

	if MODEVIDEO == 10 :
		opencv.removeFilters()
		opencv.stopCapture()




def Suivi(X,Y):
 pid.setInput("x",X)
 pid.compute("x")
 correction = int(pid.getOutput("x"))
 print ('entree pid : ', X)
 print ('sortie pid : ',correction)
 print ('position servo : ',RegardGD.getTargetOutput())
 temp = (RegardGD.getTargetOutput() - correction)
 RegardGD.moveTo(temp)
 