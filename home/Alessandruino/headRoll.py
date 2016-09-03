opencv.addListener("publishOpenCVData", "python","onOpenCVData")

pid = Runtime.createAndStart("pid","Pid")
pid.setMode(1)
#set the range of the "correction"
pid.setOutputRange(-1, 1)
#set Kp, kd, ki kp = gain, how strong it react kd = how fast it react ki= take care of the sum of errors (differences between target and actual value) in the time
pid.setPID(10.0, 0, 1.0)
pid.setControllerDirection(0)

#set a starting analog value, which will pilot the MOSFET on the Gate
heaterValue = 90

# call back - all data from opencv will come back to 
# this method
def onOpenCVData(data):
  global heaterValue
  global futureHeaterValue
  #target of temperature or target value
  pid.setSetpoint(0)
  #input value
  pid.setInput(data.getEyesDifference())
  pid.compute()
  correction = pid.getOutput()
  futureHeaterValue = (heaterValue + correction)
  if (futureHeaterValue < 180) and (futureHeaterValue >0):
   heaterValue = futureHeaterValue
   print heaterValue
  else :
   print heaterValue
  # check for a bounding box
  #print data.getEyesDifference()
