# import random
from Character import Character
from GptAPI import GptAPI

class Gamestate:
    def __init__(self, yy_out, yn_out, ny_out, nn_out):
        self.character_list = [Character(100, 0, 0, 0, 0), Character(100, 0, 0, 0, 0)]
        self.Gpt = GptAPI()
        self.round = 0
        # values are list
        self.yy_out = yy_out
        self.yn_out = yn_out
        self.ny_out = ny_out
        self.nn_out = nn_out

    def initializeSystem(self):
        for character in self.character_list:
            character.message_list.append({
                "role": "system",
                "content": f"You are a character playing a game against another player with the following rules:\n\n- You and your opponent chooses the response at the same time with the reponse containing ONLY with the string of 'y' for yes and 'n' for no\n- If you and opponent both chooses y, you both gain {self.yy_out} gold\n- If you and opponent both chooses n, you both gain {self.nn_out} gold\n- If you choose y and your opponent chooses n, you gain {self.yn_out} money while your opponent loses {self.yn_out} money\n- If you choose n and your opponent chooses y, you lose {self.yn_out} money while your opponent gains {self.yn_out} money\n\nObjective: make as much money as possible"
                })
            character.message_list.append({
                "role": "user",
                "content": f"Here is your Game State:\nMoney: 100\nRound: 100\nWon: 0\nLoss: 0\n\nYou MUST respond only with the single string of 'y' or 'n'. Reply only with a 'y' for yes or an 'n' for no. Do NOT under any circumstance reply with any other string of text. Here are examples of how your responses. Example 1: y,Example 2: n, Example 3: n, Example 4: n, Example 5: y. Game has started, respond now."
                })
            
    def updateMessageList(self):
        for character in self.character_list:
            updated = f"Here is the Game State:\nMoney: {character.money}\nRound: {self.round}\nWon: {character.won}\nLoss: {character.loss}\n\nYou MUST respond only with the single string of 'y' or 'n'. Reply only with a 'y' for yes or an 'n' for no. Do NOT under any circumstance reply with any other string of text. Here are examples of how your responses. Example 1: y,Example 2: n, Example 3: n, Example 4: y, Example 5: y. Game has started, respond now."
            character.message_list[1]["content"] = updated

    # for now, it's going to just compare the two object manually
    def runResponse(self):
        res = []
        for character in self.character_list:
            response = self.Gpt.getResponse(character.message_list)
            res.append(response.choices[0].message.content)
        
        if res == ["y", "y"]:
            self.character_list[0].money += self.yy_out
            self.character_list[1].money += self.yy_out
            self.character_list[0].yTie += 1
            self.character_list[1].yTie += 1
        elif res == ["n", "n"]:
            self.character_list[0].money += self.nn_out
            self.character_list[1].money += self.nn_out
            self.character_list[0].nTie += 1
            self.character_list[1].nTie += 1
        elif res == ["y", "n"]:
            self.character_list[0].money += self.yn_out
            self.character_list[1].money -= self.ny_out
            self.character_list[0].won += 1
            self.character_list[1].loss += 1
        elif res == ["n", "y"]:
            self.character_list[0].money -= self.ny_out
            self.character_list[1].money += self.yn_out
            self.character_list[0].loss += 1
            self.character_list[1].won += 1

        print(f"res: {res}")
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
            print(f"-----")
            id += 1
        
    def runOneTurn(self):
        self.runResponse()
        self.updateMessageList()

runner = Gamestate(1, 3, -3, 2)
runner.initializeSystem()
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
# runner.printGameState()
# runner.runOneTurn()
# runner.printGameState()
# runner.runOneTurn()
# runner.printGameState()
# runner.runOneTurn()
# runner.printGameState()
# runner.runOneTurn()
# runner.printGameState()