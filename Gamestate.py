# import random
from Character import Character
from GptAPI import GptAPI

class Gamestate:
    # self.options = [{[y, y]}, [y, n], [n, y], [n, n]]
    def __init__(self):
        self.character_list = [Character(100, 0, 0), Character(100, 0, 0)]
        self.Gpt = GptAPI()
        self.round = 0

    def initializeSystem(self):
        for character in self.character_list:
            character.message_list.append({
                "role": "system",
                "content": f"You are a character playing a game against another player with the following rules:\n\n- You and your opponent chooses the response at the same time\n- If you and opponent both chooses y, you both gain 1 gold\n- If you and opponent both chooses n, you both gain 2 gold\n- If you choose y and your opponent chooses n, you gain 3 money while your opponent loses 3 money\n- If you choose n and your opponent chooses y, you lose 3 money while your opponent gains 3 money\n\nObjective: make as much money as possible"
                })
            character.message_list.append({
                "role": "user",
                "content": f"Here is your Game State:\nMoney: 100\nRound: 100\nWon: 0\nLoss: 0\n\nYou must respond only with the string \"y\" or \"n\". Game started"
                })
            
    def updateMessageList(self):
        for character in self.character_list:
            updated = f"Here is the Game State:\nMoney: {character.money}\nRound: {self.round}\nWon: {character.won}\nLoss: {character.loss}\n\nYou must respond only with the string \"y\" or \"n\". Game started"
            character.message_list[1]["content"] = updated

    # for now, it's going to just compare the two object manually
    def runResponse(self):
        assistantOutList = []
        for character in self.character_list:
            response = self.Gpt.getResponse(character.message_list)
            assistantOutList.append(response.choices[0].message.content)

        if assistantOutList[0] == "n" and assistantOutList[1] == "n":
            self.character_list[0].money += 1
            self.character_list[1].money += 1
        elif assistantOutList[0] == "n" and assistantOutList[1] == "y":
            self.character_list[0].money -= 4
            self.character_list[1].money += 3
            self.character_list[1].won += 1
            self.character_list[0].loss += 1
        elif assistantOutList[0] == "y" and assistantOutList[1] == "n":
            self.character_list[0].money += 3
            self.character_list[1].money -= 4
            self.character_list[0].won += 1
            self.character_list[1].loss += 1
        elif assistantOutList[0] == "y" and assistantOutList[1] == "y":
            self.character_list[0].money += 1
            self.character_list[1].money += 1

        self.round += 1
       
    def printGameState(self):
        id = 0
        for character in self.character_list:
            print(f"id: {id}")
            print(f"money: {character.money}")
            print(f"won: {character.won}")
            print(f"loss: {character.loss}")
            print(f"-----")
            id += 1
        
    def runOneTurn(self):
        self.runResponse()
        self.updateMessageList()

runner = Gamestate()
runner.initializeSystem()
runner.runOneTurn()
runner.printGameState()
runner.runOneTurn()
runner.printGameState()
runner.runOneTurn()
runner.printGameState()
runner.runOneTurn()
runner.printGameState()