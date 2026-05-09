#boolean, True or False . the first letter must be capitalized unlike js.
# operators :
# assignment operators =, +=, -=, *=, /=, %=, //=, **=, &=, |=, ^=, >>=, <<=

# arithmetic operators
# Addition(+): a + b
# Subtraction(-): a - b
# Multiplication(*): a * b
# Division(/): a / b
# Modulus(%): a % b
# Floor division(//): a // b
# Exponentiation(**): a ** b


# division in python gives a floatinf number.

# Arithmetic Operations in Python
# Integers

# print('Addition: ', 1 + 2)        # 3
# print('Subtraction: ', 2 - 1)     # 1
# print('Multiplication: ', 2 * 3)  # 6
# print ('Division: ', 4 / 2)       # 2.0  Division in Python gives floating number
# print('Division: ', 6 / 2)        # 3.0         
# print('Division: ', 7 / 2)        # 3.5
# print('Division without the remainder: ', 7 // 2)   # 3,  gives without the floating number or without the remaining
# print ('Division without the remainder: ',7 // 3)   # 2
# print('Modulus: ', 3 % 2)         # 1, Gives the remainder
# print('Exponentiation: ', 2 ** 3) # 8 it means 2 * 2 * 2

# Floating numbers
# print('Floating Point Number, PI', 3.14)
# print('Floating Point Number, gravity', 9.81)

# Complex numbers
# print('Complex number: ', 1 + 1j)
# print('Multiplying complex numbers: ',(1 + 1j) * (1 - 1j))

# print('== Addition, Subtraction, Multiplication, Division, Modulus ==')

# Calculating area of a circle
# radius = 10                                 # radius of a circle
# area_of_circle = 3.14 * radius ** 2         # two * sign means exponent or power
# print('Area of a circle:', area_of_circle)

# # Calculating area of a rectangle
# length = 10
# width = 20
# area_of_rectangle = length * width
# print('Area of rectangle:', area_of_rectangle)

# # Calculating a weight of an object
# mass = 75
# gravity = 9.81
# weight = mass * gravity
# print(weight, 'N')                         # Adding unit to the weight

# # Calculate the density of a liquid
# mass = 75 # in Kg
# volume = 0.075 # in cubic meter
# density = mass / volume # 1000 Kg/m^3
# print(density, 'Kg/m^3') # Adding unit to the density


# comparison operators
# ==, !=, >, <, >=, <=

print(3 > 2)
print(3 >= 2)
print(3 < 2)
print(2 <= 3)
print(3 == 2)
print(3 != 2)
print(len('mango') == len('avocado'))
print(len('mango') != len('avocado'))
print(len('mango') < len('avocado'))
print(len('milk') < len('meat'))
print(len('milk') == len('meat')) 
print(len('python') > len('dragon')) 

print('True == True: ', True == True)

# is - returns true if both variables are the same object
# is not- Returns true if both variables are not the same object
# in - Returns True if the queried list contains a certain item
# not in - Returns True if the queried list doesn't have a certain item