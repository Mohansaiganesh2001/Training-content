# Working With Dictionaries  

# empty dict 
empty_dict = {}
print(empty_dict)
print(type(empty_dict))

# empty dict 
empty_dict = dict()
print(empty_dict)
print(type(empty_dict))

# dict with numeric data 
# data = {10,20,30,40,50} # this is set, as there are no keys only values 
# print(type(data))

# dict with numeric data 
data = {1:10,2:20,3:30,4:40,5:50}
print(type(data))
print(data)

data = dict({1:10,2:20,3:30,4:40,5:50})
print(data)

# dict with text data 
data = {"course1":"python","course2":"django","course3":"ai"}
print(data)

# dict with mixed data 
data = {1:10,2:20,3:30,"course1":"python","course2":"django","course3":"ai","gpa":3.5,"passed":True}
print(data)

# Accessing Data
data = {1:10,2:20,3:30,4:40,5:50}
print(data)
# first_element = data[0] # KeyError: 0

first_element = data[1] # KeyError: 0
print(first_element)

last_element = data[5]
print(last_element)

# Access Individual Elements -> 10k elements -> below is not efficient 
data = {1:10,2:20,3:30,4:40,5:50}
print(data[1])
print(data[2])
print(data[3])
print(data[4])
print(data[5])

# Applying Loops 
data = {1:10,2:20,3:30,4:40,5:50}
for key in data: # by default we get key 
    print(key)
    
# Applying Loops - values
data = {1:10,2:20,3:30,4:40,5:50}
for key in data: 
    print(data[key])
    
# Applying Operators -> Multiply Each Element with 10 
data = {1:10,2:20,3:30,4:40,5:50}
for key in data: 
    print(data[key] * 10)

# Applying Conditionals -> Give me only even values 
data = {1:10,2:20,3:35,4:45,5:50}
for key in data: 
    if data[key] % 2 == 0:
        print(data[key])

data = {"course1":"python","course2":"django","course3":"ai"}
for course in data: 
    print(data[course].upper())
    
# Duplicates Allowed i.e Values & Order Preserved -> yes
data = {1:10,2:20,3:20,4:40,5:20}
print(data)

# For Duplicate Keys the latest key will be updated in order 
data = {1:10,2:20,1:20,2:40,5:20}
print(data)

# dict are Mutable 
data = {1:10,2:20,3:20,4:40,5:20}
data[1] = 100
print(data)

# real world dictionary (JSON Data Representation)
# https://d33wubrfki0l68.cloudfront.net/0e4bef351d9e23cdb33adba9e491f73db3c9c50c/7dcfe/data.png
# https://media.licdn.com/dms/image/v2/D4D12AQGwOUMYbhUu-A/article-cover_image-shrink_720_1280/article-cover_image-shrink_720_1280/0/1682148646113?e=2147483647&v=beta&t=qeCSY5Ktzx2jkeq7suYaSBV_-OS_18P-yuabrIhNWcU

students = {
    "101": {
        "name":"Ravi",
        "email":"ravi2krishna@gmail.com",
        "courses": ['python','django','ai'],
        "courses_price": (10000,8000,25000)
    },
    "102": {
        "name":"John",
        "email":"john@gmail.com",
        "courses": ['java','spring','devops'],
        "courses_price": (10000,15000,25000)
    }
}

print(students)
print(type(students))

print("Only Student 101 We need")
print(students["101"])

print("Only Student 101 Name We need")
print(students["101"]['name'])

print("Only Student 101 First Course Name & Price We need")
print(students["101"]['courses'][0],students["101"]['courses_price'][0])

# dict methods / operations 
# print(dir(data))
# help(data)