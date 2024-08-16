
dict1={}
#l=int(input("enter the number of elements added to dictionaries"))
for i in range(2):
   name=str(input("enter name..."))
   des=str(input("enter designation..."))
   dict1[name]=des
print(dict1)

#print(employee.values())
#print(employee.keys())

# dict1={"name":"apple","desc":"test"}
# print (dict1)
dict1["prajwal"]="dev"
dict1["ajay"]="test"
print(dict1)

dict1.pop("ajay")
print(dict1)
del dict1["prajwal"]
print(dict1)


dict1.update({"prajwal":"test"})
print(dict1)


dict2=dict1.copy()
print("copied",dict2)


