#start Service
#download & extract at mrl root : http://www.myai.cloud/mrl/mary-mrl-ru.zip
mouth = Runtime.start("MarySpeech", "MarySpeech")
mouth.setVoice("ac-nsh")
mouth.speakBlocking(u"привет")