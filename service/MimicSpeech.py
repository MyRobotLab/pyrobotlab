#########################################
# MimicSpeech.py
# description: Speech synthesis based on Mimic from the MyCroft AI project.
# categories: speech, sound
# more info @: http://myrobotlab.org/service/MimicSpeech
#########################################

# start the service
mimicspeech = Runtime.start('mimicspeech','MimicSpeech')
mimicspeech.speakBlocking('hello, this is mimic speech from mycroft project')
mimicspeech.speakBlocking('I am a speech synthesis program')
mimicspeech.speakBlocking('How was that ?')
mimicspeech.speakBlocking('can someone fix my list voices, i think its broke')
