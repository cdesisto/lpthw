# Here's some new strange stuff, remember type it exactly.

# Set days to be the days of the week with spaces
days = "Mon Tues Wed Thu Fri Sat Sun"
# Set the first 8 months to be separated by new lines
months = "\nJan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

# Print the days of the week (should print on single line)
print("Here are the days: ", days)
# Print the months, Jan should be on the same line as the original string, then each month on a new line
print("Here are the months: ", months)

# Print this long multi line string
# if print(""" is indented and everything else is below it, it still breaks
# if you indent the string, but not the """ then the text will be indented
# only two quotes at the end will break it
print("""
    There's something going on here.
    WIth the three double-quotes.
    We'll be able to type as much as we like.
    Even 4 lines if we want, or 5, or 6.
""")
