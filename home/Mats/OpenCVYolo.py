# Run opencv yolo filter optionally receiving a videostream from the PI camera on a remote host
# Get a hook to python
python = Runtime.start("python","Python")
# Start the speech service
speech = Runtime.start("speech","MarySpeech")
# Start opencv
opencv = Runtime.start("opencv","OpenCV")
## To stream from a Rapberry PI install UV4L as described in the link below 
## https://www.linux-projects.org/uv4l/installation/
## Uncomment the three lines below if you want to use a videostream from UV4L
#opencv.setFrameGrabberType("org.myrobotlab.opencv.MJpegFrameGrabber")
#opencv.setInputSource("file")
#opencv.setInputFileName("http://headpi:8080/stream/video.mjpeg")
# Subscribe to opencv data
python.subscribe("opencv", "publishYoloClassification")
# Subscribe to speech data
python.subscribe("speech", "publishStartSpeaking")
python.subscribe("speech", "publishEndSpeaking")
# Get result from yolo detection
lastSentence = ""
speaking = False
imageLabels = {}
def onYoloClassification(data):
  global lastSentence
  global imageLabels
  global speaking

  imageLabels.clear()
  for elem in data:
    label = elem.label
    if label in imageLabels:
      # print("Adding label " + label)
      imageLabels[label] = imageLabels[label] +1
    else:
      # print("Adding one more " + label)
      imageLabels[label] = 1

  if speaking == False:   
    sentence = "I see "
    index = 1 
    if len(imageLabels) == 0:
      sentence = sentence + "nothing"
    for label in imageLabels:
      if index > 1:
        sentence = sentence + " and "
      if imageLabels[label] == 1:
        sentence = sentence + str(imageLabels[label]) + " " + label
      else:
        sentence = sentence + str(imageLabels[label]) + " " + label + "s"
      index = index + 1

    if sentence <> lastSentence:
      print sentence
      speech.speakBlocking(sentence)
      lastSentence = sentence
        
def onStartSpeaking(x):
    global speaking
    speaking = True
    
def onEndSpeaking(x):
    global speaking
    speaking = False
# Add filters
opencv.addFilter("Yolo","Yolo")
# capture
opencv.capture()
