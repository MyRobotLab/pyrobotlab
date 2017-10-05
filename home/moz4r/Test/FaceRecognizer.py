opencv = Runtime.start("opencv","OpenCV")
opencv.setMinDelay(500)
opencv.captureFromImageFile("resource/OpenCV/testData/ryan.jpg")

Python = Runtime.start("Python","Python")

Python.subscribe("opencv", "publishRecognizedFace")
def onRecognizedFace(name):
    print(name)

opencv.capture()



#### LKOpticalTrack ####################
# experiment with Lucas Kanade optical flow/tracking
# adds the filter and one tracking point
opencv.addFilter("PyramidDown")
fr=opencv.addFilter("FaceRecognizer")
fr.train()
opencv.setDisplayFilter("FaceRecognizer")
sleep(5)
opencv.captureFromImageFile("resource/OpenCV/testData/nok-test2.jpg")
sleep(5)
opencv.captureFromImageFile("resource/OpenCV/testData/rachel.jpg")
sleep(5)
opencv.captureFromImageFile("resource/OpenCV/testData/OK-test1.jpg")

