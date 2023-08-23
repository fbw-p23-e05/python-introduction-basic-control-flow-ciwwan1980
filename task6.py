
# Your task is to write a program which asks the user for a number and prints if a number is positive, odd and divisible by 7


number = int(input("Enter a number: "))

if number > 0 and number % 2 == 1 and number % 7 == 0:
    print("The number is positive, odd, and divisible by 7.")
else:
    print("The number doesn't meet all the conditions.")
