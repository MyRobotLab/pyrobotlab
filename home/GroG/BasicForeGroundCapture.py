opencv = Runtime.start("uv","OpenCV")
opencv.capture()

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
 
