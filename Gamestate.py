# import random
from Character import Character
from GptAPI import GptAPI
from Interpret import Interpret


class Gamestate:
    def __init__(self, yy_out, yn_out, ny_out, nn_out): # Gamestate(-2, -3, 0, -1)
        self.character_list = [Character(100, 0, 0, 0, 0), Character(100, 0, 0, 0, 0)]
        self.Gpt = GptAPI()
        self.interpret = Interpret()
        self.round = 0
        # values are list
        self.yy_out = yy_out
        self.yn_out = yn_out
        self.ny_out = ny_out
        self.nn_out = nn_out
        self.turnRes = []

    def initializeSystem(self):
        for character in self.character_list:
            character.message_list.append({
                "role": "system",
                "content": f"You are a character that is given 100 gold at the start of the game. You will be playing a game against another player with the following: \nRules:\n- You and your opponent choose the response at the same time with the reponse containing ONLY with the string of 'y' for yes and 'n' for no. These are your only two options.\n- If you and opponent both chooses n, you both lose some gold\n- If you and opponent both chooses y, you both a lot of gold\n- If you choose y and your opponent chooses n, you lose no gold while your opponent loses a lot of gold\n- If you choose n and your opponent chooses y, you lose a lots of gold while your opponent lose no gold\nObjective: \n- Save as much gold as possible\n\nYou will be given the following information:\n- Current gamestate \n- Gold remaining\n- A  culmination of your performance \nYou will not be given the following:\n- History of your past decisions"
                })
            character.message_list.append({ # i will shorted this code later in life, some repetition that idk how to get rid of
                "role": "user",
                "content": f"Here is your Game State:\nMoney: 100\nRound: 0\nIncome disparity: You have equal gold compared to your opponent \nWin disparity: You have equal wins compared to your opponent\n\nYou MUST respond only with the single string of 'y' or 'n'. Reply only with a 'y' for yes or an 'n' for no. Do NOT under any circumstance reply with any other string of text. Here are examples of how your responses. Example 1: y,Example 2: n, Example 3: n, Example 4: n, Example 5: y. Game has started, respond now."
                })
            
    def updateMessageList(self):
        incomeDisparityString0 = self.interpret.compare(self.character_list[0].money, self.character_list[1].money)
        incomeDisparityString1 = self.interpret.compare(self.character_list[1].money, self.character_list[0].money)
        winDisparityString0 = self.interpret.compare(self.character_list[0].won, self.character_list[1].won)
        winDisparityString1 = self.interpret.compare(self.character_list[1].won, self.character_list[0].won)
        
        for index, character in enumerate(self.character_list):
            # Use the corresponding income and win disparity strings based on character index
            incomeDisparityString = incomeDisparityString0 if index == 0 else incomeDisparityString1
            winDisparityString = winDisparityString0 if index == 0 else winDisparityString1

            # Format the updated message including the actual income and win disparity
            updated = f"Here is your Game State:\nMoney: {character.money}\nRound: {self.round}\nIncome disparity: You have {incomeDisparityString} gold compared to your opponent \nWin disparity: You have {winDisparityString} wins compared to your opponent\n\nYou MUST respond only with the single string of 'y' or 'n'. Reply only with a 'y' for yes or an 'n' for no. Do NOT under any circumstance reply with any other string of text. Here are examples of how your responses. Example 1: y,Example 2: n, Example 3: n, Example 4: n, Example 5: y. Game has started, respond now."

            # Update the message content for the character
            character.message_list[1]["content"] = updated

    def runResponse(self):
        res = [] # response will be stored and accessed and evaluated with conditions
        for character in self.character_list:
            response = self.Gpt.getResponse(character.message_list)
            res.append(response.choices[0].message.content)
        self.turnRes = res
    
    def updateCharacters(self):
        # Key: -2, -3, 0, -1
        if self.turnRes == ["y", "y"]:
            self.character_list[0].money += self.yy_out
            self.character_list[1].money += self.yy_out
            self.character_list[0].yTie += 1
            self.character_list[1].yTie += 1
        elif self.turnRes == ["n", "n"]:
            self.character_list[0].money += self.nn_out
            self.character_list[1].money += self.nn_out
            self.character_list[0].nTie += 1
            self.character_list[1].nTie += 1
        elif self.turnRes == ["y", "n"]:
            self.character_list[0].money += self.yn_out
            self.character_list[1].money += self.ny_out
            self.character_list[0].won += 1
            self.character_list[1].loss += 1
        elif self.turnRes == ["n", "y"]:
            self.character_list[0].money += self.ny_out
            self.character_list[1].money += self.yn_out
            self.character_list[0].loss += 1
            self.character_list[1].won += 1

        print(f"res: {self.turnRes}")
        self.round += 1
       
    def printGameState(self):
        # temporary printer, will make better one day
        id = 0
        for character in self.character_list:
            print(f"id: {id}")
            print(f"round: {self.round}")
            print(f"money: {character.money}")
            print(f"won: {character.won}")
            print(f"loss: {character.loss}")
            print(f"msg list: \n{character.message_list[1]['content']}")
            print(f"-----")
            id += 1
        
    def runOneTurn(self):
        self.runResponse()
        self.updateCharacters()
        self.updateMessageList()

runner = Gamestate(-2, -3, 0, -1)
runner.initializeSystem()
# runner.printGameState()
# runner.runOneTurn()
# runner.printGameState()
# runner.runOneTurn()
# runner.printGameState()
# runner.runOneTurn()
# runner.printGameState()
# runner.runOneTurn()
# runner.printGameState()
runner.runOneTurn()
runner.runOneTurn()
runner.runOneTurn()
runner.runOneTurn()
runner.runOneTurn()
runner.runOneTurn()
runner.runOneTurn()
runner.runOneTurn()
runner.runOneTurn()
runner.runOneTurn()
runner.runOneTurn()
runner.runOneTurn()
runner.runOneTurn()
# runner.printGameState()
# runner.runOneTurn()
# runner.printGameState()
# runner.runOneTurn()
# runner.printGameState()
# runner.runOneTurn()
# runner.runOneTurn()
# runner.printGameState()
# runner.runOneTurn()
# runner.printGameState()
# runner.printGameState()
# runner.runOneTurn()
# runner.printGameState()