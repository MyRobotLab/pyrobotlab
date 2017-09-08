#!/bin/bash



killall -9 java
sleep 1
cd /home/pi/mrl


rm myrobotlab.log.1
mv myrobotlab.log myrobotlab.log.1

# make sure the serial ports and arduinos are reset before starting
/home/pi/reset.py
sleep 1

# export JAVA_OPTS=\"-Xdebug -Xrunjdwp:server=y,transport=dt_socket,address=4000, suspend=n Djava.library.path=libraries/native, -Djna.library.path=libraries/native, -Dfile.encoding=UTF-8\"
# java -jar myrobotlab.jar -jvm $JAVA_OPTS -service runtime Runtime python Python gui SwingGui -invoke python execFile /home/pi/github/pyrobotlab/home/kwatters/Harry.py

java -jar myrobotlab.jar -service runtime Runtime python Python gui SwingGui -invoke python execFile /home/pi/github/pyrobotlab/home/kwatters/Harry.py

