from java.lang import String
python = Runtime.getService("python")


#Add MQTT!
execfile("../Git/py_scripts/mqttPubSubConfig.py")

#Add Sight!
execfile("../Git/py_scripts/junior_sight.py")

# create a ProgramAB service and start a session
junior = Runtime.createAndStart("junior", "ProgramAB")
junior.startSession("ProgramAB", "default", "junior")

######################################################################
# create the speech recognition service
# Speech recognition is based on WebSpeechToolkit API
######################################################################
# Start the new WebGuiREST API for MRL
webgui = Runtime.createAndStart("webgui","WebGui")

######################################################################
# Create the webkit speech recognition gui
# This service works in Google Chrome only with the WebGui
######################################################################
wksr = Runtime.createAndStart("webkitspeechrecognition", "WebkitSpeechRecognition")
######################################################################
# create the html filter to filter the output of program ab
# this service will strip out any html markup and return only the text
# from the output of ProgramAB
######################################################################
htmlfilter = Runtime.createAndStart("htmlfilter", "HtmlFilter")
# add a link between the webkit speech to publish text to ProgramAB
wksr.addTextListener(junior)

junior.addListener("publishText","python","onTextResponse")
 
#  MQTT call-back
# publishMqttMsgString --> onMqttMsgString(msg)
def onMqttMsgString(msg):
  # print "message : ", msg
  junior.getResponse(msg[0])
  print "message : ",msg[0]
  print "topic : ",msg[1]

def onTextResponse(text):
  mqtt.publish(text)
  print "sending : ", text
