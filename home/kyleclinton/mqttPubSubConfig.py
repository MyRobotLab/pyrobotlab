#########################################
# mqttPubSubConfig.py
#
# by Kyle Clinton
#########################################
###
# I am running Mosquitto on my main computer
# I know Mosquitto is available for Mac and Linux, 
# but I am sure it is also available or Windows too
###
from java.lang import String
python = Runtime.getService("python")

topicHearing = "myrobotlab/hearing"
topicSpeaking = "myrobotlab/speaking"
qos = 0 # At most once (0), At least once (1), Exactly once (2).
##Running Mosquitto on the same device that is running the "main" scripts
## broker on other machines will be the IP of this device on the network!
broker = "tcp://127.0.0.1:1883"
 
clientID = "MqttMainController"
mqtt = Runtime.start("mqttHearing", "Mqtt")
python = Runtime.start("python", "Mqtt")
 
print mqtt.getDescription()
 
mqtt.setBroker(broker)
mqtt.setQos(qos)
mqtt.setPubTopic(topicSpeaking)
mqtt.setClientId(clientID)
mqtt.connect(broker)
mqttHearing.subscribe(topicHearing, 0)

###For Testing
mqtt.publish("hello myrobotlab world")

python.subscribe("mqtt", "publishMqttMsgString")
