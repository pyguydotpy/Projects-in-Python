# Length: At least 12 characters
# At least 1 upper case letter, 1 number, and 1 special character
# The program will:
#   - Accept user input for the password
#   - Give feedback based on security criteria 

import re 
#Regular expression, or regex, are patterns use to match character combinations in a given string

password = input("Enter your password: ")
isSecure = True 

if len(password) < 12:
    print("Password should be at least 12 characters")
    isSecure = False

#regex for 1 upper case character
if not re.search(r'[A-Z]', password):
    print("At least 1 upper case letter")
    isSecure = False

#regex for 1 number
if not re.search(r'\d', password):
    print("At least 1 number")
    isSecure = False

#regex for a 1 special character
if not re.search(r'[^A-Za-z0-9]', password):
    print("At least 1 special character")  
    isSecure = False 

if isSecure:
    print("Password meets all criteria for security")
else:
    print("Password is not secure")
