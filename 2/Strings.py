s="Apple"
print(s)
print(s[0])
print(s[2])
print(s[-1])
print(s[-5])
#print(s[-6]) #error
print(s[::-1])
print(s[1:5])





n="".join(reversed(s))
print(n)




n="python\t"
print(10*n)




n=str(input("enter name\t"))
a=int(input("enter age\t"))
print(f"My name is {n},",f"Im {a} years old")





n=str(input("enter name\t"))
a=int(input("enter age\t"))
e=int(input("enter year of experience\t"))
print(f"My name is {n}\n"f"Im {a} years old\n"f"I have {e} years of experience")