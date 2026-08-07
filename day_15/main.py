# python type errors.

# SyntaxError.

# print 'hello world' - wrong syntax, because of the parenthesis

# correct way.
print('hello world')


# NameError.

# print(age) - we can't do this because age is not defined yet and we would get a name error if we print this

# correct way
age = 10
print(age)


# IndexError.

# numbers = [1, 2, 3, 4, 5]
# numbers[5]      wont work because the index is out of range. there are only 4 indexes in this list btw, so it's 0 to 4.


# ModuleNotFoundError

# import maths  - no module named maths - wrong module, the correct module is math.

# correct way

import math


# AttributeError

import math

# math.PI  - pi and not PI

math.pi     # - correct way.


# KeyError
users = {
    'name':'Asab', 
    'age':250, 
    'country':'Finland'
}

print(users['name'])
# print(users['county']) there's a typo 'county' instead of 'country'.

print(users['country'])

# TypeError
# print(4 + '3') can't add a string and int

# correct
print(4 + int('8'))

# ImportError
# from math import power

from math import pow
print(pow(2,3))