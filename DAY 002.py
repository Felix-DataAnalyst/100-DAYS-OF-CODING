# Day 2 of 100 Days of Coding with Python

print("Welcome to My Python Journey....from crawling to walking to running")

# DATA TYPES & TYPE CHECKING
print(type("hello")) #String
print(type(1234567890)) #Interger
print(type(50.1)) #Float
print(type(True)) #Boolean


#String Indexing & Slicing
print(len("Hello World"))
print("Hello World"[0])
print("Hello World"[1])
print("Hello World"[2])
print("Hello World"[3])
print("Hello World"[4])
print("Hello World"[5])
print("Hello World"[6])
print("Hello World"[7])
print("Hello World"[8])
print("Hello World"[8])
print("Hello World"[9])
print("Hello World"[10])

# interger - Whole number
print(2345+23)
print(1_234_567_890)

#TYPE CASTING
int()
str()
float()
bool()

print("123" + "456") # Would be treated as a string and no mathematical operation would take place.
print(int("123") + int("456")) # Would be treated as an Interger and hence mathematical operation would take place.

# print("Number of letters in your name: " + len(input("Enter Your Name"))) make this line of code run without errors!
name_of_user = input("Enter Your Name")
lenght_of_name = len(name_of_user )
print(type(name_of_user))
print(type(lenght_of_name))
# The line of code below solves the error
print("Number of letters in your name: " + str(lenght_of_name))

# Mathematical operators
print("My age is: " + str(15))
print(123 + 456)
print(7 - 3)
print(3 * 2)
print(6 / 2)
print(5 // 3)
print(2 ** 3)

# PEMDAS-LR Parenthesis.Exponents.Multiplication/Division.Addition.Subtraction - Left to Right
# ()
# **
# * OR /
# + OR -
print(3 * 3 + 3 / 3 - 3)
# print(3 * (3 + 3 / 3 - 3)

# String Formatting
score = 0
height = 1.8
is_winning = True
print(f"Your score is {score}. Your height is {height} You are winning is {is_winning} ")

# End of practice day two.... Heading to project
