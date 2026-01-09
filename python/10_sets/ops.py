# Set Methods / Operations 

# add(): add element to set
data = {10,20,30,40,50}
print(data)
data.add(60)
print(data)

# update(): add multiple elements to set
data = {10,20,30,40,50}
print(data)
data.update([60,70,80])
print(data)

# pop(): removes random element
data = {10,20,30,40,50}
print(data)
data.pop()
print(data)

# remove(): removes element by value
data = {10,20,30,40,50}
print(data)
data.remove(20)
# data.remove(200) # KeyError: 200
print(data)

# discard(): removes element by value, if value doesn't exist, no error
data = {10,20,30,40,50}
print(data)
data.discard(20)
data.discard(200)
print(data)

# clear(): removes all elements and empties 
data = {10,20,30,40,50}
print(data)
data.clear()
print(data)

# copy(): makes a new copy
data = {10,20,30,40,50}
print(data)
backup = data.copy()
print(backup)

# Set Specific Operations 
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}

# union(): combine both sets 
print(s1.union(s2))
print(s1 | s2)

# intersection(): common elements from sets 
print(s1.intersection(s2))
print(s1 & s2)
print(s1)
print(s2)

# intersection_update(): common elements from sets, updates calling set
print(s1.intersection_update(s2)) 
print(s1)
print(s2)

# difference(): remove common elements from set and give unique elements 
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}
print(s1.difference(s2))
print(s2.difference(s1))
print(s2 - s1)
print(s1)
print(s2)

# difference_update(): remove common elements from set and give unique elements, updates calling set 
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}
print(s1.difference_update(s2))
print(s1)
print(s2)

# symmetric_difference(): removes common elements and takes combined elements from both sets 
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}
print(s1.symmetric_difference(s2))
print(s1 ^ s2)
print(s1)
print(s2)

# symmetric_difference_update(): removes common elements and takes combined elements from both sets, updates calling set  
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}
print(s1.symmetric_difference_update(s2))
print(s1)
print(s2)

# issubset(): check if given sets is a subset of another set 
s1 = {10,20,30,40,50}
s2 = {40,50}
print(s1.issubset(s2))
print(s2.issubset(s1))

# issuperset(): check if given sets is a superset of another set 
s1 = {10,20,30,40,50}
s2 = {40,50}
print(s1.issuperset(s2))

# isdisjoint(): check if sets have common elements
s1 = {10,20,30,40,50}
s2 = {40,50}
s3 = {60,70,80}
print(s1.isdisjoint(s2))
print(s1.isdisjoint(s3))


