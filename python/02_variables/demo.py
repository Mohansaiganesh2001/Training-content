# Variables 

# Assign Data (Store Data)
student_name = "Ravi" # string 
student_age = 22 # int 
student_gpa = 9.2 # float 
student_passed = True # boolean 

# Retrieve Data (Get Data)
print(student_name)
print(student_age)
print(student_gpa)
print(student_passed)

# Retrieve Data (Get Data), Using Concatenation
print("Student Name Is: " + student_name)
# print("Student Age Is: " + student_age) # TypeError: can only concatenate str (not "int") to str
print("Student Age Is: ", student_age)
print("Student GPA Is: ", student_gpa)
print("Student Passed: ", student_passed)

# Retrieve Data Identity (Get Data Memory Address) -> use id()
print(id(student_name))
print(id(student_age))
print(id(student_gpa))
print(id(student_passed))

print("=========================")

# Python Memory Model With Simple Data Types
value_num1 = 10
print(id(value_num1))

value_num2 = 20
print(id(value_num2))

value_num3 = 10
print(id(value_num3))

print("=========================")

# Python Memory Model With Complex Data Types
value_list1 = [10,20,30]
print(id(value_list1))

value_list2 = [40,50,60]
print(id(value_list2))

value_list3 = [10,20,30]
print(id(value_list3))

print("=========================")

# Retrieve Data Type -> use type()
print(type(student_name))
print(type(student_age))
print(type(student_gpa))
print(type(student_passed))
print(type(value_list3))