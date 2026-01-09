# List Methods / Operations 

# append(): add elements to end of list 
data = [10,20,30,40,50]
print(data)
data.append(60)
print(data)

# extend(): add iterable to end of list 
data = [10,20,30,40,50]
print(data)
data.extend([60,70,80,90,100])
print(data)

# insert(): insert element at specific position (index)
data = [10,20,40,50]
print(data)
data.insert(2,30)
print(data)

# pop(): remove element, by default last element
# if index is provided, removes the index element
data = [10,20,30,40,50]
print(data)
data.pop()
print(data)

data = [10,20,30,40,50]
print(data)
data.pop(2)
print(data)

# remove(): remove element based on value 
data = [10,20,30,40,50]
print(data)
data.remove(20)
print(data)

# clear(): removes all values and empties the list 
data = [10,20,30,40,50]
print(data)
data.clear()
print(data)

# index(): used to get the index position
data = [10,20,30,40,50]
print(data)
print(data.index(30))

# count(): used to count the occurrences
data = [10,20,10,10,50]
print(data)
print(data.count(10))

# reverse(): reverses the list 
data = [10,20,30,40,50]
print(data)
data.reverse()
print(data)

# sort(): sorts the list, default is ascending order
data = [10,50,30,40,20]
print(data)
data.sort()
print(data)

data = [10,50,30,40,20]
print(data)
data.sort(reverse=True) # descending order
print(data)

# copy(): creates a backup copy
data = [10,20,30,40,50]
print(data)
backup_list = data.copy()
print(backup_list)