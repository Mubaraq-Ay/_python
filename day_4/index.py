# strings. 

# letter = 'p'
# print(letter)
# print(len(letter))

# greeting = 'hello, world!'
# print(greeting)
# print(len(greeting))

# sentence = 'i hope you are enjoying 30 days of python challenge'
# print(sentence)
# print(len(sentence))

# # multiline string

# multiline_string = '''my name is mubaraq and i enjoy coding and solving logical tasks'''
# print(multiline_string)

# multiline_string = """my name is mubaraq and i enjoy coding and solving logical problems."""
# print(multiline_string)

# # concatenation

# first_name = 'mubaraq'
# last_name = 'ayanleke'
# space = ' '

# full_name = first_name + space + last_name
# print(full_name)

# # checking the length of a string using len() built in function

# print(len(first_name))
# print(len(last_name))
# print(len(full_name))
# print(len(first_name) > len(last_name))

# escape sequences in strings

''' \n - new line
    \t - Tab means(8 spaces)
    \\ - back slash
    \' - single quote
    \" - double quote
'''

# print('i hope everyone is enjoying the python challenge. \nAre you?')
# print('Days\tTopics\tExercises') # adding tab space or 4 spaces.
# print('Day 1\t5\t5')
# print('Day 2\t6\t20')
# print('Day 3\t5\t23')
# print('Day 4\t1\t35')

# print('this is a backlash symbol (\\)')
# print('in every programming language it starts with \"hello, world!\"')

# string formatting

# old style formatting ( % operator )

# %s - string
# %d - integers
# %f - floating point numbers
# "%.number of digitsf" - decimal places

# for strings only

# first_name = 'mubaraq'
# last_name = 'ayanleke'
# language = 'python'
# formatted_string = 'I am %s %s. i teach %s' %(first_name, last_name, language)

# print(formatted_string)

# # for strings and numbers

# radius = 10
# pi = 3.14
# area = pi * radius ** 2
# formatted_string = 'the area of circle with a radius %d is %.2f' %(radius, area)

# print(formatted_string)

# python_libraries = ['django', 'flask', 'numpy', 'matplotlib', 'pandas']
# formatted_string = 'the following are python libraries:%s' % (python_libraries)

# print(formatted_string)

# my_name = 'mubaraq'
# age = 18

# formatting_result = "my name is %s and i'm %d years old" % (my_name, age)
# print(formatting_result)

# float_num = 2.33455
# print('to 3d.p: %.3f' % float_num)

# height = 189.66

# print("my name is %s, i'm %d years old, and my height is %.2f"  % (my_name, age, height))

# country = 'Nigeria'
# population = 220000000
# growth_rate = 2.58

# print("%s has a population of %d people with a growth rate of %.2f%%" % (country, population, growth_rate))

# item = 'laptop'
# price = 850.5678
# quantity = 3
# total = quantity * price

# print("item: %s | price: %.2f | quantity: %d | total: %.2f " % (item, price, quantity, total))

# new style (str) it was introduced in python version 3

# first_name = 'mubaraq'
# last_name = 'ayanleke'
# language = 'python'
# formatted_string = 'I am {} {}. i teach {}'.format(first_name, last_name, language)
# print(formatted_string)

# a = 4
# b = 3

# print('{} + {} = {}'.format(a, b, a + b))
# print('{} - {} = {}'.format(a, b, a - b))
# print('{} * {} = {}'.format(a, b, a * b))
# print('{} / {} = {:.2f}'.format(a, b, a / b))
# print('{} % {} = {}'.format(a, b, a % b))
# print('{} // {} = {}'.format(a, b, a // b))
# print('{} ** {} = {}'.format(a, b, a ** b))

# # strings and numbers
# radius = 10
# pi = 3.14
# area = pi * radius ** 2
# formatted_string = 'the area of a circle with a radius {} is {:.2f}.'.format(radius, pi)

# print(formatted_string)

# city = 'lagos'
# temp = 31.4567
# humidity = 78

# result = 'City: {} | Temp: {:.2f}°C | Humidity: {}%'.format(city, temp, humidity)
# print(result)


# student = 'mubaraq'
# score = 87.6789
# total = 100

# rs_log = '{} scored {:.2f} out of {} which is {:.2f}%'.format(student, score, total, score/total * 100)
# print(rs_log)

# a = 15
# b = 4

# total = '{} + {} = {}'.format(a, b, a + b)
# print(total)

# minus = '{} - {} = {}'.format(a, b, a - b)
# print(minus)

