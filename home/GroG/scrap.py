# dynamically grabbing sensors - http://www.blendenzo.com/tutBeginningBGEPython.html
# ----- begin ------

# ----

# getting a brick ---- begin ----
# http://blenderartists.org/forum/archive/index.php/t-302709.html
# This is because you can easily tell if an attached sensor is doing anything.
# Here's how you could check a single sensor:

import bge #Import game engine functions

cont = bge.logic.getCurrentController() #Get the controller the script is attached to
own = cont.owner #Get the object running the code. Unused in this script but good to know

move_act = cont.actuators['motion_actuator_name']
w_key = cont.sensors['sensor_name'] #Replace sensor_name with the name of teh sensor

if wkey.positive == True:
'''Do something, like move'''
cont.activate(move_act)

# getting a brick ---- end ----

# TODO
# way to dynamically add actuators & controllers
# http://www.blender.org/api/blender_python_api_2_60_6/bpy.ops.logic.html
import bge # blender game engine
import bpy  # blender python interface
import math
import sys
from os.path import expanduser
import socket
import threading
import socketserver
import json
import traceback

# FIXES
# bge dynamic import or absolute? path info ???
# clean/complete shutdown
# out of bge mode and back in - should still work - removal of all globals
# already started .... on start 
# BGE - restart does not work !!!
# when "run script" bge does not exist
# BGE - restarted - and sockets left running - everything reconnects fine BUT GRAPHICS DONT MOVE !!

import bge # blender game engine
import bpy  # blender python interface
import math
import sys
from os.path import expanduser
import socket
import threading
import socketserver
import json
import traceback

# FIXES
# bge dynamic import or absolute? path info ???
# clean/complete shutdown
# out of bge mode and back in - should still work - removal of all globals
# already started .... on start 
# BGE - restart does not work !!!
# when "run script" bge does not exist
# BGE - restarted - and sockets left running - everything reconnects fine BUT GRAPHICS DONT MOVE !!

# MRL is disconnected - BGE terminates then res
# when MRL is terminated and BGE is left running - can connect multiple times & threads appear to die as expected
# regular start/stop appears to work 

print("here")
#print(dir (bge.logic.getCurrentScene().objects["i01.head.jaw"]))
print(dir (bge.logic.getCurrentScene()))
obj = bge.logic.getCurrentScene().objects["i01.head.jaw"]
print("-------- obj begin ---------------")
print(dir(obj))
print("-------- obj end ---------------")
print("----- actuator begin ----")
print(dir(obj.actuators["i01.head.jaw"]))
print("----- actuator end ----")
actuator = obj.actuators["i01.head.jaw"]
print("dRot", actuator.dRot)
print("angV", actuator.angV)
#obj.appyRotation([1,0,0])

#obj.applyRotation([0, 0, -1.4], False)
#obj.applyRotation(actuator.dRot, True)
#for key, value in bge.logic.getCurrentScene().objects
#  print (key, "=>", val)

#print(len (bge.logic.getCurrentScene().objects))
#print(dir(bge.logic.getCurrentScene().objects["i01.head.jaw"]))

def frameClick():
    global obj, actuator
    #print("dRot", actuator.dRot)
    obj.applyRotation(actuator.dRot, True)
    print(actuator.dRot)
    print(obj.localOrientation)
    #obj.setOrientation(actuator.dRot)
    #obj.localOrientation = actuator.dRot
    #actuator = bge.logic.getCurrentScene().objects["i01.head.jaw"]
    #print("frameClick")
    
    
#-------------- crazy begin ------------------------

import bge
import math

pos = 1

def main():
    global pos
    pos += 1

    # print(dir(object))

    #cont = bge.logic.getCurrentController()
    #own = cont.owner

    #move = cont.actuators["move"]
    #cont.activate(move)
    #move.dLoc=[0,0.001,0]    
    
    scene = bge.logic.getCurrentScene()
    
    object = scene.objects["Spinal_Cord"]
    rotation = [ 0.0, 0.1, 0.0]
    object.applyRotation( rotation, False)
        
    object = scene.objects["Skull.Left"]
    rotation = [ 0.0, -0.01, 0.0]
    object.applyRotation( rotation, False)
    
    object = scene.objects["Servo_Jaw_Drive_shaft"]
    rotation = [ 0.0, -0.01, 0.0]
    object.applyRotation( rotation, False)
   
    object = scene.objects["MRL_logo"]
    rotation = [ 0.01, 0.01, 0.0]
    object.applyRotation( rotation, False)

    object = scene.objects["Ear_speaker_organic"]
    rotation = [ 0.01, 0.01, 0.0]
    object.applyRotation( rotation, False)
                    
    object = scene.objects["Skull.Right"]
    rotation = [ 0.01, 0.01, 0.0]
    object.applyRotation( rotation, True)
                    
  
#    cont = bge.logic.getCurrentController()
#    own = cont.owner   
    #print (a)    
#    xyz = own.localOrientation.to_euler()
#    xyz[0] = math.radians(pos/8)
#    own.localOrientation = xyz.to_matrix()
    
main()

#-------------- crazy end ------------------------

