###########################################
#
#  Fred InMoov main command file
#
###########################################
# The main command processor hanlde a lot of the higher 
# brain functions such as interpreting the text from the Speech Recognition 
# Service and producing output to the TTS service
# Gesture movements are also controlled from this processor.

# lets setup the path for all of out scripts first.
RuningFolder="fred/fred00"
Fred01ipAddress = "192.168.1.21"
Fred02ipAddress = "192.168.1.22"

# Start the RemoteAdapter Service calling fir it from the Runtime Service.
fred01 = Runtime.createAndStart("fred01","RemoteAdapter")
#remote.setDefaultPrefix("Fred01")
fred01.connect('tcp://'+Fred01ipAddress+':6767')

# The ProgramAB service interperates the Alice2 AIML files
execfile(RuningFolder+'/Fred01_MainBrain.py')

#mouth.speakBlocking("Hello world")
#mouth.speakBlocking("Please wait while I start up my servo systems.")

# This file sets up the Gestures as used by Fred
execfile(RuningFolder+'/Fred02_Gestures.py')

# This file sets up the OOB data processing from the AIML process
execfile(RuningFolder+'/Fred03_AIML_OOB.py')

# Other miscilanous functions.
execfile(RuningFolder+'/Fred04_MiscControls.py')

fred01.mouth.speakBlocking("I have finished starting up.")
fred01.mouth.speakBlocking("What is your command?")
