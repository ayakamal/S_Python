# Assignment 6
# 6- Write a function that accepts two arguments (length, start)
# to generate an array of a specific length filled with integer numbers increased by one from start.

def new_array(length, start):
    array = list(range(start, start + length))
    return array


new_length = int(input("Enter array length: "))
new_start = int(input("Enter start number"))
array = new_array(new_length, new_start)
print(array)

