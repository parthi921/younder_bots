def sum_square(n):
    if n==1:
        return 1
    else:
        return n**2 + sum_square(n-1)
n=int(input("enter the number:"))
print(sum_square(n))
