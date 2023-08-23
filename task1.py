
count = 0
# maximum iteration will be 3 times, starting 0,1,2 and then stop at 3 since count < 3

while count < 3:
    number = int(input("Enter number: "))
    if number % 2 == 0:
        print("Even number")
    else:
        print("Odd number")
    count += 1

    