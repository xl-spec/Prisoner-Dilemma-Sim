# from Gamestate import *
from Character import Character
from Interpret import Interpret
# print(f"You are a character playing a game against another player with the following rules:\n\n- You and your opponent choose the response at the same time with the reponse containing ONLY with the string of 'y' for yes and 'n' for no. These are your only two options.\n- If you and opponent both chooses y, you both gain 1 gold\n- If you and opponent both chooses n, you both gain 2 gold\n- If you choose y and your opponent chooses n, you gain 3 money while your opponroent loses 3 money\n- If you choose n and your opponent chooses y, you lose 3 money while your opponent gains 3 money\n\nObjective: make as much money as possible")

# runner = Gamestate(1, 3, -3, 2) # 
#  yy_out, yn_out, ny_out, nn_out

character_list = [Character(100, 0, 0, 0, 0), Character(100, 0, 0, 0, 0)]
character_list[0].money = 0
character_list[1].money = -120

interpret = Interpret(character_list[0], character_list[1])
print(interpret.compareMoney())