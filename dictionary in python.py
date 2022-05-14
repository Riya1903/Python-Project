thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
print(len(thisdict))
print(type(thisdict))
#add item in dictionary
thisdict["color"] = "red"
print(thisdict)
#remove item in dictionary
thisdict.pop("model")
print(thisdict)
#update dictionary
thisdict.update({"color": "White"})

print(thisdict)
#copy dictionary
mydict = thisdict.copy()
print(mydict)
