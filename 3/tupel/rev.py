t = input("enter elements...")
m = tuple(i for i in t.split())

print(m)
n=list(m)
m=n[::-1] 
n1=tuple(m)
print(n1)