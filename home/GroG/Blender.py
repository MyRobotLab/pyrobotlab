# TODO
# way to dynamically add actuators & controllers
# http://www.blender.org/api/blender_python_api_2_60_6/bpy.ops.logic.html
import bge # blender game engine
import bpy  # blender python interface
import math
import mathutils
import sys
from os.path import expanduser
import socket
import threading
import socketserver
import json
import traceback
import math
from math import *
import mathutils


# FIXES
# clean/complete shutdown
# out of bge mode and back in - should still work - removal of all globals
# already started .... on start 
# BGE - restart does not work !!!
# when "run script" bge does not exist
# BGE - restarted - and sockets left running - everything reconnects fine BUT GRAPHICS DONT MOVE !!

# MRL is disconnected - BGE terminates then restarts - connections look normal but mouth does not move !

# WORKS
# when MRL is terminated and BGE is left running - can connect multiple times & threads appear to die as expected
# regular start/stop appears to work 

home = expanduser("~")
print (home)
print (sys.version)
print (sys.path)

controlPort = 8989
serialPort  = 9191

readyToAttach = None # must I remove this too ?

#-------- obj begin ---------------
# ['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__','__hash__', '__init__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__','__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'actuators', 'addDebugProperty', 'alignAxisToVect', 'angularVelocity', 'applyForce', 'applyImpulse', 'applyMovement', 'applyRotation', 'applyTorque', 'attrDict', 'children', 'childrenRecursive', 'collisionCallbacks','color', 'controllers', 'debug', 'debugRecursive', 'disableRigidBody', 'enableRigidBody', 'endObject', 'get', 'getActionFrame', 'getAngularVelocity', 'getAxisVect', 'getDistanceTo', 'getLinearVelocity', 'getPhysicsId', 'getPropertyNames','getReactionForce', 'getVectTo', 'getVelocity', 'groupMembers', 'groupObject', 'invalid', 'isPlayingAction', 'life', 'linVelocityMax', 'linVelocityMin', 'linearVelocity', 'localAngularVelocity', 'localInertia', 'localLinearVelocity', 'localOrientation', 'localPosition', 'localScale', 'localTransform', 'mass', 'meshes','name', 'occlusion', 'orientation', 'parent', 'playAction', 'position', 'rayCast', 'rayCastTo', 'record_animation', 'reinstancePhysicsMesh', 'removeParent', 'replaceMesh', 'restoreDynamics', 'scaling', 'scene', 'sendMessage', 'sensors', 'setActionFrame', 'setAngularVelocity', 'setCollisionMargin', 'setLinearVelocity','setOcclusion', 'setParent', 'setVisible', 'state', 'stopAction', 'suspendDynamics', 'timeOffset', 'visible', 'worldAngularVelocity', 'worldLinearVelocity', 'worldOrientation', 'worldPosition', 'worldScale', 'worldTransform']-------- obj end ---------------

print("-------- scene begin ---------------")
scene = bge.logic.getCurrentScene()
# help(scene)
print(dir(scene))
print("-------- scene end ---------------")

  
"""
obj = scene.objects["i01.head.jaw"]
print("-------- obj begin ---------------")
print(dir(obj))
print("-------- obj end ---------------")
print("localOrientation", obj.localOrientation)
print("localPosition", obj.localPosition)
print("----- actuator begin ----")
print(dir(obj.actuators["i01.head.jaw"]))
print("----- actuator end ----")
actuator = obj.actuators["i01.head.jaw"]
print("dRot", actuator.dRot)
print("angV", actuator.angV)

obj.applyRotation([ 0.1, 0.0, 0.0], True)

print("localOrientation", obj.localOrientation)

# euler rotations
xyz = obj.localOrientation.to_euler()
xyz[0] = math.radians(10)
obj.localOrientation = xyz.to_matrix()

# create a rotation matrix
mat_rot = mathutils.Matrix.Rotation(math.radians(10.0), 4, 'X')
print("mat_rot", mat_rot)
# mat_rot = mathutils.Matrix.Rotation(math.radians(10.0), 3, 'X')

# extract components back out of the matrix
#loc, rot, sca = obj.localOrientation.decompose()
#print(loc, rot, sca)
#obj.applyRotation(mat_rot)
#obj.localTransform = mat_rot

#obj.localOrientation = mat_rot.to_3x3()

"""

