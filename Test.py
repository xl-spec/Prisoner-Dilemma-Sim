# from Gamestate import *
from Character import Character
from Interpret import Interpret
print(f"You are a character that is given 100 gold at the start of the game. You will be playing a game against another player with the following: \nRules:\n- You and your opponent choose the response at the same time with the reponse containing ONLY with the string of 'y' for yes and 'n' for no. These are your only two options.\n- If you and opponent both chooses n, you both lose some gold\n- If you and opponent both chooses y, you both a lot of gold\n- If you choose y and your opponent chooses n, you lose no gold while your opponent loses a lot of gold\n- If you choose n and your opponent chooses y, you lose a lots of gold while your opponent lose no gold\nObjective: \n- Save as much gold as possible\n\nYou will be given the following information:\n- Current gamestate \n- Gold remaining\n- A culmination of your performance \n- You will not be given the history of your past decisions\n\n")

# runner = Gamestate(1, 3, -3, 2) # 
#  yy_out, yn_out, ny_out, nn_out

# character_list = [Character(100, 0, 0, 0, 0), Character(100, 0, 0, 0, 0)]
# character_list[0].money = 0
# character_list[1].money = -120

# interpret = Interpret(character_list[0], character_list[1])
# print(interpret.compareMoney())