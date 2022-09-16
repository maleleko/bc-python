                        # 1) Encapsulation
# Encapsulation is the idea that we can group code together into objects; hence Object Oriented Programming. We use classes or "coding blue prints" to define what our objects are and how they behave. We encapsulate attributes and methods in our class.
class CoffeeM:
    def __init__(self,name):
        self.name = name
        self.water_temp = 200
    def brew_now(self,beans):
        print(f"Using {beans}!")
        print("Brew now brown cow!")
    def clean(self):
        print("Cleaning!")

                        # 2) Inheritance
# Inheritance is the idea that we pass along attributes and methods from one class into a "sub-class" or child class, and not have to re-write the code to make it work.  Child classes can be more specific versions of their Parent class.  Using the key word "super" will call methods

class CappuccinoM(CoffeeM): #<-- passes parent Class
    def __init__(self,name):
        super().__init__(name) #<--- adds this
        self.milk = "whole"
    def make_cappuccino(self,beans):
        super().brew_now(beans) #adds super again
        print("Frothy!!!")
# essentially, we get to add features from our parent class to our child class but also add new features to our child class that our parent class doesn't have access to. 
# something like an ancestry tree. we have features from our parents but a mixture of their genes makes us, and we have our own new set of features that we can potentially pass on to our descendants.  

                        # 3) Polymorphism
# Polymorphism means "many forms", and the idea in OOP is that a Child class can have a different version of a method than the Parent class. In this example the child class of CappuccinoM has a clean method, and so does CoffeeM. Depending on the class, the clean method will do different things.

class CappuccinoM( CoffeeM ):
    def __init__(self,name):
        super().__init__(name)
        self.milk = "whole"
    def make_cappuccino(self,beans):
        super().brew_now(beans)
        print("Frothy!!!")
    def clean(self): #<-- adds new clean method that does something different than our parent class
        print("Cleaning the froth!")
#essentially, we can create methods that our parent class has but make them do something different. it's important that we specify that we are in fact using a child class. (passing the parent class as parameter in our new child class)

                        #4) Abstraction
# Abstraction is an EXTENSION of Encapsulation, and we can hide attributes or methods that a Barista doesn't need to know about, like a CoffeeM. That way the Barista can make a cup of coffee in a simpler manner.

class Barista:
    def __init__(self,name):
        self.name = name
        self.cafe = CoffeeM("Cafe") #<-- here we add a new instance equalling to the main parent name. 
    def make_coffee(self):
        self.cafe.brew_now()
#essentially we just add a reference to our parent class with a new instance, and make new methods that work but not having to worry about the technicalities. acts as a hidden method so-to-speak.

