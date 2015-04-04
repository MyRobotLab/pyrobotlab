import bge # blender game engine
import bpy  # blender python interface
import math
import mathutils
from math import *


x = 0
def read_serial():
    global x
    x = x + 1
    ob = bge.logic.getCurrentController().owner
    ob.channels["jaw2"].joint_rotation = mathutils.Vector([radians(x/8),0,0])
    print(x)
    ob.update()
