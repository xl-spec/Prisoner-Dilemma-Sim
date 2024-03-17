# This is designed for the intent to convert raw numbers into adverbs for prompting
# will use f-strings to make this work somehow
class Interpret:
    def __init__(self, Obj1, Obj2):
        self.Obj1 = Obj1
        self.Obj2 = Obj2

    def compareMoney(self):
        diff = self.Obj1.money - self.Obj1.money
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