# Assignment 5
# 5- Consider dividing a string into two halves.
# Case 1: The length is even, the front and back halves are the same length.
# Case 2:The length is odd, we'll say that the extra char goes in the front half.
# e.g. 'abcde', the front half is 'abc', the back half 'de'.
# Given 2 strings, a and b, return a string of the form :
# (a-front + b-front) + (a-back + b-back)

def string_divider(str1,str2):

    lenlist = [len(str1),len(str2)]
    list = [str1,str2]
    new_list = []

    for x in range(2):
        if (lenlist[x] % 2 ==0):
            s1 = list[x][:lenlist[x]//2]
            s2 = list[x][lenlist[x]//2:]
            # print(s1,s2)
            new_list.append(s1)
            new_list.append(s2)

        else:
            s1 = list[x][:((lenlist[x] // 2)+1)]
            s2 = list[x][((lenlist[x] // 2)+1):]
            # print(s1, s2)
            new_list.append(s1)
            new_list.append(s2)
    # print(new_list)
    print(new_list[0]+new_list[2]+" "+new_list[1]+new_list[3])


a = 'even'
b = 'odd'
divider = string_divider(a,b)