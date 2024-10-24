#Data types, numbers, operations, type conversion, f-strings
#String, Integer, Float, and Boolean are data types
print("Hello"[4])
#The 0 in square brackets indicate the place value of the first letter in the string.
#Remember that programmers start counting from O.
#The method of pulling out a particular element from a string is called subscripting
#You can also use negative numbers. For example, -1 will show the last character of the string. Then we can start counting backwards.
print("Hello"[-4])
#Moving on, when you put numbers within quotes, the program reads it as strings not numbers. For example
print("123" + "456")
#The output of the function above concatenates the values rather than adds it because the program reads them as strings.
#To declare the numbers as integers, we remove the quotation. The numbers in this example are regarded as integers
#Integers = Whole numbers
print(123+456)
#With large integers, you use underscores instead of commas. The computer removes the underscores in the output.
#The essence of adding the underscores in the first place, is for easy understanding for humans
print(123_456_789)
#Next data type, Float = Floating Point Number = Numbers with decimal points like pi
#Finally, Boolean - Only two possible values; True or False. We start them with capital letter.
#you can use the type function to check the data type of any piece of data or variable
print(type(True))
print(type(3.14))
print(type(123))
#type checking = checking data types
#type casting = converting from one data type to another. We can use the builtins function like int(), float()
print(int("123") + int("456"))
#Note that you can make errors when you do type conversions. Like converting "abc" to integer. You'll get value errors
#Exercise for type casting
print("Number of letters in your name: " + str(len(input("Enter your name"))))
#Mathematical operations
#+ = addition, - = subtraction, * = multiplication, / = division,
#Divison output usually gives floating point numbers. It's called implicit type casting. To avoid the floating results, use // instead of /
print(6 / 2)
print(6 // 2)
#The // operator throws away the remainder from the division. So be careful when using for divisions with remainders
#The last operator is ** which refers to the exponent
print(2 ** 3)
#When you have more than one operation on a line of code, there's an order of priority.
#The order is PEMDAS - parenthesis, exponent, multiplication, division, addition, subtraction
#However, multiplication and division are equally important. Python prioritizes the operator most to the left
print(3 * 3 + 3 / 3 - 3)
#Number manipulation
#Flooring a number means removing all decimal places using the int() function
#Rounding a number performs rounding in a traditional mathematical way using the round() function. Example
bmi = 84 / 1.65 ** 2
print(bmi)
print(int(bmi))
print(round(bmi))
#you can use the round function to the input the number of digits you want to round it up/down to
print(round(bmi, 2))

#Assignment operator (+=, -=, *=, /=) - Allows you to accumulate the result of your calculation.
score = 0
score += 1
print(score)

# We use f-strings to mix strings and different data types since we can't concatenate strings and other data types
score = 0
height = 1.8
is_winning = True
print(f"Your score is = {score}, your height is = {height}. You are winning is {is_winning}")
