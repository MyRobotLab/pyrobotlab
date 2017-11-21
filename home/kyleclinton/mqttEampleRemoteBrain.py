from java.lang import String
from time import sleep
pi = Runtime.createAndStart("pi","RasPi")

#Load Pub/Sub Service (MQTT)
execfile("../py_scripts/mqttPubSubConfig.py")


# Add in controller for head, neck and antenna servos SHOULD be using i2c 16 servo controller
#Load Juniors mouth!
execfile("../py_scripts/juniors_voice.py")

#Load Juniors Eyes!
execfile("../py_scripts/juniors_eyes_4.py")

#####for testing
mouth.speakBlocking("Testing 1, 2, 3")


drawEyes()
sleep(2)
drawClosedEyes()
sleep(1)
drawEyes()

mqtt.subscribe("myrobotlab/speaking", 0)
#mqtt.publish("hello myrobotlab world")
python.subscribe("mqtt", "publishMqttMsgString")
# or mqtt.addListener("publishMqttMsgString", "python")
 
#  MQTT call-back
# publishMqttMsgString --> onMqttMsgString(msg)
def onMqttMsgString(msg):
  # print "message : ", msg
  mouth.speakBlocking(msg[0])
  print "message : ",msg[0]
  print "topic : ",msg[1]



mqtt.publish("What is your name?")
