# Assignment 3
# 3- The program takes a string and a character and returns a list with all
# the locations that character was found in the given string.
# Implementation hint: String “Google” char ‘o’ Output : [1,2]

def locate(string, char):
    location = []
    for s in range(len(string)):
        if string[s] == char:
            location.append(s)
    return location

string = input("Enter your word:")
char = input("Enter your letter: ")

location = locate(string, char)
print(location)
