# Assignment 2
# 2- The program takes a string and remove the vowels character from it then print its new version
# Implementation hint:So, “Mobile” becomes “Mbl”

def vowelRemover(str):
    vowels = ('a', 'A','e', 'E', 'i', 'I', 'o', 'O','u', 'U' )

    for s in str:
        if s in vowels:
            str = str.replace(s, '');

    return str

string = input("Enter your word: ")
str = vowelRemover(string)
print(str)