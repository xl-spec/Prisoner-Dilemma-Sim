from Gamestate import Gamestate


runner = Gamestate(-2, -3, 0, -1, 1, 8)
runner.initializeCharacters()
runner.initializeSystem()
runner.printGameState()
while runner.gameOver():
    runner.runOneTurn()
    runner.printGameState()
