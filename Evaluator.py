
class Evaluator:
    def __init__(self) -> None:
        pass


    def compareMoney(self, char1, char2):
        diff = char1.money - char2.money
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