# functions.

# A function is a reusable block of code that performs a specific task and can be called whenever it is needed.
# we use def keyword.

# function without parameters.
# function can be declared without parameters.

def generate_full_name():
    first_name = 'mubaraq'
    last_name = 'ayanleke'
    space = ' '
    full_name = first_name + space + last_name
    print(full_name)
generate_full_name() # calling a function

def add_two_numbers():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    print(total)
add_two_numbers()


# function returning a value - part 1

# function return values using the return statement. 
# if a function has no return statement, it returns None.

def generate_full_name():
    first_name = 'mubaraq'
    last_name = 'ayanleke'
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print(generate_full_name())


# tasks

def say_hello():
    say_hello = 'hello!'
    print(say_hello)
say_hello()
say_hello()
say_hello() # calling the function 3 times.

# 2

def school_name():
    school_name ='oui'
    print(school_name)
school_name()


# 3

def favorite_language():
    fav_language = 'python'
    return fav_language
print(favorite_language())

# 4

def favorite_number():
    favorite_number = 1
    return favorite_number
print(favorite_number())

# 5

def multiply():
    nums = 7 * 9
    return nums
print(multiply())


# 6

def print_name():
    print("Mubaraq")
print(print_name()) # none, because it has no return statement.

def return_name():
    return "Mubaraq"
print(return_name())


# 7

# write a function that returns my full name.

def full_name():
    first_name = 'mubaraq'
    last_name = 'ayanleke'
    full_name = f'{first_name} {last_name}'
    return full_name
print(full_name().upper())
    

# function with parameters.

def greetings (name):
    message = name + ' , welcome to python for everyone!'
    return message

print(greetings('mubaraq'))

def add_ten(num):
    ten = 10
    return num + ten
print(add_ten(22))

def square_number(x):
    return x ** 2
print(square_number(2))

def area_of_a_circle(r):
    PI = 3.14
    area = PI * r ** 2
    return area
print(area_of_a_circle(10))

def sum_of_numbers(n):
    total = 0
    for i in range(n+1):
        total += i
    return total
print(sum_of_numbers(10))
print(sum_of_numbers(100))

# tasks

def say_name(name):
    return f'my name is {name}'
print(say_name('mubaraq'))

# 2

def double_number(number):
    return number * 2
print(double_number(4))


# 3

def cube(number):
    return number ** 3
print(cube(2))

# 4

def is_even(number):
   if number % 2 == 0:
      return f'{number}: ', True
   else:
       return f'{number}: ', False   
print(is_even(5))

# 5

def full_name(first_name, last_name):
    return f'{first_name} {last_name}'
print(full_name('mubaraq', 'ayanleke'))

# 6

def largest(a, b):
    if a >= b:
        return a
    else:
        return b

print(largest(6,14))

# 7

def rectangle_area(length, width):
    area = length * width 
    return area
print(rectangle_area(2, 1))

# 8

def greet(name, language):
    if language == 'English':
        return f'Hello, {name}'
    elif language == 'French':
        return f'Bonjour, {name}'
    else:
        return 'language not supported.'
print(greet('mubaraq', 'English'))

# 9
# calculator.

def calculator(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        return a / b
    else:
        return 'invalid.'
print(calculator(1, 2, '*'))

# 10

# def count_vowels(word):
#     vowels = 'aeiou'
#     for i in word:
#         count = 0
#         count += 1
#         if i in vowels:
#          return i
# print(count_vowels('eeee'))


# function with two parameters.

def generate_full_name(first_name, last_name):
    full_name = f'{first_name} {last_name}'
    return full_name
print('Full name:',generate_full_name('mubby', 'jr'))

def sum_two_numbers(num_one, num_two):
    sum = num_one + num_two
    return sum
print('sum of two numbers:', sum_two_numbers(2, 6))

def calculate_age(current_year, birth_year):
    age = current_year - birth_year
    return age
print('age:', calculate_age(2026, 2008))

def weight_of_object(mass, gravity):
    weight = str(mass * gravity)+ ' N' # converting to str so i'd be able to join them.
    return weight
print('weight of an object in newton:', weight_of_object(11, 10))


# passing argument with key and value.

def print_fullname(firstname, lastname):
    full_name = f'{firstname} {lastname}'
    print(full_name)
print_fullname(firstname= 'mubaraq', lastname= 'ayanleke') 

def add_two_numbers(num1, num2):
    total = num1 + num2
    return total
print(add_two_numbers(num2= 3, num1= 2)) # order does not matter.


# function returning a value - part 2

# returning a string
def print_name(firstname):
    return firstname
print_name(firstname= 'mubaraq')

def print_full_name(firstname, lastname):
    full_name = f'{firstname} {lastname}'
    return full_name
print_full_name(firstname= 'mubaraq', lastname='ayanleke')

# returning a number.

def add_two_numbers(num1, num2):
    total = num1 + num2
    return total
print(add_two_numbers(2, 3))

def calculate_age(current_year, birth_year):
    age = current_year - birth_year
    return age
print(calculate_age(2026, 2008))


# returnign a boolean.

def is_even(n):
    if n % 2 == 0:
        return True
    return False
print(is_even(10))
print(is_even(7))

# returning a list.

def find_even_number(n):
    evens = []
    for i in range(n + 1):
        if i % 2 == 0:
            evens.append(i)
    return evens
print(find_even_number(10))


# function with default parameters

def greetings (name = 'mubby'):
    message = f'{name}, welcome to python for everyone!'
    return message
print(greetings())  
print(greetings('mubaraq'))  

def generate_full_name(first_name = 'mubaraq', last_name= 'ayanleke'):
    full_name = f'{first_name} {last_name}'
    return full_name
print(generate_full_name())
print(generate_full_name('ay','mubby'))

def calculate_age(birth_year, current_year = 2021):
    age = current_year - birth_year
    return age
print('age: ', calculate_age(2008))

def weight_of_object(mass, gravity = 9.81):
    weight = str(mass * gravity)+ ' N'
    return weight
print('weight of object in Newton: ', weight_of_object(100))
print('weight of an object in Newton: ', weight_of_object(100, 10))


# arbitrary numbers of arguments

def sum_all_nums(*nums):
    total = 0
    for num in nums:
        total += num
    return total
print(sum_all_nums(2,3,5))

# default and arbitrary number of parameters in functions.

def generate_groups(team, *args):
    print(team)
    for i in args:
        print(i)
print(generate_groups('team-1', 'mubaraq', 'mubby', 'robin', 'khabib'))


# dictionary unpacking
# calling a function which has named arguments using dictionary with matching key names using **

def greet(name='mubaraq', location='delaware'):
    # print a greeting message using the provided arguments
    print(f'hi there {name} how is the weather in {location}')

# call the function using keyword arguments
greet(name='mubaraq', location='delaware')

# create a dictionary with keys matching the function's parameter names.

my_dict = {
    'name': 'mubaraq',
    'location': 'delaware'
}

# call the function using dictionary unpacking.
greet(**my_dict)
# the ** operator unpacks the dictionary, passing its key-value pairs as keyword arguments to the function.

# tsk

# create a function
def create_car(brand, model, year):
    print(f' Brand: {brand} \n Model: {model} \n Year: {year}')
    
car = {
    'brand': 'toyota',
    'model': 'camry',
    'year': 2022
}

create_car(**car)

# default parameters

def create_phone(brand='samsung', model='s25', storage='512'):
    print(f' brand: {brand} \n model: {model} \n storage: {storage}')

phone = {
    'brand': 'google',
    'model': 'pixel 10'
}

create_phone(**phone)
