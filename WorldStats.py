class WorldStats:
    def __init__(self, character_list):
        self.character_list = character_list
        self.avgMoney
        self.avgWin
        self.avgLoss

    def getAverages(self):
        money = 0
        win = 0
        loss = 0
        for character in self.character_list:
            money += character.money
            win += character.win
            loss += character.loss

        self.avgMoney = money
        self.avgWin = win
        self.avgLoss = loss

