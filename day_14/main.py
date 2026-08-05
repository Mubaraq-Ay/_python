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

# ps - a variable can store a function

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


def laugh():
    return '😂😂😂'

def execute(func):
    return func()

print(execute(laugh))

def add():
    return 2 + 3
def subtract():
    return 10 - 4
def calculator(func):
    return func()

print(calculator(add))
print(calculator(subtract))

def subtract_num(num):
  def subtract(number):
     return number - num
  return subtract

minus_five = subtract_num(5)

print(minus_five(7))


def tax(amt):
    def tax_amt(amount):
        return amount * (1 + amt / 100)
    return tax_amt

add_vat = tax(7.5)

print(add_vat(100))


# python decorators
# decorator is a design pattern in python that allows a user to add new functionality to an existing object without modifying its structure

# creating decorators

# normal function
def greeting():
    return 'welcome to python'
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
g = uppercase_decorator(greeting)
print(g())

# implementing the example above with a decorator.
'''this decorator function is a higher order function that takes a function as a parameter'''

def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
@uppercase_decorator
def greeting():
    return 'welcome to python'
print(greeting())


def star_decorator(function):
    def wrapper():
        result = function()
        return f'***{result}***'
    return wrapper

@star_decorator
def greet():
    return 'hello'
print(greet())


def excited(func):
    def greet():
        msg = func()
        return f'{msg}!!!'
    return greet

@excited
def greet():
    return 'welcome'
print(greet())


def bracket(func):
    def city():
        result = func()
        return f'[{result}]'
    return city

@bracket
def city():
    return 'lagos'
print(city())

def emoji(func):
    def name():
        result = func()
        return f'😎 {result} 😎'
    return name

@emoji
def name():
    return 'mubaraq'
print(name())

def uppercase(func):
    def school():
        result = func()
        make_upper = result.upper()
        return f'{make_upper}'
    return school

@uppercase
def school():
    return 'mandem university'
print(school())

def log(func):
    def run():
        rs = func()
        return f'Running function...\n{rs}'
    return run

@log
def run():
    return 'hello'
print(run())


def repeat(func):
    def laugh():
        rs = func()
        return f'{rs * 3}'
    return laugh


@repeat
def laugh():
    return "😂"
print(laugh())


# applying multiple decorators to a single function 
# decoratorception
'''The decorator closest to the function is applied first.
The outer decorator wraps the result of the first one.'''

# first decorator
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

# second decorator
def split_string_decorator(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string
    return wrapper

# decorators would be executed from the top
@split_string_decorator
@uppercase_decorator
def greeting():
    return 'hello mubaraq welcome'
print(greeting())

# some tasks..

def question(func):
    def greet():
        rs = func()
        return rs + '?'
    return greet

@question
def greet():
    return 'how are you'
print(greet())

def double(func):
    def laugh():
        rs = func()
        return rs * 2
    return laugh

@double
def laugh():
    return "😂"
print(laugh())


def money(func):
    def salary():
        rs = func()
        return f'₦{rs}'
    return salary

@money
def salary():
    return 50000000000
print(salary())

def uppercase(func):
    def bank():
        rs = func()
        upper = rs.upper()
        return upper
    return bank

@uppercase
@money
def bank():
    return 'flutterwave'
print(bank())

def border(func): 
    def title():
      rs = func() 
      return f'======================\n {rs} \n======================' 
    return title 

@border 
def title(): 
    return 'SYSTEM HEALTH CHECKER' 
print(title())

# accepting parameters in decorator functions
# we might need our functions to take parameters, so we might need to define a decorator that accepts parameters.

def decorator_with_parameters(function):
    def wrapper_accepting_parameters(param1, param2, param3):
        function(param1, param2, param3)
        print(f'i live in {param3}')
    return wrapper_accepting_parameters

@decorator_with_parameters
def print_full_name(first_name, last_name, country):
    print(f'i am {first_name} {last_name}. i love to teach {country}.')
print_full_name('mubaraq', 'ayanleke', 'saudi')


# built-in higher order functions
# map(), filter, reduce. lambda function can be passed as a parameter and the best use case is in functions like map, filter and reduce

# map function
# this is a built-in function that takes a function and iterable as parameters.
# syntax -- map(function, iterable)

# example 1
numbers = [1, 2, 3, 4, 5]
def square(x):
    return x ** 2
numbers_squared = map(square, numbers)
print(list(numbers_squared))

# applying within a lambda function
numbers_squared = map(lambda x : x ** 2, numbers)
print(list(numbers_squared))

# example 2
numbers_str = ['1', '2', '3', '4', '5']
numbers_int = map(int, numbers_str)
print(list(numbers_int))

# example 3
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']

def change_to_upper(name):
    return name.upper()

names_upper_cased = map(change_to_upper, names)
print(list(names_upper_cased))

# applying with a lambda function
names_upper_cased = map(lambda name: name.upper(), names)
print(list(names_upper_cased))