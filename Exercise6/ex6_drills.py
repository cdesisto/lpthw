# Let's set the variable for types_of_people
types_of_people = 10
# x needs a value to, let's make it some super cool formatted text
x = f"There are {types_of_people} types of people?"

# binary - let's set that with something really uncreative
binary = "binary"
# in case you forgot what the contraction for 'do not' is, here it is!
do_not = "don't"
# Well in the case of y, I can think of easier ways to make this sentence, but this is all about the hard way!
y = f"Those who know {binary} and those who {do_not}."

# we haven't printed anything yet, we are overdue!
print(x)
# making up for lost time here, let's print y now!
print(y)

# Let's start telling that lousy joke with some formatted text that includes x
print(f"I said: {x}")
# Here, the single quotes don't mean anything - they are just for punctuation in the print statement.
# I can see that because I checked the output.
print(f"I also said: '{y}'")

# Here's Zed's opinion
hilarious = False
# I want to know what the empty braces are for, I'll figure that out in a minute
# Well I played around a bit, the {} refers to hilarious being boolean
# Changing hilarious it to text uses the string
joke_evaluation = "Isn't that joke so funny?! {}"

# Let's say what we think of that joke
print(joke_evaluation.format(hilarious))

# Set a variable for w, it's all text
w = "This is the left side of..."
# Set a variable for e, it's also all text
e = "a string with a right side."

# Let's put two strings together. Hey Look, no spaces between w and e
print(w + e)
