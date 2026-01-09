# Operators

# Arithmetic Operators - "Mathematical Calculations"

num1 = 10
num2 = 5

print("Sum Of Numbers", num1 + num2)
print("Difference Of Numbers", num1 - num2)
print("Product Of Numbers", num1 * num2)
print("Division Of Numbers", num1 / num2)
print("Modulus Of Numbers", num1 % num2) 

print("Floor Division", num1 // num2) 
print("Floor Division", 3 // 2) 
print("Exponentiation", 3 ** 2) # 3 ^ 2 

# Compound Assignment Operators
num = 10
num = num + 5 
print(num)

num = 10
num += 5 
print(num)

num = 10
num *= 5 
print(num)

# Increment & Decrement Operators
count = 1
count += 1
print(count)

count = 1
count -= 1
print(count)

# Comparison Operators: Comparing Values
num1 = 5
num2 = 2

print(num1 == num2) # F
print(num1 != num2) # T
print(num1 > num2) # T
print(num1 < num2) # F

print("==================")

# Logical Operators: check "multiple" conditions
num1 = 5
num2 = 2
num3 = 1
num4 = 4

print(num1 > num2 and num3 > num4) # T and F -> F
print(num1 > num2 and num3 < num4) # T and T -> T

print(num1 > num2 or num3 > num4) # T or F -> T
print(num1 < num2 or num3 > num4) # F or F -> F

print(num1 > num2) # T
print(not num1 > num2) # F

print("==================")

# Membership Operators: checking if an object in in the given sequence 
line = "python is programming language"
search_word_in_line = "python"
search_status = search_word_in_line in line
print(search_status)

search_word_in_line = "java"
search_status = search_word_in_line in line
print(search_status)

search_word_in_line = "java"
search_status = search_word_in_line not in line
print(search_status)

print("==================")

# Identity Operators: checking if both objects are same 
n1 = 10
n2 = 5
n3 = 10

print(n1 is n2)
print(n1 is n3)
print(n1 is n3)
print(n1 is not n2)

print("==================")

# Bitwise Operators: Used in Low Level Programming
n1 = 5 # 0000000000000101
n2 = 3 # 0000000000000011
       # 0000000000000001
       # 0000000000000111
# & - if both bits are 1, then result is 1
# | - if one the bits is 1, then result is 1
print(n1 & n2) 
print(n1 | n2) 