# This is designed for the intent to convert raw numbers into adverbs for prompting
# will use f-strings to make this work somehow
class Interpret:
    def __init__(self, Obj1, Obj2):
        self.Obj1 = Obj1
        self.Obj2 = Obj2

    def compareMoney(self):
        relation = self.isMoreLessEqual(self.Obj1.money, self.Obj2.money)
        significance = self.isSignificance(self.Obj1.money, self.Obj2.money)
        
        if relation == "equal":
            return "equal"
        else:
            return f"{significance} {relation}"
    
    def isMoreLessEqual(self, num1, num2):
        if num1 < num2:
            return "less"
        elif num1 == num2:
            return "equal"
        elif num1 > num2:
            return "more"
    
    def isSignificance(self, num1, num2):
        diff = abs(num1 - num2)
        if diff > 50:
            return "significantly"
        elif diff > 25:
            return "a lot"
        elif diff > 0:
            return "little bit"