# TODO - derive from json object - so we can control correct encoding
# http://stackoverflow.com/questions/3768895/python-how-to-make-a-class-json-serializable
class MyRobotLab:
  """the MyRobotLab class - mrl manages the control and serial servers which the middleware interfaces with"""
  def __init__(self):
    self.control = None
    self.controlServer = None
    self.serialServer = None
    self.virtualDevices = {}
    self.blenderObjects = {}
    self.version = "0.9"
    self.pos = 0.0
    
  def toJson(self):
    ret = "{'control': "
    ret += "'initialized'" if (self.control != None) else "'None'"
    ret += ", 'controlServer': "
    ret += "'initialized'" if (self.controlServer != None) else "'None'"
    ret += ", 'serialServer': "
    ret += "'initialized'" if (self.serialServer != None) else "'None'"
    ret += ", 'virtualDevices': ["
    
    vdJson = []
   
    print(self.virtualDevices)
    for vd in self.virtualDevices:
      print("virtual device [" + vd + "]")
      #vdJson.append("'" + vd + "': " + self.virtualDevices[vd])
      #vdJson.append("'" + vd + "': '" + vd + "'")
    
    ret += ",".join(self.virtualDevices)
    ret += "]"
    
    ret += "}"
    return ret
    
def toJson():
  return bpy.mrl.toJson();
    
# this is to initialize the mrl data
# it needs persist longer than just game mode
if (not hasattr(bpy, "mrl")):
    print("initializing MyRobotLab")
    bpy.mrl = MyRobotLab()
else:
    print("MyRobotLab already initialized")

class Message:
  """an MRL message definition in Python"""
  def __init__(self):
    self.msgID = 0
    self.timeStamp = 0
    self.name = ""
    self.sender = ""
    self.method = ""
    self.sendingMethod = ""
    self.data = []
    self.historyList = []
    #def __init__(self, j):
      #self.__dict__ = json.loads(j)
      
class VirtualDevice:
  """a virtual device Servo, Arduino, Lidar, etc"""
  def __init__(self, name, type):
    self.name = name
    self.type = type
    self.serialHandler = None
    self.service = None
   
  def toJson(self):
    ret = "{'name':'" + self.name + "', 'type':'" + self.type + "',"
    ret += "'serialHandler': '"
    ret += "'initialized'" if (self.serialHandler != None) else "'None'"
    ret += "'service': '"
    ret += "'initialized'" if (self.service != None) else "'None'"
    ret += "}"

def getVersion():
  print("version is ", bpy.mrl.version)
  return bpy.mrl.version

# TODO remove?
def Cube():
    global a
    #print ("cube ", a)
    scene = bge.logic.getCurrentScene()     #Locate current device
    cont = bge.logic.getCurrentController()
    own = cont.owner   
 
    xyz = own.localOrientation.to_euler()   #Extract the Rotation Data    
    xyz[0] = math.radians(a)                #PreLoad your RX data
                                            #xyz[0] x Rotation axis
                                            #xyz[1] y Rotation axis
                                            #xyz[2] z Rotation axis
    own.localOrientation = xyz.to_matrix()  #Apply your rotation data
  
def createJsonMsg(method, data):
  msg = Message()
  msg.name = "blender"
  msg.method = method
  msg.sendingMethod = method
  msg.data.append(data)
  retJson = json.dumps(msg.__dict__)
  # FIXME - better terminator ?
  retJson = retJson + "\n"
  return retJson.encode()

def onError(msg):
  print(msg)
  request = bpy.mrl.control.request
  request.sendall(createJsonMsg("onError", msg))
    
def stopServer():
    print ("stopping controlServer")
    controlServer = bpy.mrl.controlServer
    
    if (controlServer != None):
        controlServer.shutdown()
    else:
        print("controlServer already stopped")
    bpy.mrl.controlServer = None
    
    print ("stopping serialServer")
    
    serialServer = bpy.mrl.serialServer
    
    if (serialServer != None):
        serialServer.shutdown()
    else:
        print("serialServer already stopped")
    bpy.mrl.serialServer = None
    
    #for controlHandler in controlHandlers
    #    print (controlHandler)
    #controlHandlers[controlHandler].listening = False  
    
