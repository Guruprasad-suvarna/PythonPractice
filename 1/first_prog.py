inp1=int (input("Enter the first input: "))
inp2=int (input ("Enter the second input: "))
op=str (input ("Enter operation: "))

if op=="+":
  sum=inp1+inp2
  print("output",sum)
  
elif op=="-":
   sub=inp1-inp2
   print("output",sub)
   
elif op=="/":
    if inp2==0:
      print("Invalid Input...")
    div=inp1/inp2
    print("output",div)

elif op=="*":
   mul=inp1*inp2
   print("output",mul)