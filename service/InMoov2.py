#########################################
# InMoov2.py VERY WIP !
# more info @: 
#########################################


inMoov = Runtime.start("inMoov", "InMoov2")

#every parameters are already stored from a previous execution of InMoov
#You can override them using attach method if you want :

# https://github.com/MyRobotLab/pyrobotlab/blob/develop/service/Skeleton.py

## starting mouth service
mouth=inMoov.startMouth()

## starting ear service
ear=inMoov.startEar()

# ...