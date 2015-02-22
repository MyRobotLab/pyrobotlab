
def onOpenCVData(data):
  if data != None:
    boxes = data.getBoundingBoxArray()
    if boxes != None:
      print "found", boxes.size(), " boxes"

      
opencv = Runtime.start("uv","OpenCV")
opencv.capture()

python.subscribe("uv","publishOpenCVData", "onOpenCVData")
 
opencv.addFilter("Detector")
opencv.setDisplayFilter("Detector")
detector = opencv.getFilter("Detector") 
 
opencv.addFilter("FindContours")
contours = opencv.getFilter("FindContours") 
 
detector.learn()
 
sleep(4) 
 
detector.search()
 
sleep(20)
 
opencv.stopCapture()
