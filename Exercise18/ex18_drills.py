# this one is like your scripts with argv
# the *args tells the function that a parameter containing variables will be used
def print_two(*args):
    # sets the values for args separated by commas
    arg1, arg2 = args
    # f string containing the arg values
    print(f"arg1: {arg1}, arg2: {arg2}")

# ok, that *args is actually pointless, so we can just do This
# pointless because we can call the arguments directly rather than putting them into a parameter
def print_two_again(arg1, arg2):
    # f string containing the arg values
    print(f"arg1: {arg1}, arg2: {arg2}")

# this just takes one argument
# an example that you can do it without having multiple values and commas
def print_one(arg1):
    # f string with arguments
    print(f"arg1: {arg1}")

# this one takes no argruments
# empty parentheses means no arguments
def print_none():
    # doesn't need to be an f string because there are no arguments
    print("I got nothin'.")

# prints each of the Functions
# must put the argument values in parentheses because you need to set the inputs as strings
print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
# no arguments, just empty parentheses
print_none()
