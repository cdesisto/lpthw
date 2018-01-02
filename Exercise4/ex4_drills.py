#Variables about some cars, people and carpools
cars = 100
#space_in_a_car - does it really need be a float? Even child seats take up a whole seat!
space_in_a_car = 4
#Gotta have at least one per car!
drivers = 30
#Load up those vehicles!
passengers = 90
#Guilty, I don't drive to work
cars_not_driven = cars - drivers
#Vroom, vroom - this is much easier than setting the variable to also be the same value as drivers
cars_driven = drivers
#Yeah, let's all assume that people don't have cars full of garbage too
carpool_capacity = cars_driven * space_in_a_car
#This arithmetic sounds about right, hmmmm
average_passengers_per_car = passengers / cars_driven

#Let's chat about these cars and who *should* be in them.
print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")

#Notes:
# = sets a variable while == tests if two things have the same value.
# You don't have to put spaces around an = while setting variables, but it's good form
