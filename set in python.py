thisset = {"apple", "banana", "cherry"}
print(thisset)
print(len(thisset))
print(type(thisset))
thisset.add("orange")
print(thisset)
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)
thisset.remove("banana")
print(thisset)
#join set
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)
