#########################################
# AndroidSpeechRecognition + chatbot
#########################################

# start androidspeechrecognition
androidspeechrecognition = Runtime.start("androidspeechrecognition","AndroidSpeechRecognition")

# start a mouth
marySpeech = Runtime.start("marySpeech", "MarySpeech")

# shutdown microphone if robot speaking
androidspeechrecognition.attach(marySpeech)

# auto rearm microphone
androidspeechrecognition.setAutoListen(True)

chatBot=Runtime.start("chatBot", "ProgramAB")
chatBot.startSession("mister turing")

# attach androidspeechrecognition to chatBot
python.subscribe(androidspeechrecognition.getName(),"recognized",chatBot.getName(),"onText")

chatBot.addTextListener(marySpeech)