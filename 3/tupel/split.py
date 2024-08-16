
# t = input("enter elements...")
# m = tuple(i for i in t.split())

# print(m)



n=[i+1 for i in range(50)]
arr=[]
for j in range(0,len(n),10):
  arr.append(tuple(n[j:j+10]))
print(tuple(arr))