def startServer():
    global controlPort
    controlServer = bpy.mrl.controlServer
    if (controlServer ==  None):
      ##### control server begin ####
      controlServer = ThreadedTCPServer(("localhost", controlPort), ControlHandler)
      bpy.mrl.controlServer = controlServer
      ip, port = controlServer.server_address

      # Start a thread with the controlServer -- that thread will then start one
      # more thread for each request
      controlThread = threading.Thread(target=controlServer.serve_forever)
      # Exit the controlServer thread when the main thread terminates
      controlThread.daemon = True
      controlThread.start()
      print ("control server loop running in thread: ", controlThread.name, " port ", controlPort)
      ##### control server end ####
      ##### serial server begin ####
      serialServer = ThreadedTCPServer(("localhost", serialPort), SerialHandler)
      bpy.mrl.serialServer = serialServer
      ip, port = serialServer.server_address

      # Start a thread with the serialServer -- that thread will then start one
      # more thread for each request
      serialThread = threading.Thread(target=serialServer.serve_forever)
      # Exit the serialServer thread when the main thread terminates
      serialThread.daemon = True
      serialThread.start()
      print ("serial server loop running in thread: ", serialThread.name, " port ", serialPort)
      ##### serial server end ####
    else:
      print ("servers already started")
        

# attach a device - control message comes in and sets up
# name and type - next connection on the serial port will be
# the new device
# FIXME - catch throw on class not found
def attach(name, type):
  global readyToAttach
  # adding name an type to new virtual device
  newDevice = VirtualDevice(name, type)
  # constructing the correct type
  newDevice.service = eval(type + "('" + name + "')")
  bpy.mrl.virtualDevices[name] = newDevice
  readyToAttach = name
  print("onAttach " + str(name) + " " + str(type) + " SUCCESS - ready for serial connection")
  # print("<--- sending control onAttach(" + str(name) + ")")
  # control.request.sendall(createJsonMsg("onAttach", name))
  return name

    
class ControlHandler(socketserver.BaseRequestHandler):
    listening = False
    
    def handle(self):
        bpy.mrl.control = self
        #data = self.request.recv(1024).decode()
        myThread = threading.current_thread()
        
        print("---> client connected to control socket thread {} port {}".format(myThread.name, controlPort))
        
        buffer = ''
        
        listening = True

        while listening:
            try:
                # Try to receive som data
                # data = self.request.recv(1024).decode()
                # TODO - refactor to loading Message object
                controlMsg = json.loads(self.request.recv(1024).decode().strip())
                
                print("---> control: controlMsg ", controlMsg)
                method = controlMsg["method"]
                
                #### command processing begin ####
                command = method + "("
                cnt = 0
                
                # unload parameter array
                data = controlMsg["data"]
                if (len(data) > 0):
                  for param in data:
                    cnt += 1
                    
                    if isinstance(param, int):
                      command = command + str(param)
                    else:
                      command = command + "'" + param + "'"
                      
                    if (len(data) != cnt):
                      command = command + ","
                
                command = command + ")"
                
                print ("*** command " , command, " ***")
                
                ret = eval(command)
                retMsg = Message()
                retMsg.name = "blender"
                retMsg.method = "on" + method[0:1].capitalize() + method[1:]
                retMsg.sendingMethod = controlMsg["method"]
                retMsg.data.append(ret)
                
                retJson = json.dumps(retMsg.__dict__)
                
                print ("<--- control: ret" , retJson)
                
                self.request.sendall(retJson.encode())
                # TODO - better way to send full json message ? better way to parse it?
                self.request.sendall("\n".encode())
                #### command processing end ####
            
            except Exception as e:  
                print ("control handler error: ", e)
                print (traceback.format_exc())
                #run_main_loop = False
                listening = False
        
        print("terminating control handler", myThread.name, controlPort)


class SerialHandler(socketserver.BaseRequestHandler):
      listening = False
      service = None
      name = ""
      
      def handle(self):
          global readyToAttach
          
          myThread = threading.current_thread()
          
          if (readyToAttach in bpy.mrl.virtualDevices):
            print("++++attaching " + str(readyToAttach) + " serial handler++++ thread {} port {}".format(myThread.name, serialPort))
            bpy.mrl.virtualDevices[readyToAttach].serialHandler = self
            service = bpy.mrl.virtualDevices[readyToAttach].service
            self.name = readyToAttach
          else:
            print("could not attach serial device")
            # ERROR - we need a name to attach
            onError("XXXX incoming serial connection but readyToAttach [" + str(readyToAttach) + "] XXXX")
            return           
          
          listening = True
  
          while listening:
            try:
              data = self.request.recv(1024)
              service.handle(data)

            except Exception as e:  
                print ("serial handler error: ", e)
                print (traceback.format_exc())
                #run_main_loop = False
                listening = False
        
          print("terminating serial handler", myThread.name, serialPort)
         
