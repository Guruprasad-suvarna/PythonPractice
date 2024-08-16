Dict1 = {'raju': 100, 'raj': 60,'sam': 80, 'arun': 20, 'john': 90}

Keys1 = list(Dict1.keys())
print(Keys1)
Keys1.sort()
print(Keys1)
sorteddict = {i: Dict1[i] for i in Keys1}

print(sorteddict)
