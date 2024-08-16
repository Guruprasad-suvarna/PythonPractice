x=int(input("enter starting value"))
y=int(input("enter ending value"))
for n in range (x,y+1):
   if n==2 or n==3:
      print(n)
   elif n==1 or n%2==0 or n%3==0:
      pass
   else:
       print(n)
