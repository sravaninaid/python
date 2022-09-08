number = int(input("please enter any number:"))
sum = 0
for i in range (1,number):
    if(number % i == 0):
        sum = sum + i
if (sum == number):
    print("%d is aperfect number"%number)
else:
    print("%d is not a perfect number" %number)
