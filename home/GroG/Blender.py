import bge                      #blender game engine
import bpy                      #blender python interface
import math                     #Maths Module
import sys
from os.path import expanduser
import socket
import threading
import socketserver


home = expanduser("~")
print (home)
print (sys.version)
print (sys.path)

bpy.data.objects["Cube"].data.vertices[0].co.x += 1.0

a=0.0
version = "0.9"

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

controlServer = None
controlPort = 8989
serialServer = None
serialPort = 9191
    
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
      print ("Server loop running in thread:", serialThread.name, " port ", serialPort)
      ##### serial server end ####
    else:
        print ("servers already started")

    
class ThreadedTCPControlHandler(socketserver.BaseRequestHandler):

    def handle(self):
        #data = self.request.recv(1024).decode()
        myThread = threading.current_thread()
        #response = "{}: {}".format(myThread.name, data)
        #self.request.sendall(response.encode())
        
        buffer = ''
        listening = True

        while listening:
            try:
                # Try to receive som data
                data = self.request.recv(1024).decode()
                buffer += data
                
                if (data == "q"):
                    response = "{}: {}".format(myThread.name, buffer)
                    self.request.sendall(response.encode())
                    listening = False
                
            #except self.request.error, e:
            except e:
                if e.errno != errno.EWOULDBLOCK:
                    # Error! Print it and tell main loop to stop
                    print ("Error: %r" % e)
                    #run_main_loop = False
                # If e.errno is errno.EWOULDBLOCK, then no more data
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
 

