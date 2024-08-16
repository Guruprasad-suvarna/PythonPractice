n=str(input("enter a string\t"))
c=str(input("enter a character\t"))
count=0
for i in range (len(n)):
  if n[i]==c:
    count=count+1
print (count)