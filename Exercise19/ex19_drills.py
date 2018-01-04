# create the function cheese_and_crackers, it has two arguments
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")
# at the end of this function, the values that represent cheese_count and boxes_of_crackers are dropped
# the values are then replaced the next time the function is ran

# example where arguments are added directly
print("We can give the function numbers directly:")
cheese_and_crackers(20,30)

# example where we set the arguments from variables
print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# example where the arguments are set by doing some math
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

# zed is having us combine the options - doing math with variables we already set in the script
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

# this is my function from scratch
def climbs_many_trees(tree_species, avg_height, tree_houses):
    print("You're crazy to climb trees!")
    print(f"You climb the {tree_species} that are usually {avg_height} ft tall!")
    print(f"One has a tree house? {tree_houses}")
# tried to run a function in a function, I'll learn that later with Zed's game he's going on about
#    print(f"You eat {cheese_and_crackers} in there too?")

# arguments are a string, int, string
climbs_many_trees("cedar", 5, "YES!")

# set function variables using inputs
print("\nWhat kind of tree?\n>>>")
tree_species_in = input()
print("\rHow tall is the tree in feet?\n>>>")
avg_height_in = int(input())
print("\rDoes it have tree houses?\n>>>")
tree_houses_in = input()
print("\n")

# runs the function using input variables
climbs_many_trees(tree_species_in, avg_height_in, tree_houses_in)
print("\n")
