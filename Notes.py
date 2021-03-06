print("9.0. \\n escape character for new lines")
print("""9.1 \"\"\" triple quote allows you to type anything in there exactly as you see it
    Text must be slammed to the left, not indented unless you want the indent to show like this
""")

print("""10.0 Check out all these helpful escaped charaters:
    \\\\  Backslash
    \\' single quote
    \\" double-quote
    \\n new lines
    \\r carriage return
""")

print('''11.0 - repr() will  tell you how something is represented in python
    EX: 42 as a string is \'42\', but as a number is 42''')
print("11.1 Fun fact: end=\' \' at the end of a print line tells the prigram not to end the line and just move to the next line")
print('''11.2 When the user inputs text they can type directly in terminal and not in python, no quotes needed (unless you want them).\n
''')

print("13.0 - argv is 'argument variable' \nIt holds the arguments that you pass to your script")
print("13.1 - Really, there are only three arguments here because the script.py MUST be there\n")

print("14.0 - Set value types (int) as early as possible in the script\n")

print("""16.0 - Commands to remember
\tclose: clsoes a file (file->save)
\tread: reads the contents of a file, result can be assigned to a variable
\treadline: reads just one line of a text file
\ttruncate: empties the file (!!)
\twrite('stuff'): writes "stuff" to the file
\tseek(0): moves the read/write location to the beginning of the file
""")

print("""18.0 - Functions do three things:
\t1. Name pieces of code as variables name strings/numbers
\t2. Take arguments like scripts take argv
\t3. Using 1 and 2 they let you make mini-scripts)
""")
print("""18.1 - *args - aseteric makes the following text a list of arguments in a parameter""")
print("18.2 - Ending lines with a : (colon) makes the next line indent")
print("18.3 - Function = Mini-Script :)")
print("""18.4 - Function Checklists:
\nWhen you write your functions:
\t1. Does your function definition start with def?
\t2. Does your function name have only characters and underscore characters?
\t3. Did you put an open parenthesis right after the function name?
\t4. Did you put your arguments after the parenthesis separated by commas?
\t5. Did you make each argument unique? (No dupe names)
\t6. Did you put a close parentesis and a colon after the arguments?
\t7. Did you indent all lines of code you want in the function four spaces? One tab, duh
\t8. Did you "end" your function by going back to writing with no indent?
\n When you run/use/call a function check:
\t1. Did you run this function by typing its name?
\t2. Did you put the ( character after the name to run it?
\t3. Did you put the values you want to use into the parenthesis separated by commas?
\t4. Did you end the function call with a ) character?
""")
print("Function Names cannot start with numbers or underscores, but can contain them"
)

print("19.0 - The variables in your function are not connected to the veriables in your script")

print("""20.0 - += is a shorthand method to say this variable equals this variable plus a value\r
for total. Example: 'total = total + a' can be shortened to 'total += a' """)

print("23.0 New stuff in Strings, Bytes, and Char Encoding:")
print("23.1 - DBES = Decode Bytes, Encode Strings")
print("""23.2 - Stuff I've not seen yet
\r\tsys.argv =
\r\tif: = an if-statement tets the truth of a variable and based on that truth run another piece of code
\r\tstrip() = strips the \\n from the beginning of a line - removes whitespace from beginning/end, spaces included
\r\tencode() = converts raw bytes into strings
\r\tdecode() = converts strings into raw bytes
\r\t'maximum recursion depth exceeded' - if statement is removed and the loop keeps going and going until memory is exceeded
""")

print("24.0 - More Practice:")
print("24.1 - The value of a variable can start/end with a triple quote like in a print function, it just doesn't need parenthesis on either end")

print("""25.0 - Even more practice:
\n25.1 - .pop(i) = return an item from a list in i position
\n25.2 - .split(' ') = splits strings on a character, in this case a spaces
\n25.3- ''' ''' within a function and not after print( means it is documentation comments and appears in the helpful
\n25.4- Help can be called within python with 'help' and from there call help for the module with the name of the .py file
""")

print("""32.0 - Loops & lists
32.1 - Range - 2nd number is not inclusive --> range(0,6) is 0, 1, 2, 3, 4, 5.
32.2 - Ranges need the following commands, start value, stop value and step. E.g.:\n\t>>> list(range(0, 30, 5))\n\t[0, 5, 10, 15, 20, 25]
""")

print(""" 33.0 - While Loops
33.1 - Use While loops sparingly - usually a for loop is better
33.2 - Review the statement that it can become false at some point
33.3 - When in doubt, print your test variable at the top nad bottom of the while-loop to see what it's doing.
""")

print(""" 35.0 - Branches & functions
35.1 - exit(0) allows you to abort a program without error. exit(1) is exiting with an error
""")

print("""36.0 - Designing and Debugging
\n**Rules for if-statements**
36.1 - Every if-statement must have an else.
36.2 - If this else should hever run because it doesn't make sense,\nthen you must use a die function in the else that points out an error\nmessage and dies, just like we did in the last exercise. This will find many errors.
36.3 - Never nest if-statements more than two deep and always try to do them one deep
36.4 - Treat if-statements like paragraphs, where each if-elif-else grouping\nis like a set of sentences. Put blank lines before and after
36.5 - Your Boolean tests should be stimple. If they are complex, move their calculations to variables earlier in your function and use a good name for the variable.
\n**Rules for Loops**
36.6 - Use a while-loop only to loop forever, and that means probably never.
36.7 - Use a for-loop for all other kinds of looping, especially if ther is a fixed or limited number of things to loop over.
\n**Tips for Debugging**
36.8 - Do not use a 'debugger.' Lots of useless information
36.9 - The best way to debug a program is to print variables and values throughout
36.10 - Make sure parts of your programs work as you work on them. Code a little, run a little fix a little.
""")

print("""38.0 - Lists
38.1 - When to use lists
\t1. If you need to maintain order. Remember, this is listed order, not sorted order. Lists do not sort for you.
\t2. If you need to access the contents randomly by a number. Remember, this is using cardinal numbers starting at 0.
\t3. If you need to go through the contents linerly (first to last). Remember, that's what for-loops are for.
""")

print(""" 39.0 - Dictionaries
39.1 - A list is for an ordered list of items, a dictionary is for matching items. It's aka a lookup table)
39.2 - Use lists when order matters, for a dictionary if there is a dupe key, the last occurence is requested
39.3 - You can add individual key/value entries, delete individual entries, clear or delete the entire dictionaryself.
""")

print(""" 40.0 - Modules
40.1 - A module is a specialized dictionary that can store python code so you can access with the '.' operator.
40.2 - A Class is a grouping of functions and data and place them in a container you can access with the '.' operator.
""")

print(""" 42.0 - Has-a, Is-a, Objets, and Classes
42.1 - ""None"" is a built-in constant to represent the absence of a value
""")

print(""" 44.0 - Inheritance vs Composition
44.1 - the use of self is an empty block, it inherits all behavior from parent
""")
