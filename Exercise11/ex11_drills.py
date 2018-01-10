# setting variables with persian_cat
# by using end= ' ' it tells print not to stop, but just move to the next line
print("How old are you?", end=' ')
# input() allows the user to input something and use that to set the variable
age = input()
print("How tall are you?", end= ' ')
height = input()
print("How much do you weigh?", end= ' ')
weight = input()

# age, height and weight are all set variables now, but we didnt stipulate as what kind so they are all strings by default
# to force the program to only accept numbers use int(input())
# use f string to call the variables and insert into this formatted string
print(f"So, you're {age} old, {height} tall and {weight} heavy.")
