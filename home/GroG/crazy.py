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
