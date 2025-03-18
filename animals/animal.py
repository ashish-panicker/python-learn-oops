from abc import ABC, abstractmethod

"""
Abstract class
1. Cannot be instantiated, they can only be inherited
2. They can have both abstract and non abstract methods
3. While inheriting an abstract class, all abstract methods must be overridden
4. Is defined using the AbstractBaseClass(ABC) module
    from abc import ABC, abstractmethod
    class AbstractClass(ABC):
      pass
5. Abstract method is defined using the @abstractmethod decorator
    @abstractmethod
    def some_method(self):
      pass

"""

class Animal(ABC):
    def __init__(self, name: str):
        self.name = name

    def display_info(self) -> None:
        """Concrete method (not abstract) - available to all subclasses"""
        print(f"This is {self.name}, a {self.__class__.__name__}.")

    @abstractmethod
    def make_sound(self) -> None:
        """Abstract method"""

    @abstractmethod
    def food_habit(self) -> None:
        """Abstract method"""

class Dog(Animal):
    def make_sound(self) -> None:
        print(f"{self.name} barks: Woof! Woof!")

    def food_habit(self):
        print(f"{self.name} is a omnivore.")

class Lion(Animal):
    def make_sound(self):
        print(f"{self.name} roars: Grr! Grr!")

    def food_habit(self):
        print(f"{self.name} is a carnivore.")

dog = Dog("Golden")
lion = Lion("Simba")

animals = [dog, lion]

for animal in animals:
    print("\n---Animal---")
    animal.make_sound()
    animal.food_habit()