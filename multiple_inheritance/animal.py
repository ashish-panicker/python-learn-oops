class Animal:
    """
    Base class for all animals.

    Attributes:
        name (str): The name of the animal.
    """

    def __init__(self, name):
        """
        Initialize an Animal instance.
        Args:
            name (str): The name of the animal.
        """
        self.name = name

    def speak(self):
        """
        Make the animal speak.

        Returns:
            str: A string representing the animal's sound.
        """
        return f"{self.name} makes a sound"


class Swimmer:
    """
    Mixin class for animals that can swim.
    """

    def swim(self):
        """
        Make the animal swim.
        
        Returns:
            str: A string describing the swimming action.
        """
        return f"{self.name} is swimming"


class Walker:
    """
    Mixin class for animals that can walk.
    """

    def walk(self):
        """
        Make the animal walk.
        
        Returns:
            str: A string describing the walking action.
        """
        return f"{self.name} is walking on {self.legs} legs"

    def __init__(self, legs=4):
        """
        Initialize a Walker instance.
        
        Args:
            legs (int, optional): Number of legs. Defaults to 4.
        """
        self.legs = legs


class Dog(Walker, Animal, Swimmer):  # Multiple inheritance
    """
    Class representing a dog, which is an animal that can walk and swim.
    Inherits from Animal, Walker, Swimmer
    
    Attributes:
        name (str): The name of the dog.
        breed (str): The breed of the dog.
        legs (int): Number of legs the dog has.
    """

    def __init__(self, name, breed, legs=4):
        """
        Initialize a Dog instance.
        
        Args:
            name (str): The name of the dog.
            breed (str): The breed of the dog.
            legs (int, optional): Number of legs. Defaults to 4.
        """
        # Call the parent initializers
        Animal.__init__(self, name)
        Walker.__init__(self, legs)
        # Set dog-specific attributes
        self.breed = breed

    def speak(self):
        """
        Make the dog speak.
        
        Returns:
            str: A string representing the dog's bark.
        """
        return f"{self.name} says Woof! I'm a {self.breed}"

fido = Dog("Fido", "Golden Retreivar")
print(fido.name)       # "Fido" (from Animal)
print(fido.breed)      # "Golden Retriever" (from Dog)
print(fido.legs)       # "4" (from Walker)
print(fido.speak())    # "Fido says Woof! I'm a Golden Retriever" (from Dog)
print(fido.walk())     # "Fido is walking on 4 legs" (from Walker)
print(fido.swim())     # "Fido is swimming" (from Swimmer)


print(Animal.__doc__)
print(Walker.__doc__)
print(Swimmer.__doc__)
print(Dog.__doc__)

# Diamond problem
print()

# MRO - Method resolution order
# Sequence of classes that python will look for while calling a method
# in a base class.
print(Dog.__mro__)
print(Dog.mro())