#########################################
# Relay.py
# description: Relay used by an arduino
# categories: home automation
# more info @: http://myrobotlab.org/service/Relay
#########################################

# start the service

relay = Runtime.start('relay','Relay')

arduino = Runtime.createAndStart("arduino","Arduino")
arduino.connect("COM3")

relay.arduino=arduino
relay.pin=1
relay.onValue=0

relay.on()
sleep(2)
relay.off()
