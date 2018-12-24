#sets the variable 'ten_things'
ten_things = "Apples Oranges Crows Telephone Light Sugar"

#opening statement that we print
print("Wait there are not 10 things in that list. Let's fix that.")

#stuff is ten_things split into a list, split happens on ' '
stuff = ten_things.split(' ')
# more stuff is a list of more strings
more_stuff = ["Day", "Night", "Song", "Frisbee",
                "Corn", "Banana", "Girl", "Boy"]

#a while loop that will happen until stuff doesn't equal 10
while len(stuff) != 10:
    #next one is set to be the last value of more_stuff
    next_one = more_stuff.pop()
    #print the statement that you are adding the last value of more_stuff
    print("Adding: ", next_one)
    #append the last value of more_stuff to the stuff list
    stuff.append(next_one)
    #print how many items there are now in the stuff list, should be one more than the last until there are 10 items
    print(f"There are {len(stuff)} items now.")

#once the while loop finishes, we print a statement
print("There we go: ", stuff)

#print another statement ahead of more cool statements
print("Let's do some things with stuff.")

#print the 2nd item in the stuff list
print(stuff[1])
#print the last item in the list
print(stuff[-1])
#print the last item in the list by popping it off - yes it's the same as [-1]
print(stuff.pop())
#prints the items in stuff joined together with a separater of ' '
print(' '.join(stuff))
#prints the items 3-4 (up to, but not including 5) items in the list separated by a #
print('#'.join(stuff[3:5]))


###try to reproduce the while-loop with a for-loop
