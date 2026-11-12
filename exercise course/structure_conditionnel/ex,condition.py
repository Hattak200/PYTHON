# Write a Python program that takes two numbers as input from the user and prints the larger of the two numbers.
num1 = int(input("Enter first number"))
num2 = int(input("Enter second number"))
if num1 > num2:
    print("First number is greater than second")
elif num1 == num2:
    print("Both are equal")
else:
    print("Second number is greater than first")