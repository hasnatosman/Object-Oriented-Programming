# Inheritance = Allows a class to inherit attributes & methods from another class
#               Helps with code reusability and extensibility
#               Class child(Parent)
from operator import truediv


class Animal:                   # Parent Class

    def __init__(self,name):    # constructor
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f'{self.name} is eating.')

    def sleep(self):
        print(f'{self.name} is sleeping.')

# Child Classes
class Dog(Animal):
    def speak(self):
        print('WOOF!')

class Cat(Animal):
    def speak(self):
        print('MEAO!')

class Mouse(Animal):
    def speak(self):
        print('SQUEEK!')

# objects
dog = Dog('Donal')
cat = Cat('Jerry')
mouse = Mouse('Nic')

print(dog.name)
print(dog.is_alive)
dog.eat()
dog.sleep()
dog.speak()