# Day 4 of 100 Days of Coding with Python

# working with random numbers
import random

random_integer = random.randint(1, 10)
print(random_integer)

random_float_number = random.random() * 10
print(random_float_number)

random_float = random.uniform(1, 10)
print(random_float)

# Create a coin flip program
rand_heads_tails = random.randint(0,1)
if rand_heads_tails == 0:
    print("Heads")
else:
    print("Tails")

# LIST
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland",
                     "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island",
                     "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois",
                     "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin",
                     "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado",
                     "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma",
                     "New Mexico", "Arizona", "Alaska", "Hawaii"]

continents = ["Asia", "Africa",]
print(continents)

# adding list to an existing list
continents.extend(["North America", "South America", "Antarctica", "Europe", "Australia"])
print(continents)

dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]
print(dirty_dozen)

# popping from a list
dirty_dozen.pop(0)
print(dirty_dozen)

# Nested list
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", ]
vegetables = ["spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

nested_list = [fruits, vegetables]
print(nested_list)

# Option
nested_list2 = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", ["spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]]
print(nested_list2)

# Printing from one of the list in a nested list
print(nested_list[1][1])

# Create a fun program that randomly suggest 'who will pay the bill'

friends = ['Alice', 'Bob', 'Charlie', 'David', 'Emmanuel']

# option 1

print(random.choice(friends) + " "+"Will pay the bill")


#option 2

random_friends = random.randint(1, 4)
if random_friends == 1:
    print(friends[0] + " "+"Will pay the bill")
elif random_friends == 2:
    print(friends[1] + " "+"Will pay the bill")
elif random_friends == 3:
    print(friends[2] + " "+"Will pay the bill")
elif random_friends == 4:
    print(friends[3] + " "+"Will pay the bill")
else:
    print(friends[4] + " "+"Will pay the bill")

# option 3

random_index = random.randint(0, 4 )
print(friends[random_index] + " "+"Will pay the bill")



