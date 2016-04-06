chessgame = Runtime.start("chessgame","ChessGame")
# wait 6 seconds for the game to start
sleep(6)

# subscribes to the game engines move method
python.subscribe(chessgame, "makeHMove")

print("game has started !")

# moves pawn from b2 to b3
chessgame.move("b2-b3")

# prints out all moves
def onMakeHMove(move):
  print('move is ', move)
