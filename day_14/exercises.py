# 1.

# map - transforms every item in an iterable.
# filter - keeps only the items that satisfy a condition.
# reduce - combines all items into a single value.

# 2.

# Higher-order function:
# A function that takes another function as an argument
# or returns a function.

# closure.
# An inner function that remembers variables
# from its enclosing function even after it finishes.

# Decorator:
# A special higher-order function that adds
# extra functionality to another function
# without changing its original code.


countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for country in countries:
    print(country)

for name in names:
    print(name)

for number in numbers:
    print(number)

# level 2
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

def country_uppercase(func):
  return func.upper()
uppercase = map(country_uppercase, countries)
print(list(uppercase))

# change each number to its square.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def square_num(x):
    return x ** 2
square = map(square_num, numbers)
print(list(square))

names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']

def names_upper(func):
    return func.upper()
upper_name = map(names_upper, names)
print(list(upper_name))

# filter out countries containing land
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

def land_in_countries(func):
    if 'land' in func:
        return True
    return False
countries_land = filter(land_in_countries, countries)
print(list(countries_land)) 

def num_of_characters(func):
    if len(func) == 6:
        return True
    return False
number_char = filter(num_of_characters, countries)
print(list(number_char))

def num_of_characters(func):
    if len(func) >= 6:
        return True
    return False
number_char = filter(num_of_characters, countries)
print(list(number_char))

# filter out countries starting with E
def first_char(func):
   return func.startswith('E')
letter = filter(first_char, countries)
print(list(letter))

# use reduce to sum all the numbers in this list.
from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def add_nums(x, y):
    return int(x) + int(y)
total = reduce(add_nums, numbers)
print(total)

