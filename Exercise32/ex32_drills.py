the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list

for number in the_count:
    # number is assigned the value from the list the_count
    print(f"A fruit of type: {number}")

# also we can go through mixed lists too - str & int
# notice we have to use {} since we don't know what's in it

for i in change:
    print(f"If I got {i}")

# we can also build lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
# range does not include the final value, this is why we don't have a list including 6
for i in range(0,6):
    print(f"Adding {i} to the list.")
    # append is a function that lists undertsand
    elements.append(i)

# i retains the last value
print(">>> i =", repr(i))
# shows all values within elements
print(">>> elements =", repr(elements))

# now we can print them out too
for i in elements:
    print(f"Element was: {i}")
