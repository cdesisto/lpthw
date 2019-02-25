# Implicit Inheritance
# Override Explicitly
# Alter Before or After
# All Three Combined

class Parent(object):

    def override(self):
        print("PARENT overrride()")

    def implicit(self):
        print("PARENT implicit()")

    def altered(self):
        print("PARENT altered()")

class Child(self):

    def override(self):
        print("CHILD override()")

    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(child,self).altered()
        print("CHILD AFTER PARENT altered()")

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()
