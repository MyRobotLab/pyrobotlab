global FaceDetectedCounter
FaceDetectedCounter=0
global FaceDetected
FaceDetected=1
global startTimerFunction

python.subscribe(opencv.getName(),"publishOpenCVData")

NoFaceDetectedTimer = Runtime.start("NoFaceDetectedTimer","Clock")
NoFaceDetectedTimer.setInterval(20000)

def onOpenCVData(data):
	#print FaceDetectedCounter
	global FaceDetectedCounter
	global FaceDetected
	if data.getBoundingBoxArray() != None:
		if not data.getBoundingBoxArray():
			FaceDetectedCounter=0
		else:
			FaceDetectedCounter+=1
			if FaceDetectedCounter>50 and FaceDetected==0:
				NoFaceDetectedTimer.stopClock()
				FaceDetected=1
				chatBot.getResponse("SYSTEM FACEDETECTED")
				
				
		
		
	
		
def NoFaceDetectedTimerFunction(timedata):
	global startTimerFunction
	startTimerFunction+=1
	if startTimerFunction==2:
		FaceDetected=1
		chatBot.getResponse("SYSTEM FACENOTDETECTED")
		
		
				
NoFaceDetectedTimer.addListener("pulse", python.name, "NoFaceDetectedTimerFunction")
# start the clock

	