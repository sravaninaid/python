# python program to print rectangle star pattern

rows = int(input("please enter the total number of rows :"))
columns = int(input("please enter the total number of columns :"))

print("Rectangle star pattern")
for i in range(rows):
    for j in range(columns):
        print('*',end = '')
    print()
