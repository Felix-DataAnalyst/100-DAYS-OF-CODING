# PROJECT FOR DAY FIVE - PASSWORD GENERATOR

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Password Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

password = ""
for char in range (1, nr_letters + 1):
    random_char = random.choice(letters)
    # print(random_char) (Used this line to test how my randomization worked.)
    password += random_char
    # print(password)

for char in range(1, nr_symbols + 1):
    random_symb = random.choice(symbols)
    password += random_symb
    # print(password)

for char in range(1, nr_numbers + 1):
    random_numb = random.choice(numbers)
    password += random_numb
print(password)

# OPTION 2 - a neater code

password2 = ""
for char in range(0, nr_letters):
    password2 += random.choice(letters)
    # print(password2)
    
for char in range(0, nr_symbols):
    password2 += random.choice(symbols)
    # print(password2)
    
for char in range(0, nr_numbers):
    password2 += random.choice(numbers)
print(password2)


# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password_list = []
for char in range(0, nr_letters):
    password_list += random.choice(letters)
    # print(password2)

for char in range(0, nr_symbols):
    password_list += random.choice(symbols)
    # print(password2)

for char in range(0, nr_numbers):
    password_list += random.choice(numbers)
# print(password_list)
random.shuffle(password_list)
# print(password_list)

password_hard = ""
for char in password_list:
    password_hard += char
print(password_hard)
