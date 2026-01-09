# Working With Sets  

# empty set -> by default when we use empty {}, then it's a dict 
empty_set = {}
print(empty_set)
print(type(empty_set))

# empty set 
empty_set = set()
print(empty_set)
print(type(empty_set))

# set with numeric data 
# data = 10,20,30,40,50 # tuple 
data = {10,20,30,40,50}
print(type(data))
print(data) # order is not preserved 

data = set({10,20,30,40,50})
print(data)

# set with text data 
data = {"python","django","ai"}
print(data)

# set with mixed data 
data = {10,20,30,"python","django","ai",3.5,True}
print(data)

# Accessing Data
data = {10,20,30,40,50}
print(data)
# first_element = data[0] # TypeError: 'set' object is not subscriptable, as no index
# print(first_element)

# Applying Loops 
data = {10,20,30,40,50}
for num in data:
    print(num)

# Applying Operators -> Multiply Each Element with 10 
data = {10,20,30,40,50}
for num in data:
    print(num * 10)
         
# Applying Conditionals -> Give me only even values 
data = {10,20,35,45,50}
for num in data:
    if num % 2 == 0:
        print(num)

# Duplicates Allowed & Order Preserved -> no
data = {10,20,10,50,50}
print(data)

# set methods / operations 
print(dir(data))

# frozenset 
data = frozenset({10,20,10,50,50})
print(data)
print(type(data))

# frozenset methods / operations 
print(dir(data))