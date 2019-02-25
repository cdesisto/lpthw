## Animal is an object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## Dog is-a animal
class Dog(Animal):

    def __init__(self, name):
        ## Dog has-a name
        self.name = name

## Cat is-a Animal
class Cat(Animal):

    def __init__(self, name):
        ## Cat has-a name
        self.name = name

## Person is-a object
class Person(object):

    def __init__(self, name):
        ## Person has-a name
        self.name = name

        ## Person has a pet of some kind
        ## None is a built-in constant to represent the absence of a value
        self.pet = None

## Employee is a Person
class Employee(Person):

    def __init__(self, name, salary):
        ## super is used as a shortcut to access the base class Employee
        super(Employee, self).__init__(name)
        ## Employee has-a salary
        self.salary = salary

## Fish is-a object
class Fish(object):
    pass

## Halibut is-a Fish
class Halibut(Fish):
    pass

## Add this to make code run
## Salmone is-a Fish
class Salmon(Fish):
    pass

## rover is-a Dog (named Rover)
rover = Dog("Rover")

## satan is-a Cat (named Satan)
satan = Cat("Satan")

## mary is-a Person (named Mary)
mary = Person("Mary")

## mary has-a pet (named satan)
mary.pet = satan

## frank is-a Employee (named Frank with a salary of 120,000)
frank = Employee("Frank", 120000)

## frank has-a pet (named rover)
frank.pet = rover

## flipper is-a Fish
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

## harry is-a Halibut
harry = Halibut()
