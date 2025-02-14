a=int(input("enter the first number"))
b=int(input("enter the second number"))
c=input("1 is add /2 is sub/3 mul/4 is div :\n enter the number:")

if(c=='1'):
    d=a+b
    print(d)
elif(c=='2'):
    d=a-b
    print(d)
elif(c=='3'):
    d=a*b
    print(d)
elif(c=='4'):
    d=a/b
    print(d)
else:
    print("invalid")
    
