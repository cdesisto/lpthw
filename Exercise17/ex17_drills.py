from sys import argv
from os.path import exists

# 3 parts to run script
script, from_file, to_file = argv

# Tells the user what's going to happen (from_file and to_file come from argv
print(f"Copying from {from_file} to {to_file}")

# we could do thsese two on one line, how?
# Opens file as read-only
##in_file = open(from_file)
# Loads the data into python
##indata = in_file.read()
# This line replaces the open and read lines in a single line - it opens and reads!
indata = open(from_file).read()

# Prints the size of the file
print(f"The input file is {len(indata)} bytes long")

# Tests to see if file exists - returns TRUE or FALSE
print(f"Does the output file exist? {exists(to_file)}")
# Sets the user up for the input
print("Ready, hit RETURN to continue, CTRL-C to abort.")
# Input prompt with empty string
input()

# Opens the output file with write access
out_file = open(to_file, 'w')
# Writes out the file using the data stored from the input file
out_file.write(indata)

# Sends the user a message
print("Alright, all done.")

# Close yer files!
out_file.close()
# Comment out the following line because in_file is never actually opened because the script was shortened
##in_file.close()
