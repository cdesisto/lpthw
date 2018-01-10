# add this line
from sys import argv

print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
# set height variable as input
height = input()
# add ) to the end
print("How much do you weigh?", end=' ')
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")

#this line tells me to add 'from sys import argv'
script, filename = argv

# filename was mispelled
txt = open(filename)

print("Here's your file {filename}:")
# txt was mispelled
print(txt.read())

print("Type the filename again:")
## There might be a break here with what's in the parenthesis ater input
file_again = input("> ")

txt_again = open(file_again)

# txta_again_read doesn't exist, _ should be a .
print(txt_again.read())

# using the apostrophe means there should be a double quote or escape the sinlge quote
print("Let's practice everything.)
# I'm guessing Zed things there should be a new line and tab here, so I'll do that
print('You\'d need to know \'bout escapes \n\twith \\ that do \\n newlines and \\t tabs.')

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("--------------)
print(poem)
# need a double quote after print(
print("--------------")

# final number should be 6 to make the equation equal 5
five = 10 - 2 + 3 - 6
# add a parenthesis to the end of the line
print(f"This should be five: {five}")

# add a : to the end of the line
def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
# needs a * to make the math work
    crates = jars * 100
    return jelly_beans, jars, crates

### I think this should be started, not start_point...or does start_point need to be in the function?
start_point = 10000
# left crates off the list
beans, jars, crates = secret_formula(start_point)

# remember that this is another way to format a string
print("With a starting point of: {}".format(start_point))
# it's just like with an f"" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10

print("We can also do that this way:")
formula = secret_formula(startpoint)
# this is an easy way to apply a list to a format string
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))



people = 20
cates = 30
dogs = 15


if people < cats:
    print "Too many cats! The world is doomed!"

if people < cats:
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

if people > dogs
    print("The world is dry!")


dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs
    print("People are less than or equal to dogs.)


if people = dogs:
    print("People are dogs.")
