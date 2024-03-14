class Character:
    def __init__(self, money, won, loss, yTie, nTie):
        self.message_list = []
        self.money = money
        self.won = won
        self.loss = loss
        self.yTie = yTie 
        self.nTie = nTie

    def compareMoney(self, Ops):
        diff = self.money - Ops.money
        if diff < 50:
            return "significantly less"
        elif diff < 25:
            return "a lot less"
        elif diff < 0:
            return "little bit less"
        elif diff == 0:
            return "equal"
        elif diff > 0:
            return "little bit more"
        elif diff > 25:
            return "a lot more"
        elif diff > 50:
            return "significantly more"