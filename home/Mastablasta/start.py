from java.lang import String
botname = Runtime.createAndStart("botname", "ProgramAB")
botname.startSession("ProgramAB", "default", "botname")
htmlfilter = Runtime.createAndStart("htmlfilter", "HtmlFilter")
mouth = Runtime.createAndStart("i01.mouth", "Speech")
mouth.setGoogleURI("http://thehackettfamily.org/Voice_api/api2.php?voice=Ryan&txt=")
botname.addTextListener(htmlfilter)
htmlfilter.addTextListener(mouth)
holygrail = Runtime.createAndStart("holygrail", "WebGUI")

