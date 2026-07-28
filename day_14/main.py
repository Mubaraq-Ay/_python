# higher order functions
# functions are not just things that run code. they're values like number or string , we can pass them around, store them and hand them to other functions.

# A function can take one or more functions as parameters
# A function can be returned as a result of another function
# A function can be modified
# A function can be assigned to a variable

# function as a parameter.

def sum_numbers(nums):  # normal function
    return sum(nums)    # a sad function abusing the built-in sum function :<

def highest_order_function(f, lst):
    summation = f(lst)
    return summation
result = highest_order_function(sum_numbers, [1,2,3,4,5])
print(result)

def greet(): # a normal function.
    print('hello')

def run(func):
    func()

run(greet)


# function as a return value
def square(x):
    return x ** 2
print(square(2))

def cube(x):
    return x ** 3

def absolute(x): # an absolute value.
    if x >= 0:
        return x
    else:
        return -(x)
print(absolute(1))

# a higher order function returning a function
def highest_order_function(type):
    if type == 'square':
        return square
    elif type == 'cube':
        return cube
    elif type == 'absolute':
        return absolute

result = highest_order_function('square')
print(result(3))
result = highest_order_function('cube')
print(result(3))
result = highest_order_function('absolute')
print(result(-3))

# python closures.