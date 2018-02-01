# set the variable i to have a value of 0
i = 0
# create an empty list called numbers
numbers = []
# variable that will control the while loop
limit = 28
# increment to add to i each time in the while loop
inc_add = 4

# start of the while loop
# for every time i is less than 6 the code block will execute
# once values are not less than 6 the print statement below will happen
#while i < 6:
# use the limit variable to control the while loop
while i < limit:
    # format string that includes current version of i
    print(f"At the top i is {i}")
    # appends i to the number list
    numbers.append(i)

    # add one to i
    #i = i + 1
    # use inc_add to control the value that incrementally adds to i
    i += inc_add
    # print full list numbers
    print("Numbers now: ", numbers)
    # print the current value of i
    print(f"At the bottom i is {i}")

# print a string
print("The numbers: ")

# for every num in numbers list, print num
for num in numbers:
    print(num)
