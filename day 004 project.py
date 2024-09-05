# PROJECT FOR DAY FOUR - ROCK PAPER SCISSORS

import random

rock0 = """
    _______
---'   ____)
      (_____)
SirF  (_____)
      (____)
---.__(___)
"""

paper1 = """
    _______
---'   ____)____
          ______)
  SirF    _______)
         _______)
---.__________)
"""

scissors2 = """
    _______
---'   ____)____
SirF      ______)
       __________)
      (____)
---.__(___)
"""
game_img = [rock0, paper1, scissors2]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))
if user_choice == 0:
    print(rock0)
elif user_choice == 1:
    print(paper1)
elif user_choice == 2:
    print(scissors2)
else:
    print("You typed an invalid number, you lose!")

com_choice = random.randint(0, 2)
if com_choice == 0:
    print("Computer Chooses: " + rock0)
elif com_choice == 1:
    print("Computer Chooses: " + paper1)
elif com_choice == 2:
    print("Computer Chooses: " + scissors2)
else:
    print("You typed an invalid number, you lose!")

# Rules
# Rock wins against scissors.
# Scissors win against paper.
# Paper wins against rock.

if com_choice == 0 and user_choice == 0:
    print("It's a Draw")
elif com_choice == 0 and user_choice == 2:
    print("Computer Wins")
elif com_choice == 0 and user_choice == 1:
    print("You Win")
elif com_choice == 1 and user_choice == 0:
    print("Computer Wins")
elif com_choice == 1 and user_choice == 2:
    print("You Win")
elif com_choice == 1 and user_choice == 1:
    print("It's a Draw")
elif com_choice == 2 and user_choice == 0:
    print("You Win")
elif com_choice == 2 and user_choice == 2:
    print("It's a Draw")
elif com_choice == 2 and user_choice == 1:
    print("Computer Wins")

# Option 2

