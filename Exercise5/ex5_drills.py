name = 'Chris De Sisto'
age = 31 # Not a lie
height = 71 # inches
weight = 160 # lbs
eyes = 'Brown'
teeth = 'Whiteish'
hair = 'Black'
height_ft = height / 12
weight_kg = weight * .454

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print("Actually, that's not too heavy")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")
print(f"He is {height_ft} ft tall.")
print(f"He is", round(weight_kg), "kg heavy.") # See what I did there, I could have rounded weight_kg when I set the variable, but I did it here instead.


# This line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")

# Notes:
# You cannot name a variable with a starting character of a number
# You can round using the round() function e.g.: round(1.733) - check out line 18
