# here's a function to find the slope of your favorite mountain
def mountain_slope(height, diameter):
    return ((diameter / 2) / height) * 100

# gives some facts about random mountains
mt_rainier = mountain_slope(14410, 5280)
mt_hood = mountain_slope(12000, 5280)

print(f"Mt Rainier's slope is {mt_rainier}.")
print(f"Mt Hood's slope is {mt_hood})")

# the user interacts to talk about their favorite mountain
print("What is your favorite mountain?")

favorite_name = input()

print("How tall is it in feet?")

favorite_height = int(input())

print("How wide is it across in feet?")

favorite_diam = int(input())

# prints the slope based off inputs
print("Did you know that it has a slope of ", mountain_slope(favorite_height, favorite_diam), "%?")
