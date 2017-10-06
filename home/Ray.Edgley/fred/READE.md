#########################################
##                                     ##
##  Fred InMoov Configuration Scripts  ##
##                                     ##
#########################################

  Fred is an InMoov series robot with a difference.
  While most InMoov series robots used an x86 based computer
  Fred uses the smaller cheaper Raspberry Pi 3 ARM based computer.
  
  The Raspberry Pi 3 (RPi3) is no where as powerfull as the x86 computers,
  so to overcome this limitation, we will use more than one RPI3 computer.
  
  During initial test and development using the single RPi3, is was found 
  that Fred would from time to time stutter.
  
  With a start of 3 x RPI3 we can have the following:
  
  #  Fred00 is the main brain running ProgramAB along with the Gestures 
     and OOB scripts
  
  #  Fred01 is the servo control along with speech recognition and 
     Text To Speech (TTS) output
  
  #  Fred02 is for OpenCV which does Face Detection.
  
  Each of the RPi3 scrips are separated into sub folders for each of the RPI3's.
  
