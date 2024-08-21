# # Day 3 of 100 Days of Coding with Python

print("Welcome to My Python Journey....from crawling to walking to running")

# Control flow with if and conditional operators
water_level = 50
if water_level > 80:
    print("Drain Water")
else:
    print("Continue")

# Working with nested if and multiple nested if
print("Welcome to the rollercoaster!")
height = int(input("What is your height in CM: "))


if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    elif age >= 45 and age <= 55:
        print("Everything is going to be ok. Have a free ride on us!")
    else:
        bill = 12
        print("Adults tickets are $12.")
    want_photo = input("Do you want a photo take? Type Y for yes and N for No. ")
    if want_photo == "y":
        # Add $3 to their bill
        bill += 3

    print(f"Your final bill is ${bill}")
else:
    print("Sorry you have to grow taller before you can ride.")

# # Operator        Meaning
# >                 Greater Than
# <                 Less than
# >=                Greater than or equal to
# <=                Less than or Equal to
# ==                Equal to
# !=                Not equal to

# modulo operator
print(10 % 3)

# write a code to check if number in the input is odd or even
number_check = int(input("What is the number you want to check?  "))
if number_check % 2 == 0:
    print("Even")
else:
    print("Odd")

# Create a pizza order

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("You typed the wrong inputs")

if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your Final Bill is ${bill}.")

# Logical Operator
AND
OR
NOT

