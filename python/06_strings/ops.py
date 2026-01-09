# String Methods / Operations 

# Simulate Gmail Functionality 
#     RAvi2krISHna -> ravi2krishna@gmail.com

email = input("Enter Your Email ID: ")
format_email = email.strip() # removes white spaces 
format_email = format_email.lower() # convert to lower case 
format_email = format_email + "@gmail.com" # concat
print("Original Email: "+email)
print("Formatted Email: "+format_email)

# Simulate PAN Functionality 
# https://www.pan.utiitsl.com/panonline_ipg/forms/csfPan.html/csfPreForm

pan = input("Enter Your PAN ID: ")
if pan.isalnum() and len(pan) == 10: # isalnum(): checks if text is alpha numeric content 
    print("Given PAN: "+pan)
    print("Formatted PAN: "+pan.upper()) # upper(): converts to upper case
    print("Length Of PAN: ",len(pan))
else:
    print("Invalid PAN ID")
    
# Simulate Phone ISD Scenario 
# https://us1.discourse-cdn.com/flex016/uploads/weweb/original/2X/d/dbe25afb4aeb05640347e2f7c1b7ae532ebb28f2.png

mobile = input("Enter Your Phone Number With ISD Code: ")
if mobile.startswith("+1"): # startswith(): checks if string starts with pattern
    print("Calling US Number - Charged in Dollars")
elif mobile.startswith("+91"):
    print("Calling INDIA Number - Charged in Rupees")
elif mobile.startswith("+33"):
    print("Calling FRANCE Number - Charged in Euros")
else:
    print("Invalid NUmber - Calls Supported Only To USA, INDIA & FRANCE")
    
# Simulate Email Synchronization 
# Source Email -> Destination Email 
# ravi@gmail.com -> krishna@gmail.com (PASS)
# ravi@gmail.com -> krishna@yahoo.com (FAIL)

source_email = input("Enter Source Email ID: ")
destination_email = input("Enter Destination Email ID: ")

if source_email.endswith("@gmail.com") and destination_email.endswith("@gmail.com"):
    print("Email Synchronization Success")
else:
    print("Email Synchronization Failed")
    
# Simulate CSV Data from a file and perform some operations
# id,name,email,age,city,profession
emp_data = "101,john,john@gmail.com,34,new york,developer"

# Requirement: Fetch & Display Employee Name, Employee City & Employee Profession
emp_name = emp_data[1] 
print("Employee Name: "+emp_name)

emp_name = emp_data[4:8] # hardcoded 
print("Employee Name: "+emp_name)

# Above Approach is Hard coded and not Dynamic
# To get it more dynamic we can use split 
# split(): splits the data by space default 
words = "hello hi how are you"
words_extracted = words.split()
print(words_extracted)

emp_data_extracted = emp_data.split(",")
print(emp_data_extracted)

# Requirement: Fetch & Display Employee Name, Employee City & Employee Profession
# ['101', 'john', 'john@gmail.com', '34', 'new york', 'developer']
print("Employee Name: "+emp_data_extracted[1])
print("Employee City: "+emp_data_extracted[-2])
print("Employee Profession: "+emp_data_extracted[-1])

# Simulate Amazon Order Email / SMS Confirmation Template 
order_template = "Dear User, Your order with order_id has been Shipped"
# Dear User, Your order with AMZ-123 has been Shipped
# Dear User, Your order with AMZ-456 has been Shipped
# Dear User, Your order with AMZ-789 has been Shipped
order_ids = "AMZ-123,AMZ-456,AMZ-789"
orders_extracted = order_ids.split(",")
print(orders_extracted)
for amazon_order in orders_extracted:
    user_email_sms = order_template.replace("order_id",amazon_order)
    print(user_email_sms)

