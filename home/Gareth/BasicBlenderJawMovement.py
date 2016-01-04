import bge
import serial
import math
from math import *
import mathutils

a=0.0  # variable to adjust jaw 

def read_serial():
  global a
  scene = bge.logic.getCurrentScene()  # Get the whole bge scene
  source = scene.objects               # Helper vars for convenience
  a=a+1

  main_arm = source.get('Armature')
  
  print((a))    # debug for blenders control console output
  
  ob = bge.logic.getCurrentController().owner
  ob.channels['jaw2'].joint_rotation = mathutils.Vector([radians(a/8),0,0])

  ob.update()  # do not forget this important step as it update the display GUI
