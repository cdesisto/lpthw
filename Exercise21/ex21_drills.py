# add a bunch of functions to simulate arithmetic
def add(a, b):
# this print is basically a debug to show you what values are having arithmetic done.
    print(f"ADDING {a} + {b}")
# puts the value of a + b into the function output so it can be stored
    return a + b

def subtract(a, b):
# this print is basically a debug to show you what values are having arithmetic done.
    print(f"SUBTRACTING {a} - {b}")
# puts the value of a - b into the function output so it can be stored
    return a - b

def multiply(a, b):
# this print is basically a debug to show you what values are having arithmetic done.
    print(f"MULTIPLYING {a} * {b}")
# puts the value of a * b into the function output so it can be stored
    return a * b

def divide(a, b):
# this print is basically a debug to show you what values are having arithmetic done.
    print(f"DIVIDING {a} / {b}")
# puts the value of a / b into the function output so it can be stored
    return a / b

# just a string
print("Let's do some math with just functions!")

# let's set some variables using functions!
# this will also do the print part of the functions and put the value into the variable
age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

# print a string with the variables above - values come from the functions that make them
print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

# A puzzle for the extra credit, type it in anyway.
print("Here is a puzzle.")

# do some pemdas
# it's going to do the print part of each function in order while doing arithmetic based on the values above
what = add(age, subtract(height, multiply(weight, divide(iq,2))))

# print out a string with the value of What
# this can all be done "by hand" one line at a time in terminal within python
print("That becomes: ", what, "Can you do it by hand?")
