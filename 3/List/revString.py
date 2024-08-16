# l = int(input("enter the length of list"))
# n=[]
# for i in range(l):
#   k=input("enter number elements...")

#   n.append(k)
# print(n) 

n=[1,2,3,"python",'apple',5]
print(n)
for z in range(len(n)):
  if type(n[z])==type("ttt"):
    print(n[z][::-1])

