# Looping Structures / Statements

# "while" loop

while False:
    print("Repeat")

# while True: # infinite loop formed 
#     print("Repeat")

count = 1
while count <= 5:
    print("Count: ",count)
    count+=1
    
# You Found a lost phone, trying to break passcode 
# At What attempt, you will get it unlocked ?
actual_passcode = "7867"
user_given_passcode = ""

while user_given_passcode != actual_passcode:
    user_given_passcode = input("Enter PIN: ")
print("Phone Unlocked")

# For Loop With Sequence 
list_of_numbers = [10,20,30,40,50,60,70,80,90,100]
print(list_of_numbers)

# For loop executes a block of code once for each item in the sequence. 
for variable in list_of_numbers:
    print(variable)
    
for num in list_of_numbers:
    print(num * 5)

# with out for 
print("Hi")

# Now say Hi for 50 Times 
print("Hi")
print("Hi")
print("Hi")
print("Hi")
print("Hi")
print("Hi")
print("Hi")
print("Hi")
print("Hi")
print("Hi")
print("Hi")
print("Hi")
print("Hi")
print("Hi")
print("Hi")
print("Hi")
print("Hi")
print("Hi")
print("Hi")
print("Hi")
print("Hi")
print("Hi")
print("Hi")
print("Hi")
print("Hi")
print("Hi")
print("Hi")
print("Hi")
print("Hi")
print("Hi")
print("Hi")
print("Hi")
print("Hi")
print("Hi")
print("Hi")
print("Hi")
print("Hi")
print("Hi")
print("Hi")
print("Hi")
print("Hi")
print("Hi")
print("Hi")
print("Hi")
print("Hi")
print("Hi")
print("Hi")
print("Hi")
print("Hi")
print("Hi")
print("Hi")
print("Hi")
print("Hi")
print("Hi")
print("Hi")
print("Hi")
print("Hi")
print("Hi")
print("Hi")
print("Hi")
print("Hi")
print("Hi")
print("Hi")
print("Hi")
print("Hi")
print("Hi")
print("Hi")
print("Hi")
print("Hi")

# range()
for num in range(0,11,1):
    print(num)
    
for num in range(5,11,1):
    print(num)
    
for num in range(5,101,5):
    print(num)

for num in range(10):
    print(num)

for num in range(0,11,-1):
    print(num)
    
for num in range(11,1,-1):
    print(num)

# We use "for" loop generally, when we know number of Iterations in advance 
# Now say Hi for 50 Times 
for num in range(1,51):
    print("Hi ",num)
