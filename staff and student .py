t=int(input("enter the no of total users :"))
if(t>0):
    s=int(input("enter no of staff users:"))
    print("total  users :",t)
    print("staff users:",s)
else:
    print("no of total users is invalid")
if(t>s):
    n=s/3
    print("no of non teaching staff users:",n)
    res=t-(n+s)
    print("no of student user:",res)
else:
    print("invalid entry")
