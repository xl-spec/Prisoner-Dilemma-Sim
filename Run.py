from Gamestate import Gamestate
import pandas as pd
class Run:
    def __init__(self, yy_out, yn_out, ny_out, nn_out, nMoney, nPlayers, runs):
        self.init_args = (yy_out, yn_out, ny_out, nn_out, nMoney, nPlayers)
        self.runner = Gamestate(*self.init_args)
        self.runs = runs
        self.runsLeft = 0

    def resetGameState(self):
        self.runner = Gamestate(*self.init_args) # initialize to original
        self.runner.reset() # reset the initial values

    def exportGameStatesToCSV(self, filename='Data/game_states'):
        # Convert the list of game states to a pandas DataFrame
        df = pd.DataFrame(self.runner.game_states)
        filename += f"{self.runsLeft}.csv"
        # Export the DataFrame to a CSV file
        print(f"exporting to {filename}")
        df.to_csv(filename, index=False)

    def updateRunsLeft(self):
        self.runsLeft += 1

    def runGame(self):
        while self.gameOver():
            self.runner.initializeCharacters()
            self.runner.initializeSystem()
            self.runner.printGameState()
            while self.runner.roundOver():
                self.runner.updateGamestateCSV()
                self.runner.runOneTurn()
                self.runner.printGameState()
            self.runner.updateGamestateCSV()
            self.updateRunsLeft()
            self.exportGameStatesToCSV()
            self.resetGameState()
            # print("please work lmaooo")
            print("-------")

    def gameOver(self):
        return self.runsLeft < self.runs

# runner = Gamestate(-2, -3, 0, -1, 1, 8, 2)
run_instance = Run(-2, -3, 0, -1, 50, 8, 10)
run_instance.runGame()
# runner.initializeCharacters()
# runner.initializeSystem()
# runner.printGameState()
# while runner.gameOver():
#     runner.runOneTurn()
#     runner.printGameState()
