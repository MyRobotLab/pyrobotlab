port = "COM15"
chessgame = Runtime.start("chessgame","ChessGame")
arduino = Runtime.start("arduino","Arduino")
arduino.connect(port)

chessgame.addListener("publishMove", "python", "onMove")

xmap = {"a":100,"b":200,"c":300,"d":400,"e":500,"f":600,"g":700,"h":800}
ymap = {"1":100,"2":200,"3":300,"4":400,"5":500,"6":600,"7":700,"8":800}
  
def onMove(move):
  print(move)
  x0 = move[1]
  y0 = move[2]
  x1 = move[3]
  y1 = move[4]
  print("move from", x0, y1, "to", x1, y1)
  print("steppers from ", xmap[x0], ymap[y0], "to", xmap[x1], ymap[y1])
  # xstepper.moveTo(xmap[x0])
  # ystepper.moveTo(ymap[y0])
  # routine to drop claw # grab piece
  # lift piece
  # xstepper.moveTo(xmap[x1])
  # ystepper.moveTo(ymap[y1])
  # lower piece
  # open claw
