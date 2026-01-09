# Nested For Loop 

# Generate Math Tables 

# 1 X 1 - 1 X 2 - 1 X 3 - 1 X 4 - 1 X 5 ....
# 2 X 1 - 2 X 2 - 2 X 3 - 2 X 4 - 2 X 5 ....
# 3 X 1 - 3 X 2 - 3 X 3 - 3 X 4 - 3 X 5 ....
# 4 X 1 - .....
# 5 X 1 - .....

# Nested for loop 
for outer in range(1,6):
    print("Outer: ", outer)

for inner in range(1,6):
    print("Inner: ", inner)

print("===================")
 
for outer in range(1,6):
    print("Outer: ", outer)
    for inner in range(1,6):
        print("Inner: ", inner)

# Generate Math Tables 
for outer in range(1,6):
   for inner in range(1,6):
        print(f"{outer} X {inner} = {outer * inner}") 

# Real World use Case with ecommerce application 
colors = ["white","yellow","black","red"]
sizes = ["S","M","L","XL"]

for color in colors:
    for size in sizes:
        print(color, size)
        
# Nested While Loop

# 1 X 1 - 1 X 2 - 1 X 3 - 1 X 4 - 1 X 5 ....
# 2 X 1 - 2 X 2 - 2 X 3 - 2 X 4 - 2 X 5 ....
# 3 X 1 - 3 X 2 - 3 X 3 - 3 X 4 - 3 X 5 ....
# 4 X 1 - .....
# 5 X 1 - .....
outer = 1
while outer < 6:
    inner = 1
    while inner < 6:
        print(f"{outer} X {inner} = {outer * inner}") 
        inner += 1
    outer += 1
    