#Conditional statements, logical operators, code blocks and scope
#if/else conditional statement
#Comparison operators: >(greater than), <(less than), >=(greater than or equal to), ==(equal to), !=(not equal to)
#Note that one equal sign refers to assignment. While double equal sign refers to equality
#Modulo operator, %. It outputs the remainder of a division. For example, 10 % 3 = 1
number = int(input("Provide any number\n"))
if number % 2 == 0:
    print("Even")
else:
    print("Odd")
#Nested if/else statements. You can have another if/else statement inside the first if condition
print("Welcome to the roller coaster")
height = int(input("What is your height in CM?\n"))
if height >= 120:
    print("You can ride the rollercoaster.")
    age = int(input("What is your age?\n"))
    if age <= 12:
        bill = 5
        print("Children tickets cost $5 each")
    elif age <= 18:
        bill = 7
        print("Teens ticket cost $7")
    elif age >= 45 and age >= 55:
        print("Everything is going to be okay. Ride for free.")
    else:
        bill = 12
        print("Adult ticket cost $12")
    photos = input("Do you want photos on your ride?\nInput 'Y' for yes and 'N' for No.\n")
    if photos == "Y":
        bill += 3
    print(f"Your total bill is ${bill}")
else:
    print("Sorry, you have to grow taller before you can ride.")
#elif condition serves as an intermediary when you have several conditions. You can use as many elif as you like.
#Multiple if conditions
print("Welcome to Python Pizza Deliveries!")
bill = 0
size = input("What size of pizza do you want? S, M, or L?\n")
pepperoni = input("Do you want pepperoni on your pizza? Y or N?\n")
cheese = input("Want some extra cheese? Y or N?\n")
if size == "S":
    bill = 15
elif size == "M":
    bill = 20
elif size == "L":
    bill = 25
else:
    print("You typed the wrong input")
if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
if cheese == "Y":
    bill += 1
print(f"Your final bill is ${bill}.")
#Logical operators; And, or, not



