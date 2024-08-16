
r=int(input("enter number of rows"))
c=int(input("enter number of coloumn"))
arr=[]
for i in range(r):
    arr1=[]
    for j in range(c):
      n=int(input("enter elements"))
      arr1.append(n)
    arr.append(arr1)
print(arr)


for k in range(len(arr)):
    print(arr[k][k])

  