class WorldStats:
    def __init__(self):
        self.avgMoney = 0
        self.avgWin = 0
        self.avgLoss = 0

    def getAverages(self, character_list):
        money = 0
        win = 0
        loss = 0
        for character in character_list:
            money += character.money
            win += character.won
            loss += character.loss

        self.avgMoney = money
        self.avgWin = win
        self.avgLoss = loss

