# import argv from system so we can pass files to script
from sys import argv

# set the input values for argv
script, input_file = argv

# define function print_all - f is file
def print_all(f):
# to find where function begins
    print(">>> = f before f.read()", f)
# read in file
    print(f.read())
# to find where function ends
    print("<<< = f after f.read()", f)

# define function rewind - rewinds file
def rewind(f):
# to find where function begins
    print(">>> = f before f.seek()", f)
# seeks to byte 0 in the file
# this does not move to row 0 !!!
    f.seek(0)
# to find where function ends
    print("<<< = f after f.seek()", f)

# defines function print_a_line using the variable line_count and the file
def print_a_line(line_count, f):
# to find where function starts
    print(">>> = f before f.readline()", f)
# print the variable line_count and what's read on that line from the file
    print(line_count, f.readline())
# to find where function ends
    print("<<< = f after f.readline()", f)

# sets the current_file variable to be the input file
current_file = open(input_file)

# prints a string
print("First let's print the whole file:\n")

# puts the input file (from the variable current_file) into the print_all function
# current_file becomes the f variable in the function
print_all(current_file)

# prints a string
print("Now let's rewind, kind of like a tape.")

# puts the input file into the rewind function to take us back to the beginning of the file
# we do this because we just printed the whole thing and we are at the end of the file
rewind(current_file)

# prints a string
print("Let's print three lines:")

# this is where the functions get called
# sets current line to a value 1 - we are currently at the top of the file at row 0
current_line = 1
# uses the print_a_line function to read the current_line (1) from the input file
print_a_line(current_line, current_file)

# sets the current_line variable to be the previous value + 1
#current_line = current_line + 1
# rewrite the above line using shorthand:
current_line += 1
# uses the print_a_line function to read the current_line (2) from the input file
print_a_line(current_line, current_file)

# sets the current line to be the previous valuve + 1
#current_line = current_line + 1
# rewrite the above line using shorthand:
current_line += 1
# uses the print_a_line function to read the current_line (3) from the input file
print_a_line(current_line, current_file)
