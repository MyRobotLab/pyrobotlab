import bge                      #blender game engine
#import bpy                      #blender python interface
import math                     #Maths Module
import sys
from os.path import expanduser
import socket
import threading
import socketserver
import json
import traceback

home = expanduser("~")
print (home)
print (sys.version)
print (sys.path)

# bpy.data.objects["Cube"].data.vertices[0].co.x += 1.0

a=0.0

version = "0.9"
# the one and only controller
control = None
controlServer = None
controlPort = 8989
# I need a list of handlers - where can I get it?
# controlHandlers = []
virtualDevices = {}
readyToAttach = None

serialServer = None
serialPort = 9191

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

def getVersion():
  print("version is ", version)
  return version

# way to dynamically add actuators & controllers
# http://www.blender.org/api/blender_python_api_2_60_6/bpy.ops.logic.html

def AnaLoop():                
     global a                 
     a=a+1    
     #print (a)               
    
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
  global control
  print(msg)
  control.request.sendall(createJsonMsg("onError", msg))
    
def stopServer():
    global controlServer, serialServer
    print ("stopping controlServer")
    
    if (controlServer != None):
        controlServer.shutdown()
    else:
        print("controlServer already stopped")
    controlServer = None
    
    print ("stopping serialServer")
    
    if (serialServer != None):
        serialServer.shutdown()
    else:
        print("serialServer already stopped")
    serialServer = None
    
    #for controlHandler in controlHandlers
    #    print (controlHandler)
    #controlHandlers[controlHandler].listening = False  
    
def startServer():
    global controlServer, serialServer
    # Port 0 means to select an arbitrary unused port

    if (controlServer ==  None):
      ##### control server begin ####
      controlServer = ThreadedTCPServer(("localhost", controlPort), ControlHandler)
      ip, port = controlServer.server_address

      # Start a thread with the controlServer -- that thread will then start one
      # more thread for each request
      controlThread = threading.Thread(target=controlServer.serve_forever)
      # Exit the controlServer thread when the main thread terminates
      controlThread.daemon = True
      controlThread.start()
      print ("control server loop running in thread:", controlThread.name, " port ", controlPort)
      ##### control server end ####
      ##### serial server begin ####
      serialServer = ThreadedTCPServer(("localhost", serialPort), SerialHandler)
      ip, port = serialServer.server_address

      # Start a thread with the serialServer -- that thread will then start one
      # more thread for each request
      serialThread = threading.Thread(target=serialServer.serve_forever)
      # Exit the serialServer thread when the main thread terminates
      serialThread.daemon = True
      serialThread.start()
      print ("serial server loop running in thread:", serialThread.name, " port ", serialPort)
      ##### serial server end ####
    else:
      print ("servers already started")
        

# attach a device - control message comes in and sets up
# name and type - next connection on the serial port will be
# the new device
def attach(name, type):
  global control, virtualDevices, readyToAttach
  # adding name an type to new virtual device
  newDevice = VirtualDevice(name, type)
  # constructing the correct type
  newDevice.service = eval(type + "('" + name + "')")
  virtualDevices[name] = newDevice
  readyToAttach = name
  global control
  print("onAttach " + str(name) + " " + str(type) + " SUCCESS - ready for serial connection")
  # print("<--- sending control onAttach(" + str(name) + ")")
  # control.request.sendall(createJsonMsg("onAttach", name))
  return name

    
class ControlHandler(socketserver.BaseRequestHandler):
    global control    
    listening = False
    
    def handle(self):
        global control
        control = self
        #data = self.request.recv(1024).decode()
        myThread = threading.current_thread()
        
        print("client connected to control socket thread {} port {}".format(myThread.name, controlPort))
        #self.request.sendall(response.encode())
        
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
          global readyToAttach, virtualDevices
          
          myThread = threading.current_thread()
                              
          if (readyToAttach in virtualDevices):
            print("++++attaching " + str(readyToAttach) + " serial handler++++ thread {} port {}".format(myThread.name, serialPort))
            virtualDevices[readyToAttach].serialHandler = self
            service = virtualDevices[readyToAttach].service
            self.name = readyToAttach
          else:
            # ERROR - we need a name to attach
            onError("XXXX incoming serial connection but readyToAttach [" + str(readyToAttach) + "] XXXX")
            return           
          
          listening = True
  #        virtualDevices[myThread.name] = self
  
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

def client(ip, port, message):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, port))
    try:
        sock.sendall(message)
        response = sock.recv(1024).encode
        print ("Received: {}".format(response))
    finally:
        sock.close()
        
class Arduino:
  def __init__(self, name):
    print("creating new Arduino ", name)
    self.name = name
    self.servos = {}
    self.msgByteCount = 0
    self.msgSize = 0
    self.method = 0
    self.params = []
    self.version = 20
    
  def sendMRLCOMMMsg(self, method, value):
    socket = virtualDevices[self.name].serialHandler.request
    print("sending bytes")
    print(bytes([170, method, 1, value]))
    # MRLCOMM PROTOCOL
    # MAGIC_NUMBER|NUM_BYTES|FUNCTION|DATA0|DATA1|....|DATA(N)
    #              NUM_BYTES - is the number of bytes after NUM_BYTES to the end
    
    socket.sendall(bytes([170, 2, method, value]))

  def handle(self, byteArray):
    global pos, virtualDevices, version
    newByteCnt = len(byteArray)
    # print (self.name + " recvd " + str(newByteCnt) + " bytes")
    # print(byteArray)
    
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

      # full valid message
      if (self.msgByteCount - 2 == self.msgSize and self.msgSize != 0):
        
        # GET_VERSION
        if (self.method == 26):
          print("GET_MRLCOMM_VERSION")
          self.sendMRLCOMMMsg(26, self.version)          
        elif (self.method == 6):
          print("SERVO_ATTACH", self.params)
        elif (self.method == 7):
          print("SERVO_WRITE", self.params)
          #moveTo(self.params[1])
          pos = self.params[1]
        elif (self.method == 8):
          print("SERVO_SET_MAX_PULSE", self.params)
        elif (self.method == 9):
          print("SERVO_DETACH", self.params)
        elif (self.method == 12):
          print("SET_SERVO_SPEED", self.params)
        elif (self.method == 28):
          print("SERVO_WRITE_MICROSECONDS", self.params)
        else:
          print ("UNKNOWN METHOD ", self.method, self.params)
        
        #print("MRLCOMM msg done ")
        self.msgSize = 0
        self.msgByteCount = 0
        self.params = []
          
      # do command

class Servo:
  def __init__(self, name):
    print("creating new Servo ", name)
    self.name = name

pos = 0.0

#def moveTo(pos):
def moveTo():
    global pos
    #print ("moving servo to ", pos)
    scene = bge.logic.getCurrentScene()
    cont = bge.logic.getCurrentController()
    own = cont.owner   
    #print (a)    
    xyz = own.localOrientation.to_euler()
    xyz[0] = math.radians(pos/8)
    own.localOrientation = xyz.to_matrix()
    
def frameTick():
  """Always block will drive this to update all data which would effect the scene"""
  # iterate through global containers
  # if data different than last time - update scene
  # this method should be quick 
  print("tick")
    
def endcomm():
    bge.logic.endGame()    
    