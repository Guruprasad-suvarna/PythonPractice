t = input("enter elements...")
m = tuple(i for i in t.split())
print("tupel",m)
n=list(m)
print("list",n)

l1=int(input("enter the length of list to be added"))
z=[]
for j in range(l1):
  y=(input("enter list elements "))
  z.append(y)
z.insert(0,n)
m=tuple(z) 
print(m)





  

