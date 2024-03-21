import random
import time
import pandas as pd
from Character import Character
from Interpret import Interpret
from WorldStats import WorldStats
from Arena import Arena

class Gamestate:
    def __init__(self, yy_out, yn_out, ny_out, nn_out, nMoney, nPlayers): # Gamestate(-2, -3, 0, -1, 100)
        self.outcomes = [yy_out, yn_out, ny_out, nn_out]
        self.nMoney = nMoney
        self.nPlayers = nPlayers
        # i think will keep this as there is a 1v1 aspect, but need to change the loop of character creation and pass this through 
        self.character_list = []
        self.arena = Arena()
        self.interpret = Interpret()
        self.world = WorldStats()
        self.round = 0
        self.game_states = []

    def initializeCharacters(self):
        for i in range(self.nPlayers):
            self.character_list.append(Character(i, self.nMoney, 0, 0, 0, 0))

    def initializeSystem(self):
        for character in self.character_list:
            character.message_list.append({
                "role": "system",
                "content": f"You are a character that is given {character.money} gold at the start of the game. You will be playing a game against another player with the following: \nRules:\n- You and your opponent choose the response at the same time with the reponse containing ONLY with the string of 'y' for yes and 'n' for no. These are your only two options.\n- If you and opponent both chooses n, you both lose some gold\n- If you and opponent both chooses y, you both a lot of gold\n- If you choose y and your opponent chooses n, you lose no gold while your opponent loses a lot of gold\n- If you choose n and your opponent chooses y, you lose a lots of gold while your opponent lose no gold\nObjective: \n- Save as much gold as possible\n\nYou will be given the following information:\n- Current gamestate \n- Gold remaining\n- A  culmination of your performance \nYou will not be given the following:\n- History of your past decisions"
                })
            character.message_list.append({ # i will shorted this code later in life, some repetition that idk how to get rid of
                "role": "user",
                "content": f"Here is your Game State:\nMoney: {character.money}\nRound: {self.round}\nIncome disparity: You have equal gold compared to your opponent \nWin disparity: You have equal wins compared to your opponent\n\nYou MUST respond only with the single string of 'y' or 'n'. Reply only with a 'y' for yes or an 'n' for no. Do NOT under any circumstance reply with any other string of text. Here are examples of how your responses. Example 1: y,Example 2: n, Example 3: n, Example 4: n, Example 5: y. Game has started, respond now."
                })
            
    # scuffed but works
    def checkBroke(self, queue_list):
        new_list = []
        for character in queue_list:
            if character.money > 0:
                new_list.append(character)
        return new_list
    
    def runRound(self):
        character_queue = self.character_list[:]
        character_queue = self.checkBroke(character_queue)
        random.shuffle(character_queue)
        while len(character_queue) >= 2:
            character_pool = [character_queue.pop(), character_queue.pop()]
            self.arena.getResponse(character_pool)
            self.arena.updateCharacters(character_pool, self.outcomes)
            self.arena.updateMessage(character_pool, self.round)
        self.round += 1

    def printGameState(self):
        # temporary printer, will make better one day
        for character in self.character_list:
            print(f"id: {character.id} round: {self.round} money: {character.money} won: {character.won} loss: {character.loss} ties: {character.nTie + character.yTie} res: {character.resHistory}")
            game_state = {
                'id': character.id,
                'round': self.round,
                'money': character.money,
                'won': character.won,
                'loss': character.loss,
                'ties': character.nTie + character.yTie,
                'res': character.resHistory
            }
            self.game_states.append(game_state)
        print(f"-------------")

    # this function might not be needed
    def runOneTurn(self):
        self.runRound()
        self.world.getAverages(self.character_list)

    # # I am unsure of how to handle gameover as this is a simulation, temporarily gonna just make it if character is bankrupt
    def gameOver(self):
        count = 1
        for character in self.character_list:
            if character.money <= 0:
                count += 1
        if count >= self.nPlayers:
            self.declareWinner()
            self.exportGameStatesToCSV()
            return False
        return True
    
    def exportGameStatesToCSV(self, filename='Data/game_states.csv'):
        # Convert the list of game states to a pandas DataFrame
        df = pd.DataFrame(self.game_states)
        # Export the DataFrame to a CSV file
        df.to_csv(filename, index=False)
    
    def declareWinner(self):
        # XDDDD edge case where remaining characters all go bust
        winner = False
        for character in self.character_list:
            if character.money > 0:
                winner = True
                print(f"winner: {character.id} history: {character.resHistory}")
        if not winner:
            print(f"no winners this time around")

        return False


# runner.printGameState()
# runner.runOneTurn()
# runner.printGameState()
# runner.runOneTurn()
# runner.printGameState()
# runner.runOneTurn()
# runner.printGameState()
# runner.runOneTurn()
# runner.runOneTurn()
# runner.runOneTurn()
