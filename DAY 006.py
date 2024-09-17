# Day 6 of 100 Days of Coding with Python

# Working with function

def greetings():
    print("Hello")
    print("World")

greetings()

# Alone: Create a function to Control the Robot to draw a square at
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Alone&url=worlds%2Ftutorial_en%2Falone.json
def turn_right():
    turn_left()
    turn_left()
    turn_left()

turn_left()
move()
turn_right()
move()
turn_right()
move()
turn_right()
move()
# Above functions only works at the specified url


# Huddles 1. Create a function to Control the Robot to complete a huddle race at
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json
def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

# Option 1
jump()
jump()
jump()
jump()
jump()
jump()

# option 2
for step in range(6):
    jump()
# Above functions only works at the specified url
# Huddles 2
# Working with While loop: Reeborg has entered a hurdle race, but he does not know in advance how long the race is.
# Make him run the course, following a path similar to the one shown, but stopping at the only flag that will be
# shown after the race has started.
def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():
    jump()

# more on while loop huddles 3
def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():
    if front_is_clear():
        move()
    else:
        jump()

# Above functions only works at the specified url

# more on while loop huddles 4
def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()


while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()

# Above functions only works at the specified url



