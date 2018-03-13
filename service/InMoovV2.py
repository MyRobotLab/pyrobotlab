#########################################
# InMoovV2.py VERY WIP
# more info @: 
#########################################


inMoov = Runtime.start("inMoov", "InMoovV2")

## parameters are already stored from a previous execution or from InMoov Gui
## You can override them here like this :

#inMoov.setLanguage(0)
#inMoov.setSpeechEngine("MarySpeech")
#inMoov.setEarEngine("WebkitSpeechRecognition")

## starting mouth service
mouth=inMoov.startMouth()

## starting ear service
ear=inMoov.startEar()

# ...