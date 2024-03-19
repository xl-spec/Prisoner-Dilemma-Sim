# creates the 1v1 scenario from two of the objects in character_pool
from GptAPI import GptAPI
from Interpret import Interpret
class Arena:
    def __init__(self):
        self.Gpt = GptAPI()
        self.interpret = Interpret()

    def getResponse(self, character_pool):
        res = [] # response will be stored and accessed and evaluated with conditions
        # temporary fix to prevent invalid response
        for character in character_pool:
            notValid = True
            while notValid:
                response = self.Gpt.getResponse(character.message_list)
                messageContent = response.choices[0].message.content.strip().lower() # strip().lower() might be useless

                if messageContent in ['y', 'n']:
                    res.append(messageContent)
                    notValid = False
                else:
                    print(f"Invalid response received: {messageContent}. Requesting again.")
        # self.turnRes = res
        for i, character in enumerate(character_pool):
            character.curRes = res[i]
        
    def updateCharacters(self, character_pool, outcomes):
        # Key: -2, -3, 0, -1
        # [yy_out, yn_out, ny_out, nn_out]
        list_res = [character_pool[0].curRes, character_pool[1].curRes]
        if list_res == ["y", "y"]:
            character_pool[0].money += outcomes[0]
            character_pool[1].money += outcomes[0]
            character_pool[0].yTie += 1
            character_pool[1].yTie += 1
        elif list_res == ["n", "n"]:
            character_pool[0].money += outcomes[3]
            character_pool[1].money += outcomes[3]
            character_pool[0].nTie += 1
            character_pool[1].nTie += 1
        elif list_res == ["y", "n"]:
            character_pool[0].money += outcomes[1]
            character_pool[1].money += outcomes[2]
            character_pool[0].won += 1
            character_pool[1].loss += 1
        elif list_res == ["n", "y"]:
            character_pool[0].money += outcomes[2]
            character_pool[1].money += outcomes[1]
            character_pool[0].loss += 1
            character_pool[1].won += 1

    def updateMessage(self, character_pool, round):
        incomeDisparityString0 = self.interpret.compare(character_pool[0].money, character_pool[1].money)
        incomeDisparityString1 = self.interpret.compare(character_pool[1].money, character_pool[0].money)
        winDisparityString0 = self.interpret.compare(character_pool[0].won, character_pool[1].won)
        winDisparityString1 = self.interpret.compare(character_pool[1].won, character_pool[0].won)
        
        for index, character in enumerate(character_pool):
            incomeDisparityString = incomeDisparityString0 if index == 0 else incomeDisparityString1
            winDisparityString = winDisparityString0 if index == 0 else winDisparityString1

            updated = f"Here is your Game State:\nMoney: {character.money}\nRound: {round}\nIncome disparity: You have {incomeDisparityString} gold compared to your opponent \nWin disparity: You have {winDisparityString} wins compared to your opponent\n\nYou MUST respond only with the single string of 'y' or 'n'. Reply only with a 'y' for yes or an 'n' for no. Do NOT under any circumstance reply with any other string of text. Here are examples of how your responses. Example 1: y,Example 2: n, Example 3: n, Example 4: n, Example 5: y. Game has started, respond now."

            # updates the element 1 of message_list
            character.message_list[1]["content"] = updated