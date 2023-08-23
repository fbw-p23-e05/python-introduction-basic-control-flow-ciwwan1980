# Your task is to write a program which asks the user five times for a number and prints the maximum of those numbers.


max_number = int()
count=0

while count < 5 :
    number = int(input("Enter number please to calculate the sum: "))
    if number > max_number: 
        max_number =  number
    count +=1
print("the Max numbers between all entered :", max_number)