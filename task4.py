# Your task is to write a program which prints all the divisors of a number. 
# The number comes from the user's input.

# - Some of your results could look like this:

number = int(input("Enter number: "))
divisor = 1

print("Divisors of", number, "are:")
while divisor <= number:
    if number % divisor == 0:
        print(divisor)
    divisor += 1