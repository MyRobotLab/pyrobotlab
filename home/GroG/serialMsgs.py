##################################
# Basic script to show how serial callbacks can
# be used to create messages
#
virtual = Runtime.start('virtual','VirtualDevice')
virtual.createVirtualSerial('COM77')
serial = Runtime.start('serial','Serial')
serial.connect('COM77')

serial.addByteListener('python')

serdata = ''
method = '';

def pings():
  global method
  method = 'ping'
  serial.write("P\r")

def onConnect(portName):
  print('connected', portName)

def onDisconnect(portName):
  print('disconnected', portName)


def onByte(data):
  global serdata, method
  c = chr(data)
  serdata += c
  print('['+ serdata + ']')
  if(c == 'X'):
    print('got message ', method, serdata)
    serdata = ''
