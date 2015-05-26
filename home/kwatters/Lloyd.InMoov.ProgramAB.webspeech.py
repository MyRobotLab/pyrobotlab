from java.lang import String
 
######################################################################
# A helper function to print the recognized text to the python window.
# semi-useful for debugging.
######################################################################
def heard(data):
  print "Sphinx Data:", data
 
######################################################################
# Create ProgramAB chat bot
######################################################################
lloyd = Runtime.createAndStart("lloyd", "ProgramAB")
lloyd.startSession("c:/dev/workspace.kmw/pyrobotlab/home/kwatters", "default", "lloyd")
 
######################################################################
# create the speech recognition service
# Speech recognition is based on WebSpeechToolkit API
# 
######################################################################
# Start the REST API for MRL
webgui = Runtime.createAndStart("webgui","WebGUI")

######################################################################
# create the html filter to filter the output of program ab
######################################################################
htmlfilter = Runtime.createAndStart("htmlfilter", "HtmlFilter")
 
######################################################################
# create the speech to text service (named the same as the inmoov's)
######################################################################
mouth = Runtime.createAndStart("i01.mouth", "Speech")
 
######################################################################
# MRL Routing   sphinx -> program ab -> htmlfilter -> inmoov
######################################################################
# add a route from Sphinx to ProgramAB
# sphinx.addTextListener(lloyd)
# debugging in python route.
# sphinx.addListener("publishText", python.name, "heard", String().getClass());
 
# Add route from Program AB to html filter
lloyd.addTextListener(htmlfilter)
# Add route from html filter to mouth
htmlfilter.addTextListener(mouth)
 
# make sure the ear knows if it's speaking.
# TODO: how does this jive with webspeech ?!
# sphinx.attach(mouth)

