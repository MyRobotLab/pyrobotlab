webgui=Runtime.create("WebGui","WebGui")
webgui.autoStartBrowser(False)
webgui.startService()

#start speech recognition and AI
wksr=Runtime.createAndStart("webkitspeechrecognition","WebkitSpeechRecognition")
pinocchio = Runtime.createAndStart("pinocchio", "ProgramAB")
pinocchio.startSession("default", "pinocchio")
htmlfilter=Runtime.createAndStart("htmlfilter","HtmlFilter")
mouth=Runtime.createAndStart("i01.mouth","AcapelaSpeech")
#wksr.addTextListener(pinocchio)
wksr.addListener("publishText","python","heard")
pinocchio.addTextListener(htmlfilter)
htmlfilter.addTextListener(mouth)

opencv=Runtime.start("opencv","OpenCV")
opencv.setCameraIndex(1)
opencv.capture()
fr=opencv.addFilter("FaceRecognizer")
opencv.setDisplayFilter("FaceRecognizer")
fr.train()# it takes some time to train and be able to recognize face

def heard(data):
	lastName=fr.getLastRecognizedName()
	if((lastName+"-pinocchio" not in pinocchio.getSessionNames())):
		mouth.speak("Hello "+lastName)
		sleep(2)
	pinocchio.getResponse(lastName,data)
