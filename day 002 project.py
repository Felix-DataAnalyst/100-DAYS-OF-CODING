# PROJECT FOR DAY TWO - Tip Calculator
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill?  $"))
tip = float(input("What % tip would you like to give? 10%, 12%, or 15%?  "))
split = int(input("How many people to split the bill?  "))
subt1 = tip / 100 # Converting to percent
subt2 = bill * subt1 + bill # Bill plus % tip
subt3 = subt2 / split #
total = round(subt3,2)
print(f"Each person should pay: $ {total}")
