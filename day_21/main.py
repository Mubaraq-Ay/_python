# classes and objects
# oop - object oriented programming.

# everything in python is an object.
# class is a blueprint for creating objects.
# object is an instance created from a class:= an instance is an actual object created from a class.

# a class defines the attributes and behaviours that its objects can have.


# creating a class
# # class names conventionally use PascalCase (CamelCase).
# syntax:= 
# class ClassName:
#   code...

class Person:
    pass
print(Person)

# creating an object
# we can create an object by simply calling the class.

p = Person()
print(p) 


# class constructor.

# without the constructor, the class is basically useless. you have to manually set every attribute.

class Person:
    pass

p1 = Person()
p1.name = "Mubaraq"   # you'd have to manually set every attribute, every time
p1.age = 20

# but with the constructor __init__

class Person:
    def __init__(self, name, age):
        # self allows to attach parameter to the class.
        self.name = name
        self.age = age

p1 = Person("mubaraq", 20)
p2 = Person("ali", 21)

print(p1.name, p1.age)
print(p2.name, p2.age)

class Me:
    def __init__(self, firstname, lastname, age, country, city):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city

p = Me('mubaraq', 'ayanleke', 250, 'kuwaiti', 'dinar')
print(p.firstname, p.lastname, p.age, p.country, p.city)


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def describe(self):
        print(f'this is a {self.make} {self.model} {self.year}')

corolla = Car('toyota', 'corolla', 2020)
corolla.describe()

accord = Car('honda', 'accord', 2020)
accord.describe()


# object methods

# object can have methods. the methods are functions which belong to the object.

class Person:
    def __init__(self, firstname, lastname, age, country, city):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city

    def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. he lives in {self.country}, {self.city}'

p = Person('mubaraq', 'ayanleke', 250, 'kuwaiti', 'dinar')
print(p.person_info())