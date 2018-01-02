# set some variables with input()
age = input("How old are you? ")
height = input("How tall are you? ")
# make it better, use some escaped chraacters in there and some f strings!
weight = input(f"So you're:\n{age} old\n{height} tall\nHow much do you weigh? ")

# print this summary string with an f string
print(f"So, you're {age} old, {height} tall and {weight} heavy.")

# test ou why (print("How old are you?" , input ()) doesn't work
# ohhhh, python wants you to set the input before it prints the question!!!
print(">>>>>>")
print("How old are you" , input())
