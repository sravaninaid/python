number = int(input("enter the number of which the user wants to print the multiplication table:"))
print("the multiplication table of :",number)
for count in range (1,11):
    print(number,'x',count,'=',number*count)