# multiply = '{} * {} = {}'.format(a, b, a * b)
# print(multiply)

# divide = '{} / {} = {:.2f}'.format(a, b, a / b)
# print(divide)

# modulus = '{} % {} = {}'.format(a, b, a % b)
# print(modulus)

# floor_division = '{} // {} = {}'.format(a, b, a // b)
# print(floor_division)

# exponential = '{} ** {} = {}'.format(a, b, a ** b)
# print(exponential)


# string interpolation / f-strings (python 3.6+)

# a = 4
# b = 3
# print(f'{a} + {b} = {a + b}')
# print(f'{a} - {b} = {a - b}')
# print(f"{a} * {b} = {a * b}")
# print(f'{a} / {b} = {a / b:.2f}')
# print(f'{a} % {b} = {a % b}')
# print(f'{a} // {b} = {a // b}')
# print(f'{a} ** {b} = {a ** b}')


# # tasks

# name = 'mubaraq'
# age = 18
# city = 'lagos'
# stack = 'python'

# print(f'my name is {name}, i am {age} years old, i live in {city} and i code in {stack}')

# price = 1500.6789
# discount = 10 
# discount_amt = price * (discount / 100)
# final_price = price - discount_amt

# print(f'original price: ${price:.2f} | discout: {discount}% | final price: ${final_price:.2f}')

# first = 'python'
# second = 'programming'

# print(f"'{first}' has {len(first)} characters and '{second}' has {len(second)} characters. \n'{second}' is longer.")


# #tasks

# product = 'macbook pro'
# original_price = 2499.999
# tax_rate = 7.5
# tax_amt = tax_rate / 100 * original_price
# total = original_price + tax_amt

# print(f" Product: {product.capitalize()} | Price: ${original_price:.2f} | Tax: ${tax_amt:.2f} | Total: ${total:.2f}")


# # python strings as sequences of characters
# # In Python, a string is treated as a sequence of characters. That means each character has a position called an index.
 
# # unpacking characters

# language = 'python'
# a,b,c,d,e,f = language
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)
# print(f)

# accessing characters in strings by index

language = 'python'
# first_letter = language[0]
# print(first_letter)
# second_letter = language[1]
# print(second_letter)
# last_index = len(language) - 1
# print(last_index)
# last_letter = language[last_index]
# print(last_letter)

# counting backwards

# last_letter = language[-1]
# print(last_letter)
# second_last = language[-2]
# print(second_last)

# tasks, some are wromg

# word = 'developer'
# first_char = word[0]
# print(first_char)
# last_char = word[-1]
# print(last_char)
# # last_char_len = len(word) - 1 
# # print(last_char_len)  
# # fifth_character = word[4]
# # print(fifth_character)

# name = 'mubaraq'
# # last_three_char = name[(-1, -2)]
# # print(last_three_char)
# # first_three_names = name[{0,1,2}]
# # print(first_three_names)

# a,b,c,d,e,f,g = name
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)
# print(f)
# print(g)

# sentence = 'backend engineering'
# print(sentence[0])
# print(sentence[-1])
# print(sentence[8])
# print(len(sentence))
# print(len(word) - 1) 


# slicing

# language = 'python'
# first_three = language[0:3] # starts at zero index and up to 3 but not include 3
# print(first_three)
# last_three = language[3:6]
# print(last_three)

# # another way
# last_three = language[-3:]
# print(last_three)
# last_three = language[3:]
# print(last_three)

# # reversing a string

# greeting = 'hello, world!'
# print(greeting[::-1])

# skipping while slicing

# language = 'python'

# print(language[0:6:2])
# print(language[::2])
# print(language[::3])


# # tasks

# word = 'engineering'
# print(word[0:4])
# print(word[-4:])
# print(word[3:8])
# print(word[::-1])
# print(word[::2])

# # task 2

# full_name = 'mubaraq ayanleke'
# first_name = full_name[:7]
# print('first name:', first_name)
# last_name = full_name[8:]
# print('last name:', last_name )

# reversed = full_name[::-1]
# print('reversed:', reversed)

# initials = f'{full_name[0].upper()}.{full_name[8].upper()}'
# print(initials)

# # task 3

# sentence = 'backend development is my path'
# print(sentence[0:7])
# print(sentence[-4:])
# print(sentence[8:18])
# print(sentence[::-1])
# print(sentence[::3])


# string methods
# capitalize() - converts the first character of the string to capital letter

challenge = 'thirty days of python'
print(challenge.capitalize())

