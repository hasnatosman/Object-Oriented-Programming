# Object = A "bundle" of related attributes (variables) and methods (functions)
#         Ex. phone, cup, book
#         You need a "class" to create many objects
# from time import process_time_ns

# Class: (blueprint) used to design the structure and layout od an object
from car import Car

car1 = Car('Mustang', 2024, 'red', False)
car2 = Car('Corvette', 2025, 'Blue', True)
car3 = Car('Charger', 2026, 'White', True)
car4 = Car('BMW', 2027, 'Blue', False)


# print(car1.model)
# print(car1.year)
# print(car1.color)
# print(car1.for_sale)

car1.describe()
car1.drive()
car1.stop()
print('-' * 40)
print()

car2.describe()
car2.drive()
car2.stop()
print('-' * 40)
print()

car3.describe()
car3.drive()
car3.stop()
print('-' * 40)
print()

car4.describe()
car4.drive()
car4.stop()
print('-' * 40)


# Attributes are variables that an object has
# Methods are functions that belong to an object, they define what this object can do