class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass
        
class Arduino:
  
  MRLCOMM_VERSION = 21

  ##### PYTHON GENERATED DEFINITION BEGIN ######
  # {publishMRLCommError Integer} 
  PUBLISH_MRLCOMM_ERROR = 1

  # {getVersion} 
  GET_VERSION = 2

  # {publishVersion Integer} 
  PUBLISH_VERSION = 3

  # {analogReadPollingStart Integer} 
  ANALOG_READ_POLLING_START = 4

  # {analogReadPollingStop Integer} 
  ANALOG_READ_POLLING_STOP = 5

  # {analogWrite Integer Integer} 
  ANALOG_WRITE = 6

  # {digitalReadPollingStart Integer} 
  DIGITAL_READ_POLLING_START = 7

  # {digitalReadPollingStop Integer} 
  DIGITAL_READ_POLLING_STOP = 8

  # {digitalWrite Integer Integer} 
  DIGITAL_WRITE = 9

  # {motorAttach String String Integer Integer Integer} 
  MOTOR_ATTACH = 10

  # {motorDetach String} 
  MOTOR_DETACH = 11

  # {motorMove String} 
  MOTOR_MOVE = 12

  # {motorMoveTo String double} 
  MOTOR_MOVE_TO = 13

  # {pinMode Integer Integer} 
  PIN_MODE = 14

  # {publishCustomMsg Integer} 
  PUBLISH_CUSTOM_MSG = 15

  # {publishLoadTimingEvent Long} 
  PUBLISH_LOAD_TIMING_EVENT = 16

  # {publishPin Pin} 
  PUBLISH_PIN = 17

  # {publishPulse Integer} 
  PUBLISH_PULSE = 18

  # {publishServoEvent Integer} 
  PUBLISH_SERVO_EVENT = 19

  # {publishSesorData SensorData} 
  PUBLISH_SESOR_DATA = 20

  # {publishStepperEvent StepperEvent} 
  PUBLISH_STEPPER_EVENT = 21

  # {publishTrigger Pin} 
  PUBLISH_TRIGGER = 22

  # {pulseIn int int int int} 
  PULSE_IN = 23

  # {sensorAttach String} 
  SENSOR_ATTACH = 24

  # {sensorPollingStart String int} 
  SENSOR_POLLING_START = 25

  # {sensorPollingStop String} 
  SENSOR_POLLING_STOP = 26

  # {servoAttach String Integer} 
  SERVO_ATTACH = 27

  # {servoDetach Servo} 
  SERVO_DETACH = 28

  # {servoSweepStart String int int int} 
  SERVO_SWEEP_START = 29

  # {servoSweepStop String} 
  SERVO_SWEEP_STOP = 30

  # {servoWrite String Integer} 
  SERVO_WRITE = 31

  # {servoWriteMicroseconds String Integer} 
  SERVO_WRITE_MICROSECONDS = 32

  # {setDebounce int} 
  SET_DEBOUNCE = 33

  # {setDigitalTriggerOnly Boolean} 
  SET_DIGITAL_TRIGGER_ONLY = 34

  # {setLoadTimingEnabled boolean} 
  SET_LOAD_TIMING_ENABLED = 35

  # {setPWMFrequency Integer Integer} 
  SET_PWMFREQUENCY = 36

  # {setSampleRate int} 
  SET_SAMPLE_RATE = 37

  # {setSerialRate int} 
  SET_SERIAL_RATE = 38

  # {setServoEventsEnabled String boolean} 
  SET_SERVO_EVENTS_ENABLED = 39

  # {setServoSpeed String Float} 
  SET_SERVO_SPEED = 40

  # {setStepperSpeed Integer} 
  SET_STEPPER_SPEED = 41

  # {setTrigger int int int} 
  SET_TRIGGER = 42

  # {softReset} 
  SOFT_RESET = 43

  # {stepperAttach String} 
  STEPPER_ATTACH = 44

  # {stepperDetach String} 
  STEPPER_DETACH = 45

  # {stepperMoveTo String int int} 
  STEPPER_MOVE_TO = 46

  # {stepperReset String} 
  STEPPER_RESET = 47

  # {stepperStop String} 
  STEPPER_STOP = 48

  # {stopService} 
  STOP_SERVICE = 49


