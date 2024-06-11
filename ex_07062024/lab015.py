#Create a program that takes two numbers as input and prints whether the first number is greater than, less than, or equal to the second number.
num1 = float(input("Enter the first Number: "))
num2 = float(input("Enter the second Number: "))
if num1 < num2:
    print("num2 is greater")
elif num1 > num2:
    print("num1 is greater")
else :
    print("Both are equal")