#########################################################
# Fred01 ProgramAB the Brain of Fred
#########################################################
# We will be using the following services:
#    Runtime Service
#    Program Service
#    HtmlFiter Service
#########################################################

# Ok we now have the services we need for speech recognition and text to speech service
# from the remote connection with Fred01, so what are we going to do with it.
# From my perspective we have two options in using the data.
# Option 1 is to capture the data from the WKSR and then search though the data for
# a Particular phase.
# the data is captured with a command like the following:
# wkrs.addListener("publishText","python","onText")
# that would then call a method that you would have created called onText

# The other option would be to send the captured data to a chat box such as Alice2 which is included
# as part of the ProgramAB Service.
# This is my prefered path as it is much more powerfull.
# To do this we will first need to create the service
# My Inmoov robot is called Fred so i will call the service fred.
# In yor case yo can name the service after your robot.
fred = Runtime.createAndStart("fred", "ProgramAB")

# Next we need to start a session. The first parameter here is your name and is used to store data
# created as a result of talking to you.
# The second parameter is the name of the aiml file set that ProgramAB will be using.
fred.startSession("ray", "alice2")

# The information coming out of ProgramAB can have some Hyper Text Markup Language (HTML) included in it.
# MarySpeech does not like the markup, so we need to get rid of it.
# To do that we use a HtmlFilter Service
# From Runtime, we create the HtmlFilter Service
htmlfilter = Runtime.createAndStart("htmlfilter", "HtmlFilter")

# Next we will add what is kown as data routing.
# We will route text created by fred (ProgramAB) to the HtmlFilter
fred.addTextListener(htmlfilter)

# Next we will tell WKSR from Fred01 to send the text it has converted from speech to fred the ProgramAB service
fred01.wksr.addTextListener(fred)

# And Finally, the filtered text from the HtmlFilter to the MarySpeech of Fred01 we called mouth
htmlfilter.addTextListener(fred01.mouth)
