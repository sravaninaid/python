try:
    rows=int(input("Enter the number of rows: "))
    if (rows>0):
        for i in range(1, rows + 1):
            for j in range(1, i + 1):
                print(j/10, end=' ')
            print('')
    else:
        print("Number of rows cannot be zero or negative")
except ValueError:
    print("Enter valid input")
