# Your task is to write a program which asks the user three times for a number and prints the sum of those numbers.

# - Some of your results could look like this:

# ```bash
# Enter number: 200
# Enter number: 500
# Enter number: 300
# Sum of the numbers: 1000


total_sum = 0
count=0

while count < 3 :
    number = int(input("Enter number please to calculate the sum: "))
    total_sum += number
    count +=1
print("Sum of the numbers:", total_sum)