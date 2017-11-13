#########################################
# AndroidSpeechRecognition.py
# more info @: http://myrobotlab.org/service/AndroidSpeechRecognition
# client : https://github.com/moz4r/SpeechRecognitionMRL/blob/master/AndroidSpeechRecognition.apk
#########################################

# start the service
androidspeechrecognition = Runtime.start("androidspeechrecognition","AndroidSpeechRecognition")

# start mouth
marySpeech = Runtime.createAndStart("marySpeech", "MarySpeech")

# auto rearm microphone
androidspeechrecognition.setAutoListen(True)
androidspeechrecognition.addCommand("turn on the light", "python", "lightOn")
androidspeechrecognition.addCommand("turn off the light", "python", "lightOff")

def lightOn():
  marySpeech.speakBlocking("light is on")

def lightOff():
  marySpeech.speakBlocking("light is off")