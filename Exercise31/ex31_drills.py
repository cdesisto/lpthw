# set the scene for the game
print("""You enter a dark room with two doors.
Do you go through door #1 or door #2?""")

# make the user choose the door
door = input(">")

# if statement that if you pick 1 then get another option
if door == "1":
    print("There's a giant bear here eating a cheese cake.")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")

# input another prompt if you chose 1
    bear = input("> ")

# if statement for if you choose 1
    if bear == "1":
        print("The bear eats your face off. Good job!")
# if you chose 2 instead of 1, you get a print statement - game ends
    elif bear == "2":
        print("The bear eats your legs off. Good job!")
# if you chose anything besides 1 or 2 you get some more print statements - game end
    else:
        print(f"Well, doing {bear} is probably better.")
        print("Bear runs away.")

# if statement that if you picked 2 at the original prompt you get more prompts
elif door == "2":
    print("You stare into the endless abyss at Cthulu's retina.")
    print("1. Blueberries")
    print("2. Yellow jacket clothespins")
    print("3. Understanding revolvers yelling melodies.")

# input something for insanity 1-3
    insanity = input("> ")

# if statement that if you choose 1 or 2 you get a print statement - game end
    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello.")
        print("Good job!")
# if you chose anything besides 1 or 2 you get a print statement and - game end
    else:
        print("The insanity rots your eyes into a pool of muck.")
        print("Good job!")

# to use a range of numbers, use 'in range(x, y)' but must make sure that the value to test is a number.
# I was dumb and didn't set door to be an int and had to use the internet for help!
elif int(door) in range(3, 45):
    print("You chose a big number!")

# if you chose anything besides 1 or 2 at the first input, print statement - game end
else:
    print("You stumble around and fall on a knife and die. Good job!")
