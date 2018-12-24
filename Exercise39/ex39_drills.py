#create a mapping of state abbreviation to statements
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

#create a basic set of states and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

#add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

#print out some cities
print('-' * 10)
print("NY State has : ", cities['NY'])
print("OR State has : ", cities['OR'])

#print some statements
print('-' * 10)
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])

#do it by using the state then cities dict
print('-' * 10)
print("Michigan has : ", cities[states['Michigan']])
print("Florida has : ", cities[states['Florida']])

#print every state abbreviation
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbrevated {abbrev}")

#print every city in state
print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

#now do both at the same time
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

print('-' * 10)
#safely get a abbreviation by state that might not be there
state=states.get('Texas')

if not state:
    print("Sorry, no Texas.")

#get a city with a default values
city = cities.get('TX', 'Does Not Exist')
print(f"The city for that state 'TX' is : {city}")

#get length of dictionary
print(f"The cities dictionary is {len(cities)} long")

#print a string of the dictionary
print(f"The string of the cities dictionary is: {str(cities)}")

#find out what type of variable the dict is
print(f"In case you wanted to know, cities is a {type(cities)}")

#how to use dict.values() - a list of all values in a dict
print(f"To see all of the values, not keys in a dictionary, use 'dict.values()'. States has: {dict.values(states)}")
