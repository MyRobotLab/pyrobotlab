#########################################
# IndianTts.py
# description: used as a general template
# more info @: http://myrobotlab.org/service/IndianTts
#########################################
tts=Runtime.start("tts", "IndianTts")
#change api and user
tts.api="2d108780-0b86-11e6-b056-07d516fb06e1"
tts.userid="80"
tts.speak(u"नमस्ते भारत मित्र")
