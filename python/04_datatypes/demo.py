# Data Types

# Numeric Types

data = 10
print(type(data))

data = -10
print(type(data))

data = -10.5
print(type(data))

data = 10.0
print(type(data))

# data = 3 + i5 
print(type(data))

data = 3 + 5j 
print(type(data))

# String Type
data = "good morning"
print(type(data))
data = "a"
print(type(data))
data = ""
print(type(data))

# Boolean Type
data = True
print(type(data))

data = False
print(type(data))

# None Type 
data = None 
print(type(data))

# List Type
data = [10,20,30,40,50]
print(type(data))

# Tuple Type
data = (10,20,30,40,50)
print(type(data))

# Set Type
data = {10,20,30,40,50}
print(type(data))

# Frozenset Type
data = frozenset({10,20,30,40,50})
print(type(data))

# Dictionary Type
data = {"name":"Ravi","age":34,"country":"india"}
print(type(data))

# Custom Data Type 
class Student:
    student_id = 101
    student_name = "Ravi"
    student_gpa = 9.5
    student_passed = True

data = Student() 
print(type(data))

# Type Conversion: Automatic
n1 = 10
n2 = 10.5
sum = n1 + n2
print(sum)
print(type(sum))

# Type Casting: Manual
price = 1200.80
print(price)
print(type(price))

round_off_price = int(price) # Type Casting
print(round_off_price)
print(type(round_off_price))

# Some user in a web page filing form(text box), which has some rating (from data is strings)
rating = "5"
rating = int(rating) # Type Casting
if rating < 5: # TypeError: '<' not supported between instances of 'str' and 'int'
    print("Customer Not Satisfied")
else:
    print("Customer Satisfied")