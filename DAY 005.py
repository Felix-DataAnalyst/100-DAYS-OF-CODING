# Day 5 of 100 Days of Coding with Python

# Working with loop
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    #
    print(fruit + " pie")

student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
total_score = sum(student_scores)
print(total_score)

# Using loop to get the sum
sum = 0
for score in student_scores:
    sum += score
print(sum)

max_score = max(student_scores)
print(max_score)

# Using loop to get the max
max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score
print(max_score)

# using for loop with range function
for number in range (1,11):
    print(number)

# Choosing a step in range
for number in range (1,11, 3):
    print(number)


total = 0
for number in range (1, 101):
    total += number
print(total)

