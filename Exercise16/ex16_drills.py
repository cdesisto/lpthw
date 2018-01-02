#import argv module from system
from sys import argv

#set values for argv
script, filename = argv

#tells the user what's going to happen using filename in f-strings
#will prompt user if they want to erase the file
print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you want to do that, hit RETURN.")

#input prompt for whether or not to erase the file
input("?")

#opens the file in the start script
#'w' signifies that the file will be opened to write
print("Opening the file...")
target = open(filename, 'w')

#truncates the opened file
print("Truncating the file. Goodbye!")
target.truncate()

#sets user up for inputs of the file that was truncated
print("Now I'm going to ask you for three lines.")

#asks user to input three strings of Text
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

#message that python will print the lines
print("I'm going to write these to the file.")

#writes the strings into the new file on a new line for each string
#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

#Trying to replace the long target.write sequences above with a single line of code
#This is the winner that I came up with myself...
target.write(f"{line1}\n{line2}\n{line3}")

#This doesnt work (I tried to figure this out using the internet):
##target.write(f"{0}, {1}, {2}". (line1, line2, line3))

#This one works, but was taken from https://stackoverflow.com/questions/8691311/python-how-to-write-multiple-strings-in-one-line
#I don't quite get it though..
##target.write('%r\n%r\n%r\n' % (line1, line2, line3))

#messages the user the file will be closed then script closes the input file
print("And finally, we close it.")
target.close()
