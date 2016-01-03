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
lloyd.startSession("ProgramAB", "default", "lloyd")
 
######################################################################
# create the speech recognition service
######################################################################
sphinx = runtime.createAndStart("i01.ear","Sphinx")
pats = lloyd.listPatterns("lloyd")
# create the grammar for the speech recognition service
sphinx_grammar = "|".join(pats)
sphinx.startListening(sphinx_grammar)
 
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
sphinx.addTextListener(lloyd)
# debugging in python route.
sphinx.addListener("publishText", python.name, "heard", String().getClass());
 
# Add route from Program AB to html filter
lloyd.addTextListener(htmlfilter)
# Add route from html filter to mouth
htmlfilter.addTextListener(mouth)
 
# make sure the ear knows if it's speaking.
sphinx.attach(mouth)