r=int(input("enter number of rows"))
c=int(input("enter number of coloumn"))
arr=[]
for i in range(r):
    arr1=[]
    for j in range(c):
      n=int(input("enter elements"))
      arr1.append(n)
    arr.append(arr1)

r1=int(input("enter number of rows"))
c2=int(input("enter number of coloumn"))
arr2=[]
for k in range(r1):
    arr3=[]
    for l in range(c2):
      n1=int(input("enter elements"))
      arr3.append(n1)
    arr2.append(arr3)

if r==r1 and c==c2:
  finalArr=[]
  for y in range(len(arr)):
    arr5=[]
    for z in range(len(arr[0])):#coloumn length of array
      sum=arr[y][z]+arr2[y][z]
      arr5.append(sum)
      finalArr.append(arr5)
  print(finalArr)
else:
    print("orders are not same of matrix")    



    




