# import the argv module from system
from sys import argv

# unpacks argv and sets the variables for the script (this .py) and the the incoming text file
script, filename = argv

# sets the variable txt to be the opened text file set with argv
txt = open(filename)

# prints a string including your filename
print(f"Here's your file {filename}: ")
# prints the text within the filename using the .read command
print(txt.read())

# close the damn file!
txt = txt.close()

# prompts you to input the filename again
print("Type the filename again: ")
# uses input to set file_again variable
file_again = input("> ")

# sets the variable txt_again as the file called from the input
txt_again = open(file_again)

# prints the reopened file
print(txt_again.read())

# close the damn file again!
txt_again.close()
