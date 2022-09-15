class Human:
    """Class to represent Human"""
    # In Class, there exists two level of variables
    # 1. Class Variable
    # 2. Object Variable

    # Ex: this is Class Variable
    type = "human"
    school = "Engineering School"

    def __init__(self, name, age):
        # Ex: this is Object Level Variable
        self.name = name
        self.age = age
        self._car = "Honda"


    # In a Class, there are 3 types of method
    # 1. Object level method
    # 2. Class level method
    # 3. Static Method - Ordinary method that aims
    # to return an input

    # Example of Object Level Method. Self is passed as args
    def speak(self):
        return "Hello , my name is: ", self.name

    # Example of Static Method. 
    @staticmethod
    def add_variables(x,y):
        return x + y
    
    # Example of Class Method. CLS is passed as args. and its used to modify Class Variable.
    @classmethod
    def change_school(cls, name):
        Human.school = name
    
    # Property is a special decorator function in OOP.
    # property(fget=None, fset=None, fdel=None, doc=None)

    # return - gets the property
    @property
    def car(self):
        return self._car
    
    # setter - assign the property to value
    @car.setter
    def car(self, value):
        print("Setting Car Property")
        self._car = value

        
    # deleter - del the property
    @car.deleter
    def car(self):
        print("Deleting Car Property")
        del self._car



john = Human('John', 20)
print("John speaking")
john.speak()
john.add_variables(5,5)
john.change_school("Mars School")

# Property 

print("Initial Car.")
print("\nGet Method:", john.car)

john.car = "Maserati"
print("\nAfter Setting NewCar:", john.car)

del john.car
print("\nDel Method.")