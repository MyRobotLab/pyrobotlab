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

server = None
    
def stopServer():
    global server
    print ("stopping server")
    if (server != None):
        server.shutdown()
    else:
        print("server already stopped")
    server = None
    
def startServer():
    global server
    # Port 0 means to select an arbitrary unused port
    HOST, PORT = "localhost", 9090

    if (server ==  None):
        server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)
        ip, port = server.server_address

        # Start a thread with the server -- that thread will then start one
        # more thread for each request
        server_thread = threading.Thread(target=server.serve_forever)
        # Exit the server thread when the main thread terminates
        server_thread.daemon = True
        server_thread.start()
        print ("Server loop running in thread:", server_thread.name)
    else:
        print ("server already started")

    
class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):

    def handle(self):
        #data = self.request.recv(1024).decode()
        cur_thread = threading.current_thread()
        #response = "{}: {}".format(cur_thread.name, data)
        #self.request.sendall(response.encode())
        
        buffer = ''
        continue_recv = True

        while continue_recv:
            try:
                # Try to receive som data
                data = self.request.recv(1024).decode()
                buffer += data
                
                if (data == "q"):
                    response = "{}: {}".format(cur_thread.name, buffer)
                    self.request.sendall(response.encode())
                    continue_recv = False
                
            #except self.request.error, e:
            except e:
                if e.errno != errno.EWOULDBLOCK:
                    # Error! Print it and tell main loop to stop
                    print ("Error: %r" % e)
                    #run_main_loop = False
                # If e.errno is errno.EWOULDBLOCK, then no more data
                continue_recv = False
        
        print("buffer ", buffer)
        

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
 

