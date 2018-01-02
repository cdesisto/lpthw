# Setting the variable formatter
formatter = "{} {} {} {}"

# Sets the argruments within formatter by using the command format to be four numbers
print(formatter.format(1, 2, 3, 4))
# Sets the argruments within formatter by using the command format to be four strings
print(formatter.format("one", "two", "three", "four"))
# Sets the argruments within formatter by using the command format to be four boolean
print(formatter.format(True, False, False, True))
# Sets the argruments within formatter by using the command format to be four formatters
print(formatter.format(formatter, formatter, formatter, formatter))
# Sets the argruments within formatter by using the command format to be four strings on separate lines
# Zed is introducing indentation!!!!
# Removing commas makes errors 'tuple index out of range' because there arent enough arguments in format to match formatter
print(formatter.format(
    "Try your"
    "own text here",
    "Maybe a poem",
    "Or a song about fear"
))
