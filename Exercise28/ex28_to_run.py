print(True and False) # False

print(False and True) # False

print(1 == 1 and 2 == 1) # False

print("test" == "test") # True

print(1 == 1 or 2 != 1) # True

print(False and 1 == 1) # False

print(True or 1 == 1) # True

print("test" == "testing") # False

print(1 != 0 and 2 == 1) # False

print("test" == 1) # False

print(not (True and False)) # True

print(not (10 == 1 or 1000 == 1000)) # False

print(not (1 != 10 or 3 == 4)) # False

print(not ("testing" == "testing" and "Zed" == "Cool Guy")) # True

print(1 == 1 and (not ("testing" == 1 or 1 == 0))) # False - darn, this one is True because True and True is True!p

print("chunky" == "bacon" and (not (3 == 4 or 3 == 3))) # False

print(3 == 3 and (not ("testing" == "testing" or "Python" == "Fun"))) # False
