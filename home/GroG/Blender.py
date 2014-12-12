import bge                      #blender game engine
import bpy                      #blender python interface
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

bpy.data.objects["Cube"].data.vertices[0].co.x += 1.0

a=0.0

version = "0.9"
# the one and only controller
control = None
controlServer = None
controlPort = 8989
# I need a list of handlers - where can I get it?
# controlHandlers = []
serialHandlers = {}
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
  def __init__(self, name, type, serialHandler):
    self.name = name
    self.type = type
    self.serialHandler = serialHandler

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
  global control, serialHandlers, readyToAttach
  newDevice = VirtualDevice(name, type, None)
  serialHandlers[name] = newDevice
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
                    cnt = cnt + 1
                    
                    if isinstance(param, int):
                      command = command + str(param)
                    else:
                      command = command + "'" + param + "'"
                      
                    if (len(data) != cnt):
                      command = command + ","
                
                command = command + ")"
                
                print ("*** command " , command)
                
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
      name = ""
      
      def handle(self):
          global readyToAttach, serialHandlers
          
          #data = self.request.recv(1024).decode()
          myThread = threading.current_thread()
          
          print("++++serial client connected++++ thread {} port {}".format(myThread.name, serialPort))
          #self.request.sendall(response.encode())
          
          buffer = ''
          
          if (readyToAttach in serialHandlers):
            print("++++attaching " + str(readyToAttach) + " serial handler++++")
            serialHandlers[readyToAttach].serialHandler = self
            self.name = name
          else:
            # ERROR - we need a name to attach
            onError("XXXX incoming serial connection but readyToAttach [" + str(readyToAttach) + "] XXXX")
            return           
          
          listening = True
  #        serialHandlers[myThread.name] = self
  
          while listening:
            try:
              data = self.request.recv(1024)
              print (data)
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
  
  def handle(self):
    print 
 

