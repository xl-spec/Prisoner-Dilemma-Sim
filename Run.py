from Gamestate import Gamestate
class Run:
    def __init__(self) -> None:
        pass

    def gameOver(self):
        pass
runner = Gamestate(-2, -3, 0, -1, 1, 8, 2)
runner.initializeCharacters()
runner.initializeSystem()
runner.printGameState()
while runner.gameOver():
    runner.runOneTurn()
    runner.printGameState()
