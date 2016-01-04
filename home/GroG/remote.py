# the mac
remote = Runtime.start("remote","RemoteAdapter")

# this sets the prefix name for any remotely connected services
# through this remote adapter - default if not set would be the
# {remote adatper name}.  e.g.  remote.x
remote.setDefaultPrefix("raspi")

# connect remotely
remote.connect("tcp://127.0.0.1:6767")

# give it a second or two to connect up
sleep(2)

# connect the remote raspi arduino to its local port 
python.send("raspiarduino", "connect","COM18")
sleep(1)

# turn off and on led 13 remotely
for x in range(0, 5):
  python.send("raspiarduino", "digitalWrite", 13, 1)
  sleep(1)
  python.send("raspiarduino", "digitalWrite", 13, 0)
  sleep(1)
  
 
