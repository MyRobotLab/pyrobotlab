#########################################################
#  Web Kit Speech Recognition (WKSR)
#########################################################
# The WKSR service is a web based system, 
# in order to use it we will need to create the WebGui service first
# But we don't want to start it just yet so we just use the create command
# GUI in case you didn't know stands for Graphical User Interface.
# All service are created by the Runtime Service so the command is run from there.
# It returns an object that is the WebGui service.
WebGui = Runtime.create("WebGui","WebGui")

# The next this we need to do is prevent the Web Browser starting up on a page we don't need.
# by default when the WebGui service is started it will launce the local web browser for a runtime GUI
# We will prevent this behaveiour by setting the autoStartBrowser to false.
WebGui.autoStartBrowser(False)

# Now we have the web browser disabled from auto starting lets start the WebGui service
# with the startService command
WebGui.startService()

# Ok now we need to create and start the WebKitSpeechRecognition Service
# As with all service, it is created from the Runtime Service and can be started from there
wksr = Runtime.start("wksr","WebkitSpeechRecognition")

# Now that we have the WebGui service and a WebKitSpeechRecognotion Service running we can 
# start the Web Browser sending it to a service page we just created
# It is very inportant that the part of the path after the service is the same 
# name that you give your WebKitSpeechRecognition service in this case wksr
WebGui.startBrowser("http://localhost:8888/#/service/wksr")

# Now I'm an English speaker in Australia, so i will set the language to "en-AU"
# with the setLanguage command.
# for a full list of supported languages visit: https://cloud.google.com/speech/docs/languages
wksr.setLanguage("en-AU")

# If setAutoListen is True, webkitspeech red microphone will auto rearm. 
# microphone will shutdown too if mouth is activated. 
# Careful if this is set to True : You cannot control anymore red microphone from webgui 
# You need to control it from SwinGui, or usually from code
wksr.setAutoListen(False)
 
# If setContinuous is False, this speeds up recognition processing 
# If setContinuous is True, you have some time to speak again, in case of error
# in this case we will use False
wksr.setContinuous(False)

# So far we have delt oly with the speech recognition, but now it's time to start talking.
# For the Text To Speech (TTS) we will be useing the MarySpeech TTS service
# First thing we need to do is create it with the Runtime Service
mouth = Runtime.start("mouth", "MarySpeech")

# To set a different voice use the following command
# To find a list of different voices you can use visit http://myrobotlab.org/service/MarySpeech
mouth.setVoice("cmu-slt-hsmm")

# There is nothing worse that your robot talking to its self
# to prevent that from happening we will add the mouth service to the wksr service
wkrs.addMouth(mouth)

# Ok we now have the services we need for speech recognition and text to speach service
# So what are we going to do with it.
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

# Next we need to start a session. The first parameter here is your name and is used to same data
# created as a result of talking to you.
# The second parameter is the name of the aiml file set that ProgramAB will be using.
fred.startSession("ray", "alice2")

# The information coming out of ProgramAB can have some Hyper Text Markup Language (HTML) included in it.
# MarySpeech does ot like the markup, so we need to get rid of it.
# To do that we use a HtmlFilter Service
# From Runtime, we create the HtmlFilter Service
htmlfilter = Runtime.createAndStart("htmlfilter", "HtmlFilter")

# Next we will add what is kown as data routing.
#First we will tell WKSR to send the text it has converted from speech to fred the ProgramAB service
wksr.addTextListener(fred)

# Then the text created by fred (ProgramAB) to the HtmlFilter
fred.addTextListener(htmlfilter)

# And Finally, the filtered text from the HtmlFilter to the MarySpeech we called mouth
htmlfilter.addTextListener(mouth)

# You now have enough to have a bit of a chat with your robot.
# Just as a tip, if you ask your robot it's name, it will answer Alice2.
# You can change this by telling your robot:
# Your Name is fred
# The robot will respond with you can call me fred.

# Next step is Have Fun.
