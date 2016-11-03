from org.myrobotlab.opencv  import OpenCVFilterSURF
import org.bytedeco.javacv.ObjectFinder.Settings
opencv = Runtime.createAndStart("opencv","OpenCV")
surf = OpenCVFilterSURF("surf")
surf.settings.setThreshold(400)
# Change path to the image you want to use
filename = "c:/dev/workspace.kmw/myrobotlab/kw.jpg"
surf.loadObjectImageFilename(filename)
opencv.addFilter(surf)
opencv.setDisplayFilter("surf") 
opencv.capture()
