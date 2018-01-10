# a few print statements with some escaped characters
print("Let's practice everything.")
print('You\'d need to know \'bout escapes with \\ that do:')
print('\n newlines and \t tabs.')

# setting the poem variable with a string (poem)
# notice that a variable can start/end with a triple quote like in a print function
poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

# awww, let's print Zed's poem
print("--------------")
print(poem)
print("--------------")

# setting a variable with simple addition arithmetic
five = 10 - 2 + 3 - 6
# print out that variable in a string
print(f"This should be five: {5}")

# making a function about some jelly beans!!!
# started is going to be an original value that then spawns beans, jars and creates
# all three values get stored with the return at the end
def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

# this is what the function secret_formula looks like when you run it with a value of 1
print(">>>> ", secret_formula(1))

# sets the starting point that will become started to be used in the function
start_point = 10000
# calling the function secret_formula yeilds three values in a list, they will be output into the three variables below
# Zed is trying to mess with us by having 2/3 of the names match, you can call them anything, don't be fooled by jelly_beans --> beans
beans, jars, crates = secret_formula(start_point)

#remember that this is another way to format strings
print("With a starting point of: {}".format(start_point))
# it's just like with an f"" string
print(f"We'd have {beans} beans, {jars} jars and {crates} crates.")

# let's restart the start_point by doing some arithmetic on the existing value
start_point = start_point / 10

# use the list of outputs from the function to populate af f string - they are output in order
# better make sure your string can accommodate the order of the function output
print("We can also do that this way:")
formula = secret_formula(start_point)
# this is an easy way to apply a list to a format string
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))
