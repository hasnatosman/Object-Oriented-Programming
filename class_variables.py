# Class Variables = Shared among all instances(object) of class
#                   Defined outside the constructor
#                   Allow you to share data among all objects created from that class

class Student:

    class_year = 2024                      # class variable
    num_student = 0                        # class variable


    def __init__(self, name, age):         # name, age are attributes
        self.name = name                   # self.name is instance variable
        self.age = age                     # self.age is instance variable
        Student.num_student += 1

student1 = Student('John', 30)
student2 = Student('Smith', 35)
student3 = Student('ALex', 25)
student4 = Student('Benn', 45)

print(student1.name)
print(student1.age)
print(Student.class_year)            # good practice is calling by class name

print(student2.name)
print(student2.age)
print(student2.class_year)           # though it can be called by any object/instance

print(f"My graduating class of {Student.class_year} has {Student.num_student} students.")
