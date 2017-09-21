#########################################
# ProgramAB.py
# more info @: http://myrobotlab.org/service/ProgramAB
#########################################

# create a ProgramAB service and start a session
alice = Runtime.start("alice", "ProgramAB")
alice.startSession("username")

print alice.getResponse("How are you?")

# create a Speech service
mouth = Runtime.start("mouth", "MarySpeech")
# create a route which sends published Responses to the
# mouth.speak(String) method
alice.addTextListener(mouth)

alice.getResponse("What is new?")
sleep(3)
alice.getResponse("Tell me a joke?")
sleep(3)
alice.getResponse("What time is it?")
sleep(3)
alice.getResponse("Goodbye")