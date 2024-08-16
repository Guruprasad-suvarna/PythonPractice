
t = input("enter elements...")
m = tuple(i for i in t.split())

print(m) #creation

n=list(m)   #converting tuple to list
#print(n)   

l1=int(input("enter the length of new elements"))

for j in range(l1):
  y=(input("enter new elements "))
  n.append(y)
#print(n)  
m=tuple(n)   #converting back from list to tuple
print("added tupel:",m) 

n=list(m)  
n.pop(2) #deleting element 
m=tuple(n)
print("afterdeleting...",m) 

n=list(m)
n.sort()
m=tuple(n)
print("ascending...",m) #ascending


n=list(m)
m=n[::-1] #descending
n1=tuple(m)
print("descending",n1)

n=list(m)
n2=n.copy()
p=tuple(n2)
print("copy...")
print(p)









