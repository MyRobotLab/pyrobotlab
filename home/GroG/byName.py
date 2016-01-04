import bge
import math


a = 0.0  #Default start position of Servo

    
def JawMech():
    global a
    a = a + 1
    
    scene = bge.logic.getCurrentScene()
    
    object = scene.objects["Servo_Jaw_Drive_shaft"]
    xyz = object.localOrientation.to_euler()
    xyz[0] = math.radians(a)
    object.localOrientation = xyz.to_matrix()
    
#    rotation = [ 0.01, 0.01, 0.0]
#    object.applyRotation( rotation, True)
    

#    cont = bge.logic.getCurrentController()
#    own = cont.owner   
    #print (a)    
#    xyz = own.localOrientation.to_euler()
#    xyz[0] = math.radians(a/8)
#    own.localOrientation = xyz.to_matrix()
    