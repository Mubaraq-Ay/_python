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
# this is an inner function that remembers variables from the outer function, even after the outer function has finished running.

def add_ten():
    ten  = 10
    def add(num):
        return num + ten
    return add

closure_result = add_ten()
print(closure_result(5))
print(closure_result(10))

def add_five():
    five = 5
    def add(num):
        return num + five
    return add

plus_five = add_five()
print(plus_five(10))
print(plus_five(30))
print(plus_five(-2))


def multiply_by(number):
    def multiply(num):
        return number * num
    return multiply

double = multiply_by(2)
triple = multiply_by(3)

print(double(2))
print(triple(2))

def say_hello(name):
    def greeting():
        return f'hello {name}'
    return greeting

greet_mubaraq = say_hello('mubaraq')
greet_amad = say_hello('amad')

print(greet_mubaraq())

def add_number(number):
    def numb(num):
        return number + num
    return numb

add_five = add_number(5)
print(add_five(3))