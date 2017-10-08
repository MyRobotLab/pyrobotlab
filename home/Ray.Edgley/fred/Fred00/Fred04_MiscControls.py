######################################
#  Misc Control Systems
######################################
# anything that doesn't fit in the Gestures 
# or AIML_OOB files goes in here

# This service is to set the control of the jaw to operate 
# with the robot talking. Currently not used as it was designed 
# for Arduino only
#mouthcontrol = Runtime.start("mouthcontrol","MouthControl")
#mouthcontrol.setJaw(jaw)
#mouthcontrol.setMouth(mouth)
#mouthcontrol.setmouth(jaw.getMin(),jaw.getMax())

#####################################
# Clock Service is used to put Fred to sleep 
# when there has been no activity for a while
#####################################
lockPhrase="hello fred"
inactivityTimeToSleep =600000

# define a sleep method
def goToSleep(timedata):
    fred01.wksr.lockOutAllGrammarExcept(lockPhrase)
    GoToSleep()
    clock.stopClock()

# define a wakeup method
def wakeUp():
    fred01.wksr.clearLock()
    clock.restartClock(True)
    WakeUpFromSleep()


clock = Runtime.start("clock","Clock")
clock.addListener("pulse", python.name, "goToSleep")
clock.setInterval(inactivityTimeToSleep)
clock.startClock(True)
