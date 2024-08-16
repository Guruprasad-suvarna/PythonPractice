
def add(a,b):
   sum=a+b
   print("output is",sum)
   
def sub(a,b):
   sub=a-b
   print("output is",sub)
   
def mul(a,b):
   mul=a*b
   print("output is",mul)
   
def div(a,b):
  try:
    div=a/b
    print("output is",div)
  except: 
    print("invalid input")

   
def mod(a,b):
  try:
    mod=a%b
    print("output is",mod)
  except:
    print("invalid input")

a=int(input("enter the first value.."))
b=int(input("enter the second value.."))
inp=str (input("enter inputs for operations..."))
if inp =="+":
    add(a,b)
elif inp =="-":
    sub(a,b)
elif inp =="*":
    mul(a,b)
elif inp =="/":
      div(a,b)
elif inp =="%":
      mod(a,b)