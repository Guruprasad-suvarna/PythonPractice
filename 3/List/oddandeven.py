l = int(input("enter the length of list1"))
list1=[]
evnlst=[]
oddlst=[]
for i in range(l):
  k=float(input("enter number elements..."))

  list1.append(k)
print(list1) 

for i in range(len(list1)):

   
     if list1[i]%2==0:
        evnlst.append(list1[i])
     else:
        oddlst.append(list1[i])
print(evnlst)
print(oddlst)




# lst1=[1,2,3,4.6,5.5,5.6]
# evnlst=[]
# oddlst=[]
# for i in range(len(lst1)):

   
#      if lst1[i]%2==0:
#         evnlst.append(lst1[i])
#      else:
#         oddlst.append(lst1[i])
# print(evnlst)
# print(oddlst)

    
    