# Your task is to write a program which asks the user for a number and prints if it is even and divisible by 3.

number = int(input("Enter a number: "))

if number % 2 == 0 and number % 3 == 0:
    print("The number is even and divisible by 3.")
else:
    print("The number is not both even and divisible by 3.")
