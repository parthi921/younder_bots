a=[1,2,3,4,5,6,67,21,23,999]

b=[]
b.append(max(a))
a.remove(b[0])
b.append(max(a))
a.remove(b[1])
b.append(max(a))
a.remove(b[2])
print(b)
