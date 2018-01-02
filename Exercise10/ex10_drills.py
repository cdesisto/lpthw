# this tabby is tabbin' in!!! set that variable!
tabby_cat = "\nI'm tabbed in."
# for some reason I think that siamese would be more clever for 'split'
persian_cat = "I'm split\non a line."
# backslash cat - sounds like a weird variable, I'll set it anyway
backslash_cat = "I'm \\ a \\ cat."

# This fat cat has tabs, the \n\t is a good way to make multiple lines of output with a single line of code
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""
# Lesson learned: carriage return is a control character or mechanism used to reset a device's position to the beginning of a line of text
# So it will overwrite a tab and any other text ahead of it on that line...poison
# I guess it's like a typewriter, returns the carriage to 0s

# now I'ma gonna print all them cats! Funny, there's a cat on my shoulder as I type.
# she meets none of the descriptions above
print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)
#print(fat_cat, tabby_cat)
# make sure in the line above you include the comma, duh.
