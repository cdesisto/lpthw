# Just going to write out a bunch of logic
print("""
NOT:
not false           True
not true            False
--> Not is opposite
""")

print("""
OR:
True or False       True
True or True        True
False or True       True
False or false      False
--> If Or contains a true, it's true
""")

print("""
AND:
True and False      False
True and True       True
False and True      False
False and False     False
--> If And contains a false, it's false
""")

print("""
NOT OR:
not (True or False)     False
not (True or True)      False
not (False or True)     False
not (False or False)    True
--> Just like the Or, but opposite because of not
""")

print("""
NOT AND:
not (True and False)    True
not (True and True)     False
not (False and True)    True
not (True and True)     True
--> Just like the And, but opposite because of not
""")

print("""
!=:
1 != 0          False
1 != 1          False
0 != 1          True
0 != 0          False
--> It's simple, just look at the numbers
""")

print("""
==:
1 == 0          False
1 == 1          True
0 == 1          False
0 == 0          True
--> Just remember to use the double ==
""")
