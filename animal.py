# Parent class
class Animal:
   
  def __init__(self, species:str=""):
    self.species = species

  def make_sound(self):
    print("Animal making sound")

# Child or Derived class
class Dog(Animal):
  pass

"""
SOLID Principle
S ingle Responsibility
O pen to Change Closed to modifications
L iskov substitution
I nterface segregation
D ependency Injection
"""