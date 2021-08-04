# Assignment 7
# 7- write a function that takes a number as an argument and
# if the number divisible by 3 return "Fizz" and if it is divisible by 5
# return "buzz" and if it is divisible by both return "FizzBuzz"

def numeric(num):
    if (num % 3 == 0 and num % 5 == 0):
        print("FizzBuzz")
    elif (num % 3 == 0):
        print("Fizz")
    elif (num % 5 == 0):
        print("buzz")
    else:
        print("Number is not divisible by 3 or 5")



num = int(input("Enter your number: "))
numeric(num)