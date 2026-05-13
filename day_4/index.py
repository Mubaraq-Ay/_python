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

first_name = 'mubaraq'
last_name = 'ayanleke'
language = 'python'
formatted_string = 'I am {} {}. i teach {}'.format(first_name, last_name, language)
print(formatted_string)

a = 4
b = 3

print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b))
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))

# strings and numbers
radius = 10
pi = 3.14
area = pi * radius ** 2
formatted_string = 'the area of a circle with a radius {} is {:.2f}.'.format(radius, pi)

print(formatted_string)