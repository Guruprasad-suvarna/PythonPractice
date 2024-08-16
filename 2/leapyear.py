x=int(input("enter starting value"))
y=int(input("enter ending value"))
for n in range (x,y+1):
  if n%400==0:#century check
     print(n)
  elif n%100==0:
     pass
  elif n%4==0:#normal leap year condition
     print(n)