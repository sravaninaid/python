n=int(input("enter the num"))
org=n
sum=0
while(n>0):
    a=n%10
    sum=sum*10+a
    n=n//10
    print(a)
