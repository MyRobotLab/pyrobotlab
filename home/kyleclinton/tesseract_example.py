################################################################
#
#  tesseract_example.py
#  Kyle J Clinton
#
#  This is an example of the use of TesseractOcr to read text from an image
#  it is using many of the services that are common to the InMoov project or 
#  MRL in general
#
################################################################

### Start and Setup OpenCV
opencv=Runtime.start("opencv","OpenCV")

opencv.captureFromResourceFile("http://192.168.1.130:8080/stream/video.mjpeg"); 
# This Grabber does not seem to set correctly inside of OpenCV !?!?!
opencv.setFrameGrabberType("org.myrobotlab.opencv.MJpegFrameGrabber"); 

opencv.capture()

### Start and Setup Tesseract (Not as a filter inside OpenCV)
tesseract = Runtime.createAndStart("tesseract","TesseractOcr")


### Start and Setup MarySpeech (You could switch out for your favorite TextToSpeech service) 
mouth = Runtime.createAndStart("MarySpeech", "MarySpeech")
mouth.setVoice("cmu-bdl-hsmm")

### This is my little mod to the voice to make it specifically "Junior's Voice"
mouth.setAudioEffects("TractScaler(amount=1.4) + F0Add(f0Add=60.0) + Robot(amount=8.0) ")

def readTextFromImage():
  tesseract = Runtime.createAndStart("tesseract","TesseractOcr")
  txtStr = tesseract.ocr("20170908_141852.jpg")
  print("tess results: ", txtStr) 
  mouth.speakBlocking(txtStr)
  ## Not sure why I need to cleanup string for image name???
  ####imgNameStr = opencv.recordFrame()
  ####imgNameStr = imgNameStr.replace("u'", "").replace("'", "")
  ####print("captured image: ", imgNameStr)
  ####txtStr = tesseract.ocr(imgNameStr)
  ## For Testing
  #txtStr = tesseract.ocr("20170908_141852.jpg")
  ## Cleanup of the string is required and this is very basic and needs to be more robust!
  #txtStr = txtStr.replace("\n", " ").replace(":", " ")
  #print("tess results: ", txtStr)
  #mouth.speakBlocking(txtStr)
