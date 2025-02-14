a=0
b=1
n=int(input("enter the number:"))
for i in range(5,n+1):
    print(a)
    a,b=b,a+b
