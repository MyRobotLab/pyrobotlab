webgui = Runtime.start("webgui","WebGUI")

def callBack(binaryData):
  data = str(binaryData)
  print("callBack was called with data=", data)
  if (data == 'Hello'):
    print('Yay!')
