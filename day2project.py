print("Welcome to the tip calculator!")
bill = float(input("What was the total bill?\n$"))
tip_percentage = int(input("How much tip would you like to give? 10, 12, or 15?\n"))
tippers = int(input("How many people to split the bill?\n"))
tip = round((tip_percentage / 100 + 1) * bill / tippers, 2)
print(f"Each person should pay: ${tip}")


