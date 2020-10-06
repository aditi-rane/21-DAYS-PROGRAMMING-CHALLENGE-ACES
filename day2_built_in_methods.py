#LIST METHODS

list=["apple","banana","cherry","orange"]
car=["ford","BMW","volvo"]

print(list.index("apple"))
print(list.copy())
print(list.count("orange"))

list.append("orange")
print(list)

list.extend(car)
print(list)

list.insert(1,"grapes")
print(list)

list.pop(5)
print(list)

list.remove("grapes")
print(list)

list.reverse()
print(list)

list.sort()
print(list)

list.clear()
print(list)

#TUPLES METHODS

tuple=("mango","apple","banana","cherry","apple")

print(tuple.count("apple"))
print(tuple.index("cherry"))
print(tuple)


#SETS METHODS

set1={"apple","banana","cherry","melon","mango"}
set2={"google", "microsoft", "apple"}

set1.add("orange")
print(set1)

set1.discard("orange")
print(set1)

set1.pop()
print(set1)

set1.remove("banana")
print(set1)

set3=set1.difference(set2)
print(set3)

set3=set1.intersection(set2)
print(set3)

set3=set1.isdisjoint(set2)
print(set3)

set3=set1.issubset(set2)
print(set3)

set3=set1.issuperset(set2)
print(set3)

set3=set1.symmetric_difference(set2)
print(set3)

set3=set1.union(set2)
print(set3)

#DICTIONARY METHODS

dicti = {  "brand": "Ford","model": "Mustang","year": 1964}
y=0

print(dicti.get("year"))
print(dicti.items())
print(dicti.keys())
print(dicti.values())

dicti.pop("year")
print(dicti)

x = dicti.setdefault("model", "Bronco")
print(x)

dicti = dict.fromkeys(dicti, y)
print(dicti)

