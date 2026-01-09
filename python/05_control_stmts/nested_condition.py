# Nested Conditions 

# Improvise Voting Application
# Add Identity Check
# Voting App - Dynamic     
age = int(input("Enter Your Age: "))
if age >= 18:
    has_id = input("Do You have ID (yes/no): ")
    if has_id == "yes":
        print("You Can Vote")
    else:
        print("You Cannot Vote Without ID")
else:
    print("You Cannot Vote, Underage")
    