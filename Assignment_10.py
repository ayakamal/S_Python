# Assignment 10
# 10- Ask the user for his name then confirm that
# he has entered his name (not an empty string/integers).
# then proceed to ask him for his email and print all this data
# - (Note) check if it is a valid email or not

import re
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
name = input("Please Enter your name: ")
while (name == "" or not name.isalpha()):
    print("invalid name")
    name = input("Please Enter your name: ")

email = input("Please Enter your email: ")
while (not re.search(regex,email)):
    print("invalid email")
    email = input("Please Enter your email: ")
print("Your Name is " + name + '\n' + "Your Email is " + email)