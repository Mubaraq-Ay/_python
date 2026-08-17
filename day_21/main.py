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

# object default methods
# this is giving the constructor parameters fallback values, same idea as default arguments in regular functions btw.

class Person:
    def __init__(self, firstname = 'mubaraq', lastname = 'ayanleke', age = 250, country = 'qatar', city = 'medinah'):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city

    def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. he lives in {self.country}, {self.city}'

p1 = Person()
print(p1.person_info())

# i can override the values
p2 = Person('ali', 'smith', 230, 'saudi', 'makkah')
print(p2.person_info())

# method to modify class default values.
# this let's us change an object's data after it has been created. 

class Person:
    def __init__(self, firstname = 'mubaraq', lastname = 'ayanleke', age = 250, country = 'qatar', city = 'medinah'):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city
        self.skills = []

    def person_info(self):
            return f'{self.firstname} {self.lastname} is {self.age} years old. he lives in {self.country}, {self.city}'

    def add_skill(self, skill):
            self.skills.append(skill)

p1 = Person()
print(p1.person_info())
p1.add_skill('html')
p1.add_skill('css')
p1.add_skill('python')

print(p1.skills)

p2 = Person('ali', 'smith', 230, 'saudi', 'makkah')
print(p2.person_info())

p2.add_skill('docker')
p2.add_skill('go')

print(p2.skills)


# 2

class Person:
    def __init__(self, firstname='Mubaraq', lastname='Ayinde', age=20):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old'

    def set_age(self, age):
        self.age = age

p1 = Person()
print(p1.person_info())

p1.set_age(25)
print(p1.person_info())


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def describe(self):
        print(f'this is a {self.make} {self.model} {self.year}')

    def set_year(self, year):
        self.year = year

corolla = Car('toyota', 'corolla', 2020)
corolla.describe()

accord = Car('honda', 'accord', 2020)
accord.describe()

corolla.set_year(2026)
corolla.describe()