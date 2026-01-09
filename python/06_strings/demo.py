# Strings 

# Single Line Strings ('' or "")
s1 = 'hello'
print(s1)

s2 = "hello"
print(s2)

s3 = '''hello''' # not recommended for single line strings 
print(s3)

s4 = """hello""" # not recommended for single line strings 
print(s4)

# Define Multi Line Strings 
# define_python = "Python is a high-level, general-purpose programming language. 
#         Its design philosophy emphasizes code readability with the use of 
#         significant indentation. Python is dynamically type-checked and garbage-collected"

# print(define_python)

define_python = ''' Python is a high-level, general-purpose programming language. 
        Its design philosophy emphasizes code readability with the use of 
        significant indentation. Python is dynamically type-checked and garbage-collected ''' 
print(define_python)

define_python = """ Python is a high-level, general-purpose programming language. 
        Its design philosophy emphasizes code readability with the use of 
        significant indentation. Python is dynamically type-checked and garbage-collected """
print(define_python)

# single quote in a string, enclose them in double quotes
question = "How are You ?"
# answer = 'i'm fine'
answer = "i'm fine"
print(answer)

# double quote in a string, enclose them in single quotes 
question = "How are You ?"
# answer = "i"m fine"
answer = 'i"m fine'
print(answer)

# both single quote and double quote in a string, enclose them in triple quotes 
question = "How are You ?"
# answer = 'i"m fine i'm fine '
answer = ''' i"m fine i'm fine '''
print(answer)
answer = """ i"m fine i'm fine """
print(answer)

# Accessing Strings 
text = "python"
print(text)

# Accessing Characters In Strings Using Index 
# Positive Indexing
print(text[0])
print(text[1])
print(text[2])

# Negative Indexing
print(text[-1])
print(text[-2])

text = "python"
print(text[0])
# print(text[10]) # IndexError: string index out of range

# Access All Characters in text 
print(text[0])
print(text[1])
print(text[2])
print(text[3])
print(text[4])
print(text[5])

# Access All Characters in text 
text = "pythonpythonpythonpythonpythonpythonpythonpython"
for char in text:
    print(char)
    
# len() -> used to check the length of string 
print("Length Of String: ",len(text))
text = " ravi"
print("Length Of String: ",len(text))

# Slicing -> string[start:end:step]

text = "python"
print(text[:])
print(text[::])
print(text[0:3:1]) # pyt
print(text[1:3:]) # yt
print(text[0:5:2]) # pto

print(text[-4:-1:1]) # tho  
print(text[-4:-1:-1]) # empty
print(text[-4:-6:-1]) # ty

# String Concatenation 
g = "good"
m = "morning"
print(g+m)

# Formatted String Literals (f-strings)
age = 30
# print("My Age is "+age) # TypeError: can only concatenate str (not "int") to str
print(f"My Age is {age}")
print("My Age is ",age)

# String Repetition 
laugh = "HaHa"
print(laugh)

laugh_hard = laugh * 10
print(laugh_hard)

# String Immutability 
greet = "hello"
print(greet)
print(greet[0])
# greet[0] = 'H' # TypeError: 'str' object does not support item assignment
print(greet[0])

greet = list(greet) # List is Mutable, so we can change the data 
print(greet)
print(greet[0])
greet[0] = 'H'
print(greet[0])
