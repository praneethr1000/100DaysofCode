print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
percentage = float(input("What percentage tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))
finalSplit = (bill + (bill*percentage)/100)/people
formated = "{:.2f}".format(finalSplit)
print(f'Each person should pay: ${formated}')