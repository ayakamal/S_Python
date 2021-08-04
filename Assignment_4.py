# Assignment 4
# 4- Given a list of numbers, create a function that returns a list
# where all similar adjacent elements have been reduced to a single element.
# So [1, 2, 2, 3, 2] Returns [1, 2, 3].

def nonDuplicates(duplicate_list):

    # set_of_elements = []
    non_duplicates_list =[]
    for x in duplicate_list:
        if x not in non_duplicates_list:
            non_duplicates_list.append(x)
    return non_duplicates_list

dup_list = [1,2,2,3,2,7,7,7,5,2,5,6,6]
non_dup = nonDuplicates(dup_list)
print(non_dup)