##### PYTHON GENERATED INTERFACE END ##### 
  def __init__(self, name):
    print("creating new Arduino ", name)
    self.name = name
    self.servos = {}
    self.msgByteCount = 0
    self.msgSize = 0
    self.method = 0
    self.params = []
    
  def sendMRLCOMMMsg(self, method, value):
    socket = bpy.mrl.virtualDevices[self.name].serialHandler.request
    print("sending bytes")
    print(bytes([170, method, 1, value]))
    # MRLCOMM PROTOCOL
    # MAGIC_NUMBER|NUM_BYTES|FUNCTION|DATA0|DATA1|....|DATA(N)
    #              NUM_BYTES - is the number of bytes after NUM_BYTES to the end
    
    socket.sendall(bytes([170, 2, method, value]))

  def handle(self, byteArray):
    newByteCnt = len(byteArray)
    # print (self.name + " recvd " + str(newByteCnt) + " bytes")
    # print(byteArray)
    
    # parse MRL Msg
    for newByte in byteArray: 
      self.msgByteCount += 1
      # print("byte ", newByte, " byteCount  ", self.msgByteCount, " size ", self.msgSize)
      # check magic
      if (self.msgByteCount == 1):
        if (newByte != 170):
          print("ERROR message does not begin with MAGIC")
          self.msgByteCount = 0
          self.msgSize = 0
      elif (self.msgByteCount == 2):      
        # print command - TODO error checking > 64        
        self.msgSize = newByte
        # print("MRLCOMM msg size is " + str(self.msgSize))
      elif (self.msgByteCount == 3):  
        # print("MRLCOMM method is " + str(newByte))
        self.method = newByte
      elif (self.msgByteCount > 3 and self.msgByteCount - 3 < self.msgSize):  
        # print("MRLCOMM datablock")
        self.params.append(newByte)
      elif (self.msgByteCount > 3 and self.msgByteCount - 3 > self.msgSize):  
        print("MRLCOMM ERROR STATE - resetting ")
        self.msgSize = 0
        self.msgByteCount = 0
        self.params = []

      # now we have a full valid message
      if (self.msgByteCount - 2 == self.msgSize and self.msgSize != 0):
        print("Arduino Msg Method # -> ", self.method)
        # GET_VERSION
        if (self.method == self.GET_VERSION):
          print("GET_MRLCOMM_VERSION")
          self.sendMRLCOMMMsg(self.PUBLISH_VERSION, self.MRLCOMM_VERSION)          
        elif (self.method == self.SERVO_ATTACH):
          print("SERVO_ATTACH", self.params)
          # create "new" servo if doesnt exist
          # attach to this Arduino's set of servos
          params = self.params
          servoIndex = params[0]
          servoPin = params[1]
          
          servoName = ""
          for x in range(3, params[2]+3):
            servoName += chr(params[x])
          print ("servo index", servoIndex, "pin", servoPin, "name", servoName)
          self.servos[servoIndex] = servoName
          bpy.mrl.blenderObjects[servoName] = 0 # rest position? 90 ?
        elif (self.method == self.SERVO_WRITE):
          print("SERVO_WRITE", self.params)
          servoIndex = self.params[0]
          pos = self.params[1]
          servoName = self.servos[servoIndex]
          ob = bge.logic.getCurrentController().owner
          if (servoName in ob.channels):
            ob.channels[servoName].joint_rotation = mathutils.Vector([radians(pos),0,0])
            ob.update()
            print("WROTE ", servoName, radians(-pos+90))
          else:
            print("ERROR can't find bone ", servoName)
        elif (self.method == self.SERVO_DETACH):
          print("SERVO_DETACH", self.params)
        elif (self.method == self.SET_SERVO_SPEED):
          print("SET_SERVO_SPEED", self.params)
        elif (self.method == self.SERVO_WRITE_MICROSECONDS):
          print("SERVO_WRITE_MICROSECONDS", self.params)
        else:
          print ("ERROR UNKNOWN METHOD ", self.method, self.params)
        
        #print("MRLCOMM msg done ")
        self.msgSize = 0
        self.msgByteCount = 0
        self.params = []
          
      # do command


def client(ip, port, message):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, port))
    try:
        sock.sendall(message)
        response = sock.recv(1024).encode
        print ("Received: {}".format(response))
    finally:
        sock.close()
    
def endcomm():
    print("endcomm")
    bge.logic.endGame()    
    
    
startServer()

frame = 0
def frameTick():
    global frame
    frame = frame + 1