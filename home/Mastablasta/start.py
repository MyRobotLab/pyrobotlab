from java.lang import String

def heard(data):
  print "Sphinx Data:", data

botname = Runtime.createAndStart("botname", "ProgramAB")
botname.startSession("ProgramAB", "default", "botname")
sphinx = runtime.createAndStart("i01.ear","Sphinx")
pats = botname.listPatterns("botname")
sphinx_grammar = "|".join(pats)
sphinx.startListening(sphinx_grammar)
htmlfilter = Runtime.createAndStart("htmlfilter", "HtmlFilter")
mouth = Runtime.createAndStart("i01.mouth", "Speech")
mouth.setGoogleURI("http://thehackettfamily.org/Voice_api/api2.php?voice=Ryan&txt=")
sphinx.addTextListener(botname)
sphinx.addListener("publishText", python.name, "heard", String().getClass());
botname.addTextListener(htmlfilter)
htmlfilter.addTextListener(mouth)
holygrail = Runtime.createAndStart("holygrail", "WebGUI")
sphinx.attach(mouth)

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
