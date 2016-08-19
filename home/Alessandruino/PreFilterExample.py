from org.myrobotlab.opencv import OpenCVFilterAffine

affine = OpenCVFilterAffine("affine")
affine.setAngle(180.0)

leftPort= "/dev/cu.wchusbserial1450" 
i01 = Runtime.start("i01","InMoov")
headTracking = i01.startHeadTracking(leftPort)
eyesTracking = i01.startEyesTracking(leftPort,10,12)
i01.headTracking.addPreFilter(affine)
i01.eyesTracking.addPreFilter(affine)
sleep(1)
i01.headTracking.faceDetect()
i01.eyesTracking.faceDetect()
