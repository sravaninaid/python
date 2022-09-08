# 1-12-123-1234 pattern up to n lines

n = int ( input("enter numbder of rows:"))

for i in range (1,n+1):
    for j in range (1, i+1):
        print(j, end="")
    print()
