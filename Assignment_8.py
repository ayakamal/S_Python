# Assignment 8
# 8- Write a function which has an input of a string from user
# then it will return the same string reversed.

def reverse_string(str):
    return  str[::-1]

str = input("Enter your string: ")
s = reverse_string(str)
print(s)