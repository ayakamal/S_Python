# Assignment 11
# 11- Write a function that takes a string and prints the longest alphabetical ordered substring occured.
# For example, if the string is 'abdulrahman' then the output is:
# Longest substring in alphabetical order is: abdu

def longest_Alphabet_order(str):
    longest = str[0]
    temp = str[0]
    for x in str[1:]:
        if x >= temp[-1]:
            temp += x
            if len(temp) > len(longest):
                longest = temp
        else:
            temp = x
    print ("The Longest substring in alphabetical order is:", longest)

str = input("Enter Your string: ")
longest_Alphabet_order(str)