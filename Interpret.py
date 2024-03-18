# This is designed for the intent to convert raw numbers into adverbs for prompting
# will use f-strings to make this work somehow
class Interpret:
    def __init__(self):
        pass

    def compare(self, num1, num2):
        relation = self.isMoreLessEqual(num1, num2)
        significance = self.isSignificance(num1, num2)
        
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
            return "a little"