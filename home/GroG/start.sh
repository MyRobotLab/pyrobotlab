#! /bin/bash
#################################
# bash script for starting robot
#################################
REPOS_ROOT="/home/gperry/mrl.develop.head"

# refresh pyrobotlab repo
sudo -u gperry -H sh -c "cd /home/$REPOS_ROOT/pyrobotlab; git pull" 

# got to future "service" directory
cd /opt/mrl

# run java and execute script
# this starts only 1 service (besides Runtime) and its python
# after the python service is created the Sabertooth.py service script is executed
# it binds the joystick axis with the wheel motors
java -jar myrobotlab.jar -service python Python -invoke python execFile "/home/gperry/mrl.develop.head/pyrobotlab/service/Sabertooth.py"
