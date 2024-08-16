l = int(input("enter the length of list"))
n=[]
for i in range(l):
  k=int(input("enter number elements..."))
  n.append(k)
print(n) 

for j in range(len(n)):
   for y in range(j+1,len(n)):
     if n[j]==n[y]:
      print(n[j])
     
