# execption handling

# Exception handling is the process of detecting and responding to runtime exceptions so the program can handle failures instead of crashing unexpectedly.
# runtime error is an application error that occurs during program execution after the code has been successfully compiled or interpreted.

# it catches the error before python prints it.
# (graceful handling)

# try:
#     print(10 + '5')
# except:
#     print('something went wrong') # would raise a type error.

# try:
#     name = input('enter your name: ')
#     year_born = int(input('year you were born: '))
#     age = 2019 - year_born
#     print(f'you are {name} and your age is {age}')
# except:
#     print('something went wrong')


# try:
#     name = input('enter your name: ')
#     year_born = int(input('year you were born: '))
#     age = 2017 - year_born
#     print(f'your name is {name} and your age is {age}')
# except TypeError as e:
#     print(f'type error occured: {e}')
# except ValueError as e:
#     print(f'value error occured: {e}')
# except ZeroDivisionError:
#     print('zero division error occured')


# e. - this brings the real message python generated



# def safe_divide(a, b):
#     try:
#         result = a / b
#         print(f'result: {result}')
#     except ZeroDivisionError as e:
#         print(f'cannot divide by zero: {e}')
#     except TypeError as e:
#         print(f'both values need to be numbers: {e}')

# safe_divide(10, 2)
# safe_divide(10, 0)
# safe_divide('a', 2)



# def get_number():
#     try:
#         num = int(input('enter a valid number: '))
#         print(f'you entered {num}')
#     except ValueError:
#         print('pls enter a valid number.')

# get_number()




# def get_item(items, index):
#     try:
#         items = ['Python', 'Linux', 'Docker']
#         print(f'{items[index]}')
#     except IndexError:
#         print('index does not exist.')

#     get_item(items, 2)

# def safe_divide(a, b):
#     try:
#         result = a / b
#         print(f'{result}')
#     except ZeroDivisionError:
#         print('you cannot divide a number by zero.')
#     except TypeError:
#         print('only two integers can be divided.')

# safe_divide(2, 'w')

# def calculate_age():
#     try:
#         name = input('name: ')
#         birth_year = int(input('birth year: '))
#         age = 2026 - birth_year
#         print(f'your name is {name} and you are {age} years old.')
#     except ValueError:
#         print('enter your valid date of birth')

# calculate_age()

# def get_student_info(key):
#     try:
#         student = {
#     "name": "Mubaraq",
#     "age": 18,
#     "level": 200
# }
#         print(f'{student[key]}')
#     except KeyError:
#         print('enter the correct key.')

# get_student_info('age')

 

# def safe_list_access(my_list, index):
#     try:
#         print(f'{my_list[index]}')
#     except IndexError:
#         print('could not find index.')
#     except TypeError:
#         print('wrong type')

# my_list = [1, 2, 3]
# safe_list_access(my_list, 4)

# to raise an error manually, we use keyword raise

# raising exception and custom exception

# def set_age(age):
#     if age < 0:
#         raise ValueError('age cannot be negative.')
#     print(f'age set to {age}')

# set_age(-1)

# using try except.

def set_age(age):
    try:
        if age < 0:
            raise ValueError('age cannot be negative.')
        print(f'age set to {age}')
    except ValueError as e:
        print(f'invalid input {e}')

set_age(0)


def set_password(password):
    try:
        if len(password) < 8:
            raise ValueError('password cannot be shorter than 8 characters.')
        print('password set!')
    except ValueError as e:
        print(f'set better password bro {e}')

set_password('12349568')


class InsufficientFundsError(Exception):
    pass

def withdraw(balance, amount):
    try:
        if amount > balance:
            raise InsufficientFundsError('insufficient funds!')
        print(f'transfer of {amount} successful')
    except InsufficientFundsError as e:
        print(f'transfer failed; {e}')

withdraw(20, 30)


class OutOfStockError(Exception):
    pass

def process_order(item_price, quantity, stock_available):
    try:
        if quantity > stock_available:
            raise OutOfStockError('out of stock.')
        if item_price < 0 or quantity < 0:
            raise ValueError('quantity or item price cannot be zero')
        total = item_price * quantity
        print(f'order successful!; {total}')

        
    except OutOfStockError as e:
        print(f'pls reduce the quantity. {e}')
    except ValueError as e:
        print(f'item price cannot be zero: {e}')

process_order(50, 2, 10)
process_order(20, 10, 2)
process_order(-39, 2, 2)


# try:
#     name = input('enter your name: ')
#     year_born = int(input('year you born: '))
#     age = 2026 - year_born
#     print(f'you are {name}. and your age is {age}.')
# except TypeError:
#     print('type error occured')
# except ValueError:
#     print('value error occured')
# except ZeroDivisionError:
#     print('zero division error occured')
# else:
#     print('i usually run with the try block')
# finally:
#     print('i always run.')

# else - the risky operation ran, now do this.
# finally - runs regardless of whether an exception happened or not.


# packing and unpacking arguments in python.

# we use two operators.

# * for tuples and
# ** for dictionaries.

# unpacking. (unpacking lists)

def sum_of_five_nums(a, b, c, d ,e):
    return a + b + c + d + e

lst = [1, 2, 3, 4, 5]
print(sum_of_five_nums(*lst))

# we can also use unpacking in the range built-in function that expects a start and an end.

numbers = range(2, 7)
print(list(numbers))
args = [2, 7]
numbers = range(*args)
print(numbers)

# a tuple or a list can also be unpacked like this

countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
fin, sw, nor, *rest = countries
print(fin, sw, nor, rest)

numbers = [1,2,3,4,5,6,7]
one, *middle, last = numbers
print(one, middle, last)

# unpacking dictionaries.

def unpacking_person_info(name, country, city, age):
    return f'{name} lives in {country}, {city}. he is {age} years old'
dct = {
    'name': 'mubaraq',
    'country': 'nig', 
    'city': 'lag',
    'age': '250'
}

print(unpacking_person_info(**dct))

# packing lists

def sum_all(*args):
    s = 0
    for i in args:
        s += i
    return s
print(sum_all(1,2,3)) 
print(sum_all(1,2,3,4,5,6,6,7))

# packing dictionaries

def packing_person_info(**kwargs):
    # check the type of kwargs and it is a dict type
    # print(type(kwargs))
    # printing dictionary items
    for key in kwargs:
        print(f'{key} = {kwargs[key]}')
    return kwargs
print(packing_person_info(
      name="Asabeneh",
      country="Finland", 
      city="Helsinki", 
      age=250
))


# spreading in python

lst_one = [1, 2, 3]
lst_two = [4, 5, 6, 7]
lst = [0, *lst_one, *lst_two]
print(lst)
country_lst_one = ['Finland', 'Sweden', 'Norway']
country_lst_two = ['Denmark', 'Iceland']
nordic_countries = [*country_lst_one, *country_lst_two]
print(nordic_countries)