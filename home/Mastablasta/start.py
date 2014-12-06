from java.lang import String

botname = Runtime.createAndStart("botname", "ProgramAB")
botname.startSession("ProgramAB", "default", "botname")
htmlfilter = Runtime.createAndStart("htmlfilter", "HtmlFilter")
mouth = Runtime.createAndStart("i01.mouth", "Speech")
mouth.setGoogleURI("http://thehackettfamily.org/Voice_api/api2.php?voice=Ryan&txt=")
botname.addTextListener(htmlfilter)
htmlfilter.addTextListener(mouth)
holygrail = Runtime.createAndStart("holygrail", "WebGUI")

def randommove():
  i01.moveHand("right",50,50,50,60,50,50)
  i01.moveArm("right",30,120,105,10)
  i01.moveTorso(100,90,90)
  i01.moveArm("left",0,90,96,99)
  sleep(0.5)
  i01.moveHand("right",50,50,50,60,50,20)
  i01.moveArm("right",0,110,96,0)
  i01.moveTorso(90,90,90)
  i01.moveArm("left",0,90,90,90)
  
randommove()
