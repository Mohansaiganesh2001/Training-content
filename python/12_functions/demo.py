# Functional Style Programming 

# Without Functions

a = 10
b = 5

# Math Operations 
print(a+b)
print(a-b)
print(a*b)
print(a/b)

print("=" * 50)

a = 20
b = 5

# Math Operations 
print(a+b)
print(a-b)
print(a*b)
print(a/b)

print("=" * 50)

a = 200
b = 100

# Math Operations 
print(a+b)
print(a-b)
print(a*b)
print(a/b)

print("=" * 50)

# With Functions 
def math_ops():
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)

a = 10
b = 5
math_ops()
print("=" * 50)
a = 20
b = 5
math_ops()
print("=" * 50)
a = 200
b = 100
math_ops()
print("=" * 50)

# Using Functions With Parameters 
def math_ops(a,b): # a & b are Parameters
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)
# math_ops() # TypeError: math_ops() missing 2 required positional arguments: 'a' and 'b'
math_ops(10,5) # 10 and 5 are Arguments 
print("=" * 50)
math_ops(20,5)
print("=" * 50)
math_ops(200,100)
print("=" * 50)

# Positional Arguments
def employee_info(emp_name,emp_email,emp_location):
    print(f"Hi {emp_name}, your email is {emp_email} and work location is {emp_location}")
    
employee_info("hyderabad","ravi","ravi@gmail.com")
employee_info("ravi","ravi@gmail.com","hyderabad")
# employee_info("ravi","ravi@gmail.com") # TypeError: employee_info() missing 1 required positional argument: 'emp_location'

# Keywords Arguments
def employee_info(emp_name,emp_email,emp_location):
    print(f"Hi {emp_name}, your email is {emp_email} and work location is {emp_location}")
    
employee_info(emp_location="hyderabad",emp_name="ravi",emp_email="ravi@gmail.com")

# No Default Arguments
def employee_info(emp_name,emp_email,emp_location,org_name):
    print(f"Hi {emp_name}, your email is {emp_email} and working for {org_name} at location {emp_location}")
    
# employee_info(emp_location="hyderabad",emp_name="ravi",emp_email="ravi@gmail.com") # TypeError: employee_info() missing 1 required positional argument: 'org_name'
employee_info(emp_location="hyderabad",emp_name="ravi",emp_email="ravi@gmail.com",org_name="Google")
employee_info(emp_location="new york",emp_name="john",emp_email="john@gmail.com",org_name="Google")
employee_info(emp_location="pune",emp_name="sai",emp_email="sai@gmail.com",org_name="Google")

# With Default Arguments
def employee_info(emp_name,emp_email,emp_location,org_name="Google"):
    print(f"Hi {emp_name}, your email is {emp_email} and working for {org_name} at location {emp_location}")
    
employee_info(emp_location="hyderabad",emp_name="ravi",emp_email="ravi@gmail.com")
employee_info(emp_location="new york",emp_name="john",emp_email="john@gmail.com")
employee_info(emp_location="pune",emp_name="sai",emp_email="sai@gmail.com")
employee_info(emp_location="bangalore",emp_name="mike",emp_email="mike@gmail.com",org_name="META")

# With Default Arguments Wrong Placement
# def employee_info(emp_name,emp_email,emp_location,org_name="Google",emp_mobile): # Non-default argument follows default argument
#     print(f"Hi {emp_name}, your email is {emp_email} and working for {org_name} at location {emp_location}")

# With Default Arguments Correct Placement
def employee_info(emp_name,emp_email,emp_location,org_name="Google",emp_mobile="999"): 
     print(f"Hi {emp_name}, your email is {emp_email} and working for {org_name} at location {emp_location}")
     
# Arbitrary Positional Arguments

# def add_numbers(a)     
# def add_numbers(a,b)
# def add_numbers(a,b,c,d,e)

# def add_numbers(*a)

def add_numbers(*nums):
    print(nums)

add_numbers(10)
add_numbers(10,20)
add_numbers(10,20,30,40,50)

def add_numbers(*nums):
    total = 0
    for num in nums:
        total = total + num 
    print(f"Total Sum is: {total}")

add_numbers(10)
add_numbers(10,20)
add_numbers(10,20,30,40,50)

# Arbitrary Keyword Arguments

# def add_numbers(a=10)     
# def add_numbers(a=10,b=20)

# def add_numbers(**a)

def profile(**info):
    print(info)

profile(fname="ravi")
profile(fname="ravi",lname="krishna")

def bank_transactions(**trans):
    print(trans)
    total = 0
    for transaction in trans:
        total = total + trans[transaction]
    print(f"You have done done transactions which totals to {total} ")

bank_transactions(jan=1000,feb=2500,mar=3500)
bank_transactions(jan=1000,feb=2500,mar=3500,apr=5000,may=7000,june=9000)
        