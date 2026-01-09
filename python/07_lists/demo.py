# Working With Lists 

# empty list 
empty_list = []
print(empty_list)
print(type(empty_list))

# empty list 
empty_list = list()
print(empty_list)
print(type(empty_list))

# list with numeric data 
data = [10,20,30,40,50]
print(data)

data = list([10,20,30,40,50])
print(data)

# list with text data 
data = ["python","django","ai"]
print(data)

# list with mixed data 
data = [10,20,30,"python","django","ai",3.5,True]
print(data)

# Accessing Data
data = [10,20,30,40,50]
print(data)

first_element = data[0]
print(first_element)

last_element = data[-1]
print(last_element)

# print(data[10]) # IndexError: list index out of range

# Access Range Of Data / Values 
data = [10,20,30,40,50]
print(data[0:3:1])
print(data[0:5:2])

# Access Individual Elements -> 10k elements -> below is not efficient 
data = [10,20,30,40,50]
print(data[0])
print(data[1])
print(data[2])
print(data[3])
print(data[4])

# Applying Loops 
data = [10,20,30,40,50]
for num in data:
    print(num)
    
# Applying Operators -> Multiply Each Element with 10 
data = [10,20,30,40,50]
for num in data:
    print(num * 10)
    
# Applying Conditionals -> Give me only even values 
data = [10,20,35,45,50]
for num in data:
    if num % 2 == 0:
        print(num)

# Duplicates Allowed & Order Preserved -> yes
data = [10,20,10,50,50]
print(data)

# list methods / operations 
print(dir(data))
help(data)

# Lists are Mutable 
data = [10,20,10,50,50]
data[0] = 100
print(data)