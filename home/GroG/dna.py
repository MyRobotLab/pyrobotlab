########################################################
# DNA - (Description of Neighboring Automata) 
# Some services are composites of other services. If written
# correctly these composites "bind" to other services using
# names. The following example shows how to share the same
# Arduino service between 2 different Tracking services.
#
# more info : http://myrobotlab.org/content/sample-inmoov-head-dna

from org.myrobotlab.service import Tracking

# print out the dna of a service
# you can get all of the names and types of services
# which a composite needs

# this command will show what the DNA would look like
# if you were going to start a Tracking service named tracker1
dna = Runtime.buildDNA("tracker1", "Tracking")
print (dna)


# this substitutes a name for a different name
Runtime.reserveRootAs("tracker1.arduino","sharedArduino")
Runtime.reserveRootAs("tracker2.arduino","sharedArduino")

# print our changes to the global registery
print(Runtime.getDNA())

# since you know the name of the service which will be shared you
# may create it first and apply additional configuration changes
# or other changes
sharedArduino = Runtime.create("sharedArduino","Arduino")
sharedArduino.connect("COM4")

# now start the 2 Tracking services
tracker1 = Runtime.start("tracker1","Tracking")
tracker2 = Runtime.start("tracker2","Tracking")
