a=[ ]
b=int(input("Enter the number of elements: "))
for i in range(b):
    c=int(input("Enter the number: "))
    a.append(c)

M=int(input("Enter the value of M: "))
N=int(input("Enter the value of N: "))
n=N-1
if (M>0):
    def max(a):
        length=len(a)
        a.sort()
        print(M,"th maximum number= ",a[length-M])
    
    Maxi = max(a)

    def min(a):
        length=len(a)
        a.sort()
        print(N,"th minimum number= ",a[n])
        print("Sum =",a[length-M]+a[n])
        print("Diff =",a[length-M]-a[n])
    Mini = min(a)
else:
    print("Enter a natural number")
