class Character:
    def __init__(self, id, money, won, loss, yTie, nTie):
        self.id = id
        self.message_list = []
        self.money = money
        self.won = won
        self.loss = loss
        self.yTie = yTie 
        self.nTie = nTie
        self.curRes = ""
        self.resHistory = []