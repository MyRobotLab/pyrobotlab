def facerecognizer():
    opencv.capture()
    opencv.setDisplayFilter("FaceRecognizer")
    fr.train()# it takes some time to train and be able to recognize face
    #if((lastName+"-inmoovWebKit" not in inmoovWebKit.getSessionNames())):
        #mouth.speak("Hello "+lastName)
        #sleep(2)
    #inmoovWebKit.getResponse(lastName,data)
