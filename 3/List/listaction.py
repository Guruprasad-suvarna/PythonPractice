
l = int(input("enter the length of list"))
n=[]
for i in range(l):
  k=int(input("enter number elements..."))
  n.append(k)
print(n)      #list creation


l1=int(input("enter the length of new list"))

for j in range(l1):
  y=int(input("enter new elements to the list"))
  n.append(y)
print(n)     #adding new list


n.remove(1) #removing elements by value
print(n)

n.pop(2)    #removing elements by index
print(n)




#sorting
n.sort()
print(n) #ascending

print(n[::-1]) #descending

#coping list
n2=n.copy()
print("copy...")
print(n2)


