from time import sleep
# The geofence and measure distance methods should be available in MRL > 1.0.86

gps1 = Runtime.start("gps1", "GPS")

gps1.connect("/dev/tty.palmOneGPS-GPSSerialOut")
sleep(1)

# define some points ... 
# Lets use Nova Labs 1.0
lat1 = 38.950829
lon1 = -77.339502
# and Nova Labs 2.0
lat2 = 38.954471 
lon2 = -77.338271
# and the nearest Metro station
lat3 = 38.947254
lon3 = -77.337844
# and the Sand Trap out back
lat4 = 38.954844
lon4 = -77.338797

def input():
  startingAngle = 0
  Latitude = msg_gps1_publishGGAData.data[0][2]
  Longitude =  msg_gps1_publishGGAData.data[0][4]
  altitude = msg_gps1_publishGGAData.data[0][9]
  print "Lat: " + Latitude
  print "Long: " + Longitude
  print "Alt: " + altitude + "\n"
  

#have python listening to lidar
gps1.addListener("publishGGAData", python.name, "input") 

print "Ready to receive Data from GPS..."

print "Let's put a 100 meter GeoFence around around Nova Labs 2.0"
# create a point based geofence with a 100m radius
geofence = gps1.setPointGeoFence(lat2, lon2, 100)

distance = gps1.calculateDistance(lon1, lat1, lon2, lat2)

# check if a GPS point is inside the fence
if (gps1.checkInside(geofence, lat1, lon1)):
    print "Inside the Fence"
else:
    print "Outside the Fence"
print "Distance (meters): ",distance," between Nova Labs 1.0 and Nova Labs 2.0\n"

distance = gps1.calculateDistance(lon2, lat2, lon3, lat3)

# check if a GPS point is inside the fence
if (gps1.checkInside(geofence, lat3, lon3)):
    print "Inside the Fence"
else:
    print "Outside the Fence"
print "Distance (meters): ",distance, " between NL 2 and the nearest Metro Station\n"

distance = gps1.calculateDistance(lon2, lat2, lon4, lat4)

# check if a GPS point is inside the fence
if (gps1.checkInside(geofence, lat4, lon4)):
    print "Inside the Fence"
else:
    print "Outside the Fence"
print "Distance (meters): ",distance, "between NL 2 and the nearest sand trap\n"
