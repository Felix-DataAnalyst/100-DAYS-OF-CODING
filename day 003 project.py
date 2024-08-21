# PROJECT FOR DAY THREE - Treasure Island Game

print(
"""
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/_____/[S.Felix]
******************************************************************************* """)
print("""Welcome to Treasure Island.
Your mission is to find the TREASURE.
""")

lev1 = input("""You're at a cross road. Where do you want to go?\nType "left" or "right" --->  """).lower()
if lev1 == "left":
    # Continue in game
    lev2 = input("""You've come to a lake. There is an island in the middle of the lake. 
                \nType "wait" to wait for a boat. or \nType "swim" to swim across --->  """).lower()
    if lev2 == "wait":
        # Continue in game
        lev3 = input("""You arrived at the island unharmed.\nThere is a house with 3 doors. One red, One yellow and One blue.
        \nWhich colour do you choose?   --->  """).lower()
        if lev3 == "red":
            print("You Entered a room full of fire. GAME OVER.")
        elif lev3 == "blue":
            print("You were Eaten by a Beast. GAME OVER")
        elif lev3 == "yellow":
            print("CONGRATULATIONS!!! YOU WIN")
        else:
            print("Fail!!! GAME OVER")
    else:
        print("You were attacked by Sea Monsters. GAME OVER!!!")


else:
    print("No one returns from this Evil forest alive. GAME OVER!!!")




