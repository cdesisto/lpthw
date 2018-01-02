## Cannot figure out how to use input() to set arguments (argv)
##argv = input("script, first, second, third? ")
##print(">>>>>", argv)
##print(repr(argv))
# import the argv module from system
from sys import argv
# read the WYSS section for how to run This
# WYSS is 'what you should see' and is a section within the exercise
# The next line unpacks argv and gets the variables assigned to it
script, first, second, third = argv

# print each argument that goes into argv including the script name
print("The script is called:", script)
print("You first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

#input("What are the arguments?") = argv
#print("The script is called:", script)
#print("You first variable is:", first)
#print("Your second variable is:", second)
#print("Your third variable is:", third)

## ex13_drills.py yes no maybe
