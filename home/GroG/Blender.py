import bge                      #blender game engine
import bpy                      #blender python interface
import math                     #Maths Module
import sys
from os.path import expanduser
import socket
import threading
import socketserver
import json

home = expanduser("~")
print (home)
print (sys.version)
print (sys.path)

bpy.data.objects["Cube"].data.vertices[0].co.x += 1.0

a=0.0
version = "0.9"
controlServer = None
controlPort = 8989
# I need a list of handlers - where can I get it?
controlHandlers = []

serialServer = None
serialPort = 9191

class Message(object):
  def __init__(self, j):
    self.__dict__ = json.loads(j)

def getVersion():
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
    
def startServer():
    global controlServer, serialServer
    # Port 0 means to select an arbitrary unused port

    if (controlServer ==  None):
      ##### control server begin ####
      controlServer = ThreadedTCPServer(("localhost", controlPort), ThreadedTCPControlHandler)
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
      serialServer = ThreadedTCPServer(("localhost", serialPort), ThreadedTCPControlHandler)
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

    
class ThreadedTCPControlHandler(socketserver.BaseRequestHandler):

    def handle(self):
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
                
                controlMsg = json.loads(self.request.recv(1024).decode().strip())
                
                print("recv msg ", controlMsg)
                
                #### command processing begin ####
                command = controlMsg["method"] + "("
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
                
                print ("command " , command)
                
                # eval(command)
                #### command processing end ####
            
            except Exception as e:             
                print ("Error receiving message: ", e)
                #run_main_loop = False
                listening = False
        
        print("buffer ", buffer)
        if (buffer == "stopServer"):
            stopServer()
        

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
 

