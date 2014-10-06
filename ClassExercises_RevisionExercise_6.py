# William Craddock
# 06/10/2014
# Class Exercises - Selection Statements - Task 6

number1 = int(input("Please enter a first number: "))
number2 = int(input("Please enter a second number: "))
number3 = int(input("Please enter a third number: "))
if number1 == number2 and number1 == number3:
    print("Your numbers are equal")
elif number1 > number2 and number1 > number3:
    print("The first number is greater than the second number and the third number")
elif number2 > number1 and number2 > number3:
    print("The second number is greater than the first number and the third number")
elif number3 > number1 and number3 > number2:
    print("The third number is greater than the first number and the second number